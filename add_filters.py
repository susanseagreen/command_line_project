import sys
import os.path
import click
from PIL import Image, ImageChops, ImageOps, ImageEnhance
from common.helpers import (img_path, original, filter_choices)

# The below imports are used within the dynamic filters function
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)


class OrderedParamsCommand(click.Command):
    options = []

    def parse_args(self, ctx, args):
        ctx.params = {}
        # clear options if list already exists
        self.options.clear()
        parser = self.make_parser(ctx)
        opts, _, param_order = parser.parse_args(args=list(args))
        for param in param_order:
            if param.param_type_name != 'argument':
                self.options.append((param, opts[param.name].pop(0)))

        return super().parse_args(ctx, args)


@click.command(cls=OrderedParamsCommand)
@click.argument('images', default=["input.jpg", "new.jpg"], type=(str, str))
@click.option('overlays', '--overlay', '-o', multiple=True, type=(str, int, int))
@click.option('light', '--brightness', '-b', multiple=True, type=float)
@click.option('rotates', '--rotate', '-r', multiple=True, type=int)
@click.option('saturates', '--saturate', '-s', multiple=True, type=float)
@click.option('filters', '--filters', '-f', multiple=True,
              type=(click.Choice(filter_choices, case_sensitive=False)))
def add_filters(images, overlays, light, rotates, saturates, filters):
    img, save_name = images
    click.echo(f'Filters added to "{img}" and re-saved as "{save_name}"')

    img = Image.open(os.path.join(original, img))
    save_path = os.path.join(img_path, 'filtered', f'{save_name}')

    offset = 0
    if len(OrderedParamsCommand.options) > 0:
        for param, value in OrderedParamsCommand.options:
            if param.name.lower() == 'light':
                img = brightness(value, img)

            elif param.name.lower() == 'contrasts':
                img = contrast(value, img)

            elif param.name.lower() == 'overlays':
                img = overlay(value, img)

            elif param.name.lower() == 'rotates':
                img = rotate(value, img, offset)

            elif param.name.lower() == 'saturates':
                img = saturate(value, img)

            # Filters
            elif value.lower() == 'flip':
                img = flip(img)

            elif value.lower() == 'grayscale':
                img = grayscale(img)

            elif value.lower() == 'mirror':
                img = mirror(img)

            else:
                img = dynamic_filters(value, img)

    img.save(save_path)
    img.show()


# Dynamically convert the filter strings to class
def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def brightness(value, img):

    click.echo(f'Brightness({value}) filter')
    img = ImageEnhance.Brightness(img)
    img = img.enhance(float(value))

    return img


def contrast(value, img):

    click.echo(f'Contrast({value}) filter')
    img = ImageEnhance.Contrast(img)

    return img


def overlay(value, img):

    click.echo('Overlay filter')
    overlay_img = value[0]
    x = int(value[1])
    y = int(value[2])
    img_overlay = Image.open(os.path.join(original, overlay_img))
    img_overlay = img_overlay.convert('RGBA')
    img.paste(img_overlay, (x, y), img_overlay)

    return img


def rotate(value, img, offset):

    click.echo(f'Rotate({value}deg) filter')
    offset += int(value)
    # expand is being used in order to stop the image edges from being cropped as the image turns
    img = img.rotate(int(value), expand=True)

    # We only want to crop images with black border edges if offset is divisible by 90 degrees
    # This is to stop edges being cut off on the image when it is at an angle
    if offset % 90 == 0:
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            img = img.crop(bbox)

    return img


def saturate(value, img):

    click.echo(f'Saturate({value}) filter')
    img = ImageEnhance.Color(img)
    img = img.enhance(float(value))

    return img


def flip(img):

    click.echo('Flip filter')
    img = ImageOps.flip(img)

    return img


def grayscale(img):

    click.echo('Grayscale filter')
    img = ImageEnhance.Color(img)
    img = img.enhance(0)

    return img


def mirror(img):

    click.echo('Mirror filter')
    img = ImageOps.mirror(img)

    return img


def dynamic_filters(value, img):

    click.echo(f'{value.title()} filter')
    # we can not pass strings through img.filter() so this needs to be converted to a class
    filter_type = str_to_class(value.upper())
    img = img.filter(filter_type)

    return img


if __name__ == '__main__':
    add_filters()
