# Google Earth Engine

## What is Google's Earth Engine?
google earth engine is a free platform for earth science data visualization and analysis, performed on a cloud and acessible anywhere through the internet

<!--next slide-->

Earth Engine is used for global-scale data mining

two ways to access google earth engine

1. [APIs for Python and Javascript](https://github.com/google/earthengine-api)
2. [Google's online Code Editor](https://code.earthengine.google.com)

<!-- next slide-->

![code editor](https://i.imgur.com/04ITJ9q.jpg)

The Code Editor (Javascript)
<!-- next slide-->

what can it do?

- [travel time from suburbs/villages to urban areas](https://medium.com/google-earth/mapping-global-travel-time-to-urban-resources-448c1d7919d2) [(code)](https://code.earthengine.google.com/203a274adc2bcd93c5b97176e1269ff6)
- [air quality in california](https://medium.com/google-earth/getting-hyper-local-mapping-street-level-air-quality-across-california-d5d2f8b2f6b9)

<!--next slide-->

[![night lights](https://img.youtube.com/vi/5-2pFViTqcs/0.jpg)](https://youtu.be/5-2pFViTqcs)

<!--next slide-->

[![night lights](https://img.youtube.com/vi/tpOv56c7MSs/0.jpg)](https://youtu.be/tpOv56c7MSs)

## Signup
signup is manual, please do so to code along with this workshop

<!--next slide-->
### note
JavaScript is not ES6 compatible
- no let, const
- no default arguments in functions

## Loading maps
Load maps from search
Load maps from csv - learn
Add maps (map.Addlayer)

## Filtering maps
Filter from image collection
By date (filterBounds)
By band (layer) (select)

## Computing over maps
- per pixel computation

<!--next slide-->
### Mean, Median, Max etc
link to code in earth engine with mean median and max examples

<!--next slide-->
### Subtract, Multiply etc
[source](https://developers.google.com/earth-engine/image_math)

link to code in earth engine with subtract(buiding heights) and multiply

<!--next slide-->
### false color computations (NDVI, NDBI)

![ndvi ndbi comparisons](http://oi64.tinypic.com/28k4kyr.jpg)

<!--next slide-->
NDVI, NDBI, NDWI, EVI... What are they?
they are calculations used to enhance different parts of the image (like special filters used to see vegetation and bare land)

things reflect different wavelengths

![spectral differences](https://i.imgur.com/7nLaNBK.png)

<!--next slide-->
[source](https://docs.google.com/document/d/1CMyCHwS1mYTeSZzj4HEpHNhaT9K5snunl2WRLy2iC0o/edit)
[mapping a function over a collection (multiple images)](https://developers.google.com/earth-engine/tutorial_api_06)

- NDVI : Normalized Difference **Vegetation** Index
- EVI : Enhanced **Vegetation** Index
- NDWI : Normalized Difference **Water** Index (Vegetation water content)
- NDWBI : alternative NDWI
- NDBI : Normalized Difference **Bare** Index (Urban Areas)
- BAI : **Burned** Area Index
- NBRT : Normalized **Burn** Ratio Thermal
- NDSI : Normalized Difference **Snow** Index

<!--next slide-->
[![NDVI](http://oi64.tinypic.com/ehxbgn.jpg)](https://code.earthengine.google.com/17d561960edfb29cf2a71531c50ef684)

<!--next slide-->
### classification (auto-labeling from examples)
Classify from map data - learn


## Exporting data
[source](https://developers.google.com/earth-engine/exporting)

Export (tiff for use) (visualize, then export for images)
Csv - learn
Image
Video - export video (needs 3 bands)
Some examples (ndvi)(ndbi)(height)(distance map)


which maps are interesting?
land cover
night lights
road accessibility
—————


Try this later

Get data from gee 

Do this tutorial
https://youtu.be/dbs4IYGfAXc

Display data in 3D 

