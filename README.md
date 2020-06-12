## Simple RLP (Recursive Length Prefix)
#### Encode the and decode data structures simple and fast

This module is a alternative to official Ethereum [pyrlp](https://github.com/ethereum/pyrlp).

The pyrlp needs 5 dependencies. This alternative is write in
pure python and don't have any dependencies. Recommended use for 
projects that don't need the Ethereum tools. If you already uses
the Ethereum tools uses the [pyrlp](https://github.com/ethereum/pyrlp).

#### Features:  
 - Very simple usage to encode and decode lists of data  
 - Very fast to encode  
 - Auto serialize python objects (check supported types)
 - Templates to convert bytes in decoded objects
 - No dependencies

#### Installation:
```
pip install simple-rlp 
```
  
#### Usage:  

##### Encode:
```python
>>> import rlp
>>> my_list = ['python', 'rlp', 255]
>>> rlp.encode(my_list)
b'\xcd\x86python\x83rlp\x81\xff'
```
##### Decode:
```python
>>> import rlp
>>> my_list_encoded = b'\xcd\x86python\x83rlp\x81\xff'
>>> rlp.decode(my_list_encoded)
[b'python', b'rlp', b'\xff']
```

Use templates to decode and convert the bytes to python objects

##### Supported types:  

 - Signed integer  
 - Unsigned integer  
 - Bool  
 - Float  
 - String

```python
rlp.converters.UInteger # Signed integer
rlp.converters.SInteger # Unsigned integer
rlp.converters.Bool # Bool
rlp.converters.Float # Float
rlp.converters.String # String
```
Signed and unsigned integer uses by default big-endian order.
If you need to use little-endian edit the static attribute:

```python
LittleEndianUInt = rlp.converters.UInteger
LittleEndianUInt.byteorder =  'little'
```
String uses UTF-8 encoding by default if you need to use another then:
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
Note: Put None object to do nothing in template.
