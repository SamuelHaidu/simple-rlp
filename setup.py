from setuptools import setup

with open('README.md', 'r') as readme_file:
    README = readme_file.read()

setup(
    name='simple-rlp',
    version='0.1.2',
    packages=['rlp'],
    url='https://github.com/SamuelHaidu/simple-rlp',
    license='MIT Custom',
    author='Samuel Haidu',
    author_email='samuelhaidu3@gmail.com',
    description='RLP (Recursive Length Prefix) - Encode and decode data structures',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6'
)
