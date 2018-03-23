# -*- coding: utf-8 -*-

from flask import Flask, render_template, Markup
import markdown

import os
from shutil import copyfile

"""
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


def make_content(filepath_in, urlify=True, fix_images=True):
    image_dir = os.path.dirname(filepath_in) + '/'
    copy_images_to_static(image_dir)  # makes a copy of the images found in the content's local /images folder

    with open(filepath_in, encoding='utf-8', errors='ignore') as md_content:
        md_content = md_content.readlines()
        for j, line in enumerate(md_content):
            if urlify:
                line = ensure_url(line)
            if fix_images:
                line = ensure_images(line)
            md_content[j] = line
        result = ''.join(md_content)

    html_content = markdown_to_html(result)
    output = html_content
    return output



app = Flask(__name__)

test_file = './static/content/introduction to git/git-readme.md'
content = make_content(test_file)

@app.route('/')
def main_page():
    global content
    return render_template('presentation.html',
                           content=content)



if __name__ == '__main__':
    app.run()