import unittest
from rlp import decode

__all__ = ['TestDecode']


class TestDecode(unittest.TestCase):

    def test_decode_single_byte(self):
        data = b'\x10'
        expected = b'\x10'
        actual = decode(data)
        self.assertEqual(expected, actual)

    def test_decode_small_byte_string(self):
        data = b'\x83dog'
        expected = b'dog'
        actual = decode(data)
        self.assertEqual(expected, actual)

    def test_decode_big_byte_string(self):
        data = b'\xb9\x04\x00' + b'A' * 1024
        expected = b'A' * 1024
        actual = decode(data)
        self.assertEqual(expected, actual)

    def test_decode_small_list(self):
        data = b'\xcd\x83dog\x83cat\xc4\x83spy'
        expected = [b'dog', b'cat', [b'spy']]
        actual = decode(data)
        self.assertEqual(expected, actual)

    def test_decode_big_list(self):
        data = b'\xf9\x04\x03\xb9\x04\x00' + b'A' * 1024
        expected = [b'A' * 1024]
        actual = decode(data)
        self.assertEqual(expected, actual)

    def test_decode_empty_list(self):
        data = b'\xc0'
        expected = []
        actual = decode(data)
        self.assertEqual(expected, actual)

    def test_decode_empty_byte_string(self):
        data = b'\x80'
        expected = b''
        actual = decode(data)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
