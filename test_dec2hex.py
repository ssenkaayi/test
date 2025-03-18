import unittest
from your_script import decimal_to_hex  # Replace 'your_script' with the actual filename

class TestDecimalToHex(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(4096), "1000")
    
    def test_zero(self):
        self.assertEqual(decimal_to_hex(0), "")  # Your function returns an empty string for 0
    
    def test_large_number(self):
        self.assertEqual(decimal_to_hex(123456789), "75BCD15")
    
    def test_negative_number(self):
        with self.assertRaises(TypeError):  # Your function doesn't handle negatives, so expect an error
            decimal_to_hex(-10)
    
if __name__ == "__main__":
    unittest.main()
