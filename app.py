# -*- coding: utf-8 -*-

from flask import Flask, render_template, Markup
import markdown

import os, re
from shutil import copyfile

"""
FORMAT
------
currently there are two extra tags to remember in addition to markdown formatting:
<!-- next slide --> : slices your slides into separate slides
(bg) : (WIP) takes your image and turns it into a background image (maybe alt-text="background" is more reliable?)

also takes
<h1> and <h2> tags and turns them into 'title page' style slides

------

NOTES
-----
Markdown workflow:
1. parse markdown into css through python's markdown library
2. match css style to github-markdown form css stylesheet embedded in layout.html

backslashes available in markdown:
\ backslash
` backtick
* asterisk
_ underscore
{} curly braces
[] square brackets
() parentheses
# hashmark
+ plus sign
- minus sign (hyphen) 
. dot
! exclamation mark

++ RESERVED CHARACTERS:
||| complete

"""


def markdown_to_html(md_content):
    return Markup(markdown.markdown(md_content))


def markdown_to_html_unescaped(md_content):
    return markdown.markdown(md_content)

def copy_images_to_static(src_dir, dst_dir='./static/images'):
    temp = list(os.walk(src_dir))
    destination_folder = dst_dir

    image_filepaths = []
    for group in temp:
        check = os.path.basename(group[0])
        if 'images' in check:
            for file in group[2]:
                image_filepaths.append(os.path.join(group[0], file))

    #print('images found: ')
    #[print(file) for file in image_filepaths]

    for file in image_filepaths:
        destination_path = os.path.join(destination_folder, os.path.basename(file))
        copyfile(file, destination_path)
        print('copied {0}  -->  {1}'.format(file, destination_path))


def ensure_url(line_of_text, split_key=' '):
    words = line_of_text.split(split_key)  # split lines by spacing
    for i, character in enumerate(words):
        if character[:4] == 'http':
            # add formatting to both urls in the middle and end of lines
            # (urls at the end of the line have a '\n' escape
            if character.endswith('\n'):
                words[i] = '<' + character.strip() + '>' + '\n'
            else:
                words[i] = '<' + character + '>'
    return split_key.join(words)


# todo: https://stackoverflow.com/questions/28207761/where-does-flask-look-for-image-files
def ensure_images(line_of_text, image_dir='./static/'):
    if './' in line_of_text:
        line_of_text = line_of_text.replace('./', image_dir, 1)
        print(line_of_text)
    return line_of_text


def convert_html_tags(html_string, html_tags=['h1', 'h2'], divider="<!--next slide-->"):
    for tag in html_tags:
        start_tag = '<{0}>'.format(tag)
        end_tag = '</{0}>'.format(tag)

        # start tag
        html_string = html_string.replace(start_tag, '{0}\n{1}'.format(divider, start_tag))
        #end tag
        html_string = html_string.replace(end_tag, '{0}\n{1}'.format(end_tag, divider))

    return html_string


# TODO: turn images into bg with the (bg) flag at the end of the markdown image
def convert_slides(html_string):
    # turns words from these tags into slides (usually titles)
    html_tags_to_convert = ['h1', 'h2']
    # add these classes into the div container
    classes_slides = "slide-divider scroll-area"
    classes_css = "slides"
    html_divider = "<!--next slide-->"

    temp = convert_html_tags(html_string, html_tags=html_tags_to_convert, divider=html_divider)

    temp = re.split('<!--\s*next slide\s*-->', temp)

    # cleaning the list of blank slides
    # only keep the bits that are longer than 2 characters
    temp = list(filter(lambda x: len(x) >= 2, temp))

    print(str(len(temp)) + ' slides found.')

    converted = []
    for i, stuff in enumerate(temp):
        if len(stuff) <= 1:
            print('deleting one empty slide')
        else:
            #print('appending ', stuff, '\n----------')
            converted.append(
                """
                <div class="{0}">
                    <div class="slide-frame">
                        <div class="{1}" id="slide{3}">
                            {2}
                        </div>
                    </div>
                </div>
                """.format(classes_slides, classes_css, stuff, i)
            )
    # print(converted[0])
    return ''.join(converted), len(temp)


def make_sidebar(num_slides):
    links = ['<li><a class="sidebar-link" href="#slide{0}">{0}</a></li>'.format(i) for i in range(num_slides)]
    sidebar_links = '\n'.join(links)
    #print(sidebar_links)
    return sidebar_links


def make_page(filepath_in, urlify=True, fix_images=True):
    image_dir = os.path.dirname(filepath_in) + '/'
    copy_images_to_static(image_dir)  # makes a copy of the images found in the content's local /images folder

    # open and preprocess file
    with open(filepath_in, encoding='utf-8', errors='ignore') as md_content:
        md_content = md_content.readlines()
        # DO MARKDOWN INJECTION HERE
        for j, line in enumerate(md_content):
            if urlify:
                line = ensure_url(line)
            if fix_images:
                line = ensure_images(line)
            md_content[j] = line
        result = ''.join(md_content)

    # create html content
    html_content = markdown_to_html_unescaped(result)
    html_content, num_slides = convert_slides(html_content)
    html_content = Markup(html_content)

    # create sidebar
    sidebar_content = Markup(make_sidebar(num_slides))

    #print(type(html_content))
    # DO HTML INJECTION HERE

    return html_content, sidebar_content




app = Flask(__name__)

test_file = './static/content/google earth engine/gee-readme.md'
content, sidebar_content = make_page(test_file)


@app.route('/')
def main_page():
    global content, sidebar_content
    return render_template('presentation.html',
                           content=content,
                           sidebar_content=sidebar_content)



if __name__ == '__main__':
    app.run()