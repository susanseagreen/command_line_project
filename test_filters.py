import unittest
from add_filters import add_filters
from click.testing import CliRunner


class TestFilters(unittest.TestCase):

    # Test all filter types
    def test_blur(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_blur.jpg -f blur'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_blur.jpg"\n' \
               + 'Blur filter\n', result.output

    def test_brightness(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_brightness.jpg -b 0.1'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_brightness.jpg"\n' \
               + 'Brightness(0.1) filter\n', result.output

    def test_darkness(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_darkness.jpg -b 2'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_darkness.jpg"\n' \
               + 'Brightness(2) filter\n', result.output

    def test_contour(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_contour.jpg -f contour'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_contour.jpg"\n' \
                                'Contour filter\n', result.output

    def test_detail(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_detail.jpg -f detail'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_detail.jpg"\n' \
                                'Detail filter\n', result.output

    def test_edge_enhance(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_edge_enhance.jpg -f edge_enhance'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_edge_enhance.jpg"\n' \
                                'Edge_Enhance filter\n', result.output

    def test_edge_enhance_more(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_edge_enhance_more.jpg -f edge_enhance_more'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_edge_enhance_more.jpg"\n' \
                                'Edge_Enhance_More filter\n', result.output

    def test_emboss(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_emboss.jpg -f emboss'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_emboss.jpg"\n' \
                                'Emboss filter\n', result.output

    def test_find_edges(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_find_edges.jpg -f find_edges'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_find_edges.jpg"\n' \
                                'Find_Edges filter\n', result.output

    def test_flip(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_flip.jpg -f flip'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_flip.jpg"\n' \
                                'Flip filter\n', result.output

    def test_mirror(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_mirror.jpg -f mirror'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_mirror.jpg"\n' \
                                'Mirror filter\n', result.output

    def test_rotate_45(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_rotate_45.jpg -r 45'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_rotate_45.jpg"\n' \
               + 'Rotate(45deg) filter\n', result.output

    def test_rotate_left(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_rotate_left.jpg -r 90'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_rotate_left.jpg"\n' \
               + 'Rotate(90deg) filter\n', result.output

    def test_rotate_right(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_rotate_right.jpg -r -90'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_rotate_right.jpg"\n' \
               + 'Rotate(-90deg) filter\n', result.output

    def test_saturate_high(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_saturate_high.jpg -s 3'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_saturate_high.jpg"\n' \
               + 'Saturate(3) filter\n', result.output

    def test_saturate_low(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_saturate_low.jpg -s 0.5'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_saturate_low.jpg"\n' \
               + 'Saturate(0.5) filter\n', result.output

    def test_smooth(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_smooth.jpg -f smooth'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_smooth.jpg"\n' \
               + 'Smooth filter\n', result.output

    def test_smooth_more(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_smooth_more.jpg -f smooth_more'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_smooth_more.jpg"\n' \
               + 'Smooth_More filter\n', result.output

    def test_sharpen(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_sharpen.jpg -f sharpen'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_sharpen.jpg"\n' \
               + 'Sharpen filter\n', result.output

    def test_smooth_more(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_smooth_more.jpg -f smooth_more'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_smooth_more.jpg"\n' \
               + 'Smooth_More filter\n', result.output

    # Leave filters blank
    def test_no_filters(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_no_filters.jpg'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_no_filters.jpg"\n', result.output

    # Leave image arguments blank
    def test_img_defaults(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            ''.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "new.jpg"\n', result.output

    # Change save file type from jpg to png
    def test_savefile_type(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_savefile_type.png'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_savefile_type.png"\n', result.output

    # Multiple filters tests
    def test_grayscale_overlay(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_grayscale_overlay.jpg -f grayscale -o python.png 0 60'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_grayscale_overlay.jpg"\n' \
                                'Grayscale filter\nOverlay filter\n', result.output

    def test_overlay_x_16(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters,
            'input.jpg test_overlay_x_16.jpg \
            -o python.png 0 60 -o python.png 240 60 -o python.png 480 60 -o python.png 720 60 \
            -o python.png 0 220 -o python.png 240 220 -o python.png 480 220 -o python.png 720 220 \
            -o python.png 0 480 -o python.png 240 480 -o python.png 480 480 -o python.png 720 480 \
            -o python.png 0 740 -o python.png 240 740 -o python.png 480 740 -o python.png 720 740'.split())
        assert result.output == 'Filters added to "input.jpg" and re-saved as "test_overlay_x_16.jpg"\n' \
                                'Overlay filter\nOverlay filter\nOverlay filter\nOverlay filter\n' \
                                'Overlay filter\nOverlay filter\nOverlay filter\nOverlay filter\n' \
                                'Overlay filter\nOverlay filter\nOverlay filter\nOverlay filter\n' \
                                'Overlay filter\nOverlay filter\nOverlay filter\nOverlay filter\n', result.output

    def test_saturate_blur_mirror_edge_enhance_overlay(self):
        runner = CliRunner()
        result = runner.invoke(
            add_filters, 'input.jpg test_saturate_blur_mirror_edge_enhance_overlay.jpg -s 10.5 -f blur -f mirror \
            -f edge_enhance -o python.png 0 30'.split())
        assert result.output == \
               'Filters added to "input.jpg" and re-saved as "test_saturate_blur_mirror_edge_enhance_overlay.jpg"\n' \
               'Saturate(10.5) filter\nBlur filter\nMirror filter\nEdge_Enhance filter\nOverlay filter\n', result.output


if __name__ == '__main__':
    unittest.main()
