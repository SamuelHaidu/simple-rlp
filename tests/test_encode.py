import unittest
from rlp import encode


__all__ = ['TestEncode']


class TestEncode(unittest.TestCase):

    def test_encode_single_byte(self):
        data = b'\x10'
        expected = b'\x10'
        actual = encode(data)
        self.assertEqual(expected, actual)

    def test_encode_small_byte_string(self):
        data = b'dog'
        expected = b'\x83dog'
        actual = encode(data)
        self.assertEqual(expected, actual)

    def test_encode_big_byte_string(self):
        data = b'A' * 1024
        expected = b'\xb9\x04\x00' + b'A' * 1024
        actual = encode(data)
        self.assertEqual(expected, actual)

    def test_encode_small_list(self):
        data = [b'dog', b'cat', [b'spy']]
        expected = b'\xcd\x83dog\x83cat\xc4\x83spy'
        actual = encode(data)
        self.assertEqual(expected, actual)

    def test_encode_big_list(self):
        data = [b'A' * 1024]
        expected = b'\xf9\x04\x03\xb9\x04\x00' + b'A' * 1024
        actual = encode(data)
        self.assertEqual(expected, actual)

    def test_encode_empty_list(self):
        data = []
        expected = b'\xc0'
        actual = encode(data)
        self.assertEqual(expected, actual)

    def test_encode_empty_byte_string(self):
        data = b''
        expected = b'\x80'
        actual = encode(data)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
