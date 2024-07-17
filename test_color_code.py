import unittest
from color_code import get_color_from_pair_number, get_pair_number_from_colors

class TestColorCode(unittest.TestCase):
    def test_get_color_from_pair_number(self):
        self.assertEqual(get_color_from_pair_number(1), ("White", "Blue"))
        self.assertEqual(get_color_from_pair_number(23), ("Violet", "Green"))
        with self.assertRaises(ValueError):
            get_color_from_pair_number(0)
        with self.assertRaises(ValueError):
            get_color_from_pair_number(26)
    
    def test_get_pair_number_from_colors(self):
        self.assertEqual(get_pair_number_from_colors("White", "Blue"), 1)
        self.assertEqual(get_pair_number_from_colors("Violet", "Green"), 23)
        with self.assertRaises(ValueError):
            get_pair_number_from_colors("Pink", "Blue")
        with self.assertRaises(ValueError):
            get_pair_number_from_colors("White", "Pink")

if __name__ == "__main__":
    unittest.main()
