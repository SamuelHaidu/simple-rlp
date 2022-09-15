import unittest
from rlp.rlp import convert_to_bytes

class TestConvertToBytes(unittest.TestCase):
    
        def test_convert_to_bytes_string(self):
            input_object = 'test'
            expected = b'test'
            actual = convert_to_bytes(input_object)
            self.assertEqual(expected, actual)
    
        def test_convert_to_bytes_bool(self):
            input_object = True
            expected = b'\x01'
            actual = convert_to_bytes(input_object)
            self.assertEqual(expected, actual)
    
        def test_convert_to_bytes_int(self):
            input_object = 255
            expected = b'\x00\xff'
            actual = convert_to_bytes(input_object)
            self.assertEqual(expected, actual)
    
        def test_convert_to_bytes_negative_int(self):
            input_object = -127
            expected = b'\xff\x81'
            actual = convert_to_bytes(input_object)
            self.assertEqual(expected, actual)
    
        def test_convert_to_bytes_float(self):
            input_object = 3.14159
            expected = b'\xd0\x0fI@'
            actual = convert_to_bytes(input_object)
            self.assertEqual(expected, actual)
    
        def test_convert_to_bytes_bytes(self):
            input_object = b'\x01\x02\x03'
            expected = b'\x01\x02\x03'
            actual = convert_to_bytes(input_object)
            self.assertEqual(expected, actual)