import unittest
from io import StringIO
import sys
from Dec2Hex import decimal_to_hex

# Assuming the decimal_to_hex function is in the same file, if not, import it like this:
# from your_module import decimal_to_hex.

class TestDecimalToHex(unittest.TestCase):
    
    def test_valid_decimal(self):
        # Test with a valid decimal value.
        decimal_value = 255
        expected_output = "FF"
        
        # Capture the print output
        captured_output = StringIO()
        sys.stdout = captured_output
        decimal_to_hex(decimal_value)
        sys.stdout = sys.__stdout__  # Reset redirect.
        
        # Check if the output matches
        self.assertIn(f"Hexadecimal representation is: {expected_output}", captured_output.getvalue())
    
    def test_input_is_not_integer(self):
        # Test if the function raises TypeError for non-integer input
        with self.assertRaises(TypeError):
            decimal_to_hex("string")
    
    def test_decimal_less_than_one(self):
        # Test if the function handles a decimal value less than 1
        captured_output = StringIO()
        sys.stdout = captured_output
        decimal_to_hex(0)
        sys.stdout = sys.__stdout__  # Reset redirect.
        
        self.assertIn("Please provide Decimal value greater than 0", captured_output.getvalue())
    
    def test_valid_edge_case(self):
        # Test with another valid decimal value (e.g., 16)
        decimal_value = 16
        expected_output = "10"
        
        captured_output = StringIO()
        sys.stdout = captured_output
        decimal_to_hex(decimal_value)
        sys.stdout = sys.__stdout__  # Reset redirect.
        
        self.assertIn(f"Hexadecimal representation is: {expected_output}", captured_output.getvalue())
    
    def test_invalid_input(self):
        """Test when invalid input is provided (e.g., None or a string)."""
       
        with self.assertRaises(TypeError):
            decimal_to_hex(None)

        with self.assertRaises(TypeError):
            decimal_to_hex("string")


if __name__ == "__main__":
    unittest.main()
