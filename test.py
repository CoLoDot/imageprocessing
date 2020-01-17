import unittest
from lena import read_lena

class TestImageProcessing(unittest.TestCase):
    """Test Image Processing"""

    def test_read_lena(self):
        self.assertEqual(read_lena(), (512, 512, 3))

if __name__ == '__main__':
    unittest.main()