from pathlib import Path
import os.path


BASE_DIR = Path(__file__).resolve().parent.parent

img_path = os.path.join(BASE_DIR, 'src')

original = os.path.join(img_path, 'original')

filter_choices = [
    'blur',
    'contour',
    'detail',
    'edge_enhance',
    'edge_enhance_more',
    'emboss',
    'find_edges',
    'smooth',
    'smooth_more',
    'sharpen',
    'grayscale',
    'flip',
    'mirror',
]
