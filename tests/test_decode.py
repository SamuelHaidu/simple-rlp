from rlp import decode


def test_decode(encoded_input: bytes, expected: any, test_name: str) -> None:
    encoded_input = decode(encoded_input)
    if encoded_input != expected:
        print(f'{test_name}: Fail')
        print(encoded_input)
    else:
        print(f'{test_name}: Pass')


if __name__ == '__main__':
    test_decode(b'\x10', b'\x10', 'decode single byte')
    test_decode(b'\x83dog', b'dog', 'decode small byte string')
    test_decode(b'\xb9\x04\x00' + b'A' * 1024, b'A' * 1024, 'decode big byte string')
    test_decode(b'\xcd\x83dog\x83cat\xc4\x83spy', [b'dog', b'cat', [b'spy']], 'decode small list')
    test_decode(b'\xf9\x04\x03\xb9\x04\x00' + b'A' * 1024, [b'A' * 1024], 'decode big list')
