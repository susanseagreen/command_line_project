import click
from common.helpers import filter_choices

help_brightness = "<brightness_value>"
help_overlay = "<image_name> <x coordinates> <y coordinates>"
help_rotate = "<degrees>"
help_saturate = "<saturation_value>"


@click.group()
@click.argument('images', default=["input.jpg", "new.jpg"], type=(str, str))
@click.option('overlays', '--overlay', '-o', multiple=True, type=(str, int, int), help=help_overlay)
@click.option('light', '--brightness', '-b', multiple=True, type=float, help=help_brightness)
@click.option('rotates', '--rotate', '-r', multiple=True, type=int, help=help_rotate)
@click.option('saturates', '--saturate', '-s', multiple=True, type=float, help=help_saturate)
@click.option('filters', '--filters', '-f', multiple=True,
              type=(click.Choice(filter_choices, case_sensitive=False)))
def click_help():
    '''This script adds various filters to a chosen image and re-saves it to the users chosen name and image
    type. To get started, Type 'python add_filters.py <image> <save_as> <filters>'
    Defaults for image are 'input.jpg' and save file name is 'new.jpg.
    These can be left blank if you want to use the default values'''
    pass


if __name__ == '__main__':
    click_help()
