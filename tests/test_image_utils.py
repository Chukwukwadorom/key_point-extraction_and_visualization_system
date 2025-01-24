import pytest
from utils.image_utils import load_image


def test_load_image_valid_path():
    img = load_image("static/raw_images/pose1.jpeg")
    assert img is not None

def test_load_image_invalid_path():
    with pytest.raises(ValueError):
        load_image("nonexistent_path.jpeg")
