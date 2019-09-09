## README selmafs assignment3

All programs require Python v. 3.6+ to enable f-string formatting.

### wc.py
#### How to run
1) Source the file:
```bash
$ source wc.py
```
2) Run by calling:
```bash
$ wc [filename(s)]
```

More info about implementation and return format in the file docstring.

### test_complex.py
Tests utilize pytest.
Run tests by calling:
```bash
$ pytest test_complex.py
```

I did not write documentation for every test method, but in the module documentation for test_complex i explain how the names of the tests describe which feature (function) they test and which scenarios they test.

More info about tests in the file docstring.

### complex.py
- Both my implementation of complex numbers and the in-build implementation of complex numbers in python use the instance variables called `real` and `imag` for real and imaginary numbers, so there was no need to implement `__complex__` with the way I implemented the class.
- Did not write documentation for `__init__` - thought the class documentation was sufficient. The class documentation describe the attributes, and the constructor only assigns value to the instance variables.


More info about implementation of Complex in the file/class/methods docstring.
