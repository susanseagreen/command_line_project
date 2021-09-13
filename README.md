## Getting started
Setup Virtual environment<br/>
`python -m venv env`
`env\Scripts\activate.bat`
Install project requirements<br/>
`pip install -r requirements.txt`

This script adds various filters to a chosen image and re-saves it to the users chosen name and image type. <br/>
To get started, Type 'python add_filters.py <image> <save_as> <filters>'<br/>
Defaults for image are 'input.jpg' and save file name is 'new.jpg.<br/>
These can be left blank if you want to use the default values'<br/>

## View console help
`python help.py`

## Run Tests
`python test_filters.py`

### User Options:
Codes                | Vars             | High level
-------------------- | ---------------- | -------------
  -o, --overlay      | <IMG INT INT>    | <image_name> <x coordinates> <y coordinates>
  -b, --brightness   | FLOAT            | <brightness_value>
  -r, --rotate       | INTEGER          | <degrees>
  -s, --saturate     | FLOAT            | <saturation_value>
  -f, --filters      | TEXT             | <filter_options>

Filter options: [blur / contour / detail / edge_enhance / edge_enhance_more / emboss / find_edges / smooth / smooth_more / sharpen / grayscale / flip, mirror]

-------------------------------------
## Original Challenge Requirements

### Python coding challenge

This exercise is not related to web development. This is on purpose because frameworks like Django and Flask
dictate a common way of working. For this reason we use this test to see more generic programming skills
and creativity.

### Exercise

Create a commandline script that applies 1 or more filters to an image and saves it as a new file. 

The filters should be:

1. `gray_scale` convert the image to black and white.
2. `overlay` overlay a given image on top of the source.
3. `rotate` rotate N degrees. (no need for resizing/cropping)
4. Optionally, make up your own filter. Not required.

Other requirements:

* All parameters should be given in one line. (no interactive approach using `input()`)
* Each filter should be optional. 
* The order of filters is important since we want to be able to control if the overlay will become black and white or not. 
* The source image should be given as a filename on the command line.
* The overlay image should also be given as a filename on the command line and should be a transparent png.
* The number of degrees should be given on the command line.
* The output file should be given as a filename on the command line. (Support saving as png and jpg)
* Allow applying a filter more than once. (for example: gray_scale > rotate > overlay > rotate)
* Think about extensibility. How can you make it easy (for future you) to allow adding a new filter without changing a lot of code.
* Add unittests to test individual components of your program. Add instructions on how to run the tests.
* Follow PEP8 guidelines.

Images input.jpg and overlay.png are provided to save you a little time.

Provide a zip file with the script and a README with instructions on how to use it.
Also include how much time you spent on it.

