from rlp import encode


def test_encode(decoded_input: any, expected: bytes, test_name: str) -> None:
    encoded_input = encode(decoded_input)
    if encoded_input != expected:
        print(f'{test_name}: Fail')
        print(encoded_input)
    else:
        print(f'{test_name}: Pass')


if __name__ == '__main__':
    test_encode(b'\x10', b'\x10', 'encode single byte')
    test_encode(b'dog', b'\x83dog', 'encode small byte string')
    test_encode(b'A'*1024, b'\xb9\x04\x00'+b'A'*1024, 'encode big byte string')
    test_encode([b'dog', b'cat', [b'spy']], b'\xcd\x83dog\x83cat\xc4\x83spy', 'encode small list')
    test_encode([b'A'*1024], b'\xf9\x04\x03\xb9\x04\x00'+b'A'*1024, 'encode big list')
