## Simple RLP (Recursive Length Prefix)
#### Efficiently encode and decode data structures with minimal dependencies

This module provides an alternative to the official Ethereum [pyrlp](https://github.com/ethereum/pyrlp) library.

While pyrlp requires 5 dependencies, this alternative is written in pure Python and has no dependencies. It is recommended for projects that do not require the full suite of Ethereum tools. If your project already uses Ethereum tools, consider using [pyrlp](https://github.com/ethereum/pyrlp) instead.

#### Features:
 - Straightforward encoding and decoding of lists containing various data types
 - Fast encoding process
 - Automatic serialization of Python objects (refer to supported types below)
 - Templates for converting bytes into decoded objects
 - Dependency-free implementation

#### Installation:
```
pip install simple-rlp 
```

#### Usage:

##### Encoding:
```python
>>> import rlp
>>> my_list = ['python', 'rlp', 255]
>>> rlp.encode(my_list)
b'\xcd\x86python\x83rlp\x81\xff'
```
##### Decoding:
```python
>>> import rlp
>>> my_list_encoded = b'\xcd\x86python\x83rlp\x81\xff'
>>> rlp.decode(my_list_encoded)
[b'python', b'rlp', b'\xff']
```

Use templates to decode and convert bytes to Python objects

##### Supported Types:

 - Signed integer
 - Unsigned integer
 - Boolean
 - Float
 - String

```python
rlp.converters.UInteger # Unsigned integer
rlp.converters.SInteger # Signed integer
rlp.converters.Bool # Boolean
rlp.converters.Float # Float
rlp.converters.String # String
```
Both signed and unsigned integers use big-endian byte order by default. To use little-endian, modify the static attribute:

```python
LittleEndianUInt = rlp.converters.UInteger
LittleEndianUInt.byteorder =  'little'
```
String uses UTF-8 encoding by default. To use a different encoding, modify the static attribute:

```python
ASCIIString = rlp.converters.String
ASCIIString.encoding =  'ascii'
```

##### Template Usage:
```python
>>> from rlp.converters import *
>>> import rlp

>>> my_list = ['rlp', 1024, 3.14159, True, b'\x08']
>>> my_list_template = [String, UInteger, Float, Bool, None]
>>> my_list_encoded = rlp.encode(my_list)
>>> rlp.decode(my_list_encoded, template=my_list_template)
['rlp', 1024, 3.141590118408203, True, b'\x08']
```
Note: Use a `None` object in the template to leave the corresponding element unchanged.
