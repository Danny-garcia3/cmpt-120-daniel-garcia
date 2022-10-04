from pickletools import pybytes_or_str
from hello import hello

def test_hello():
    assert hello() == "Hello, world!"
