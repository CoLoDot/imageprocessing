import unittest
from lena import LenaIP

class TestImageProcessing(unittest.TestCase):
    """Test Image Processing"""

    def test_read_lena(self):
        lena = LenaIP()
        self.assertEqual(lena.read_lena(), (512, 512, 3))

    def test_convert_lena_to_grayscale(self):
        lena = LenaIP()
        self.assertEqual(lena.convert_lena_to_grayscale(), [(512, 512), 162])

    def test_grayscale_lena_saving(self):
        lena = LenaIP()
        self.assertEqual(lena.save_lena_grayscale(), 1)

if __name__ == '__main__':
    unittest.main()