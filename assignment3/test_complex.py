#!/usr/bin/env python

""" Test program for the class Complex from the module complex.

How to run:
    $ pytest test_complex.py

Note:
    Tests utilize the pytest library.
    Requires Python v. 3.6 or later to enable f-string formatting.

---

Methods included in testing:
    __init__    Implicitly tested
    __add__
    __radd__    Implicitly tested
    __sub__
    __rsub__    Implicitly tested
    __mul__
    __rmul__    Implicitly tested
    __neg__
    __eq__
    modulus
    conjugate
Methods excluded from testing:
    __str__     Does not calculate or evaluate complex numbers.


Naming conventions:
    The names  for these test methods describe the feature they test and the scenario they test.
    They do NOT describe the expected outcome of a test UNLESS the test is expected to fail.

        'test_feature'
            Describes the feature being tested.
            E.g. 'test_add', 'test_sub'

        'test_feature_expression_desc'
            Describes the expression the test asserts on the feature.

            For operands (with arguments)
            __add__(a + b), __sub__(a - b), __mul__(a + b)

                'test_feature_positive/negative_left/right'
                    Describes whether the expression to the left or right of the operand is all positive or all negative.
                    E.g. 'test_add_positive_left_negative_right'

                'test_feature_with_real_number_left/right'
                    Describes a test that tests the feature with a real number value,
                    and whether the real number is to the left or the right of the complex number.
                    (If to the left, the __r[feature]__ method is also tested.)
                    E.g. 'test_add_with_real_number_left'

                'test_feature_with_complex_number_left/right'
                    Describes a test that tests the feature with a built-in complex number in python,
                    and whether the python complex number is to the left or the right of the complex number.
                    (If to the left, the __r[feature]__ method is also tested.)
                    E.g. 'test_add_with_complex_number_right'

            For methods and operands without arguments
            modulus, conjugate, __neg__ (-a)

                'test_feature_positive/negative_real_positive/negative_imag'
                    Describes whether the real and imaginary numbers in the complex number are positive or negative.
                    E.g. 'test_modulus_negative_real_positive_imag'

            For comparison
            __eq__ (a == b)

                'test_eq_positive/negative/zero_real_positive/negative/zero_imag'
                    Describes whether the real and imaginary numbers in the complex number are positive, negative or zero.
                    E.g. 'test_eq_negative_real_positive_imag'

                'test_eq_with_real/complex_number_left/right_of_eq'
                    Describes a test where Complex is compared to an in-build python complex number or a real number,
                    and whether the python complex is to the left or right of the '==' operand.
                    E.g. 'test_eq_with_complex_number_left_of_eq'

        'test_feature_expression_desc_fail'
            Describes a test expected to fail.
            E.g. 'test_eq_positive_real_positive_imag_fail'
"""
import pytest
from complex import Complex

#__add__ (__radd__)

def test_add_positive_left_positive_right():
    assert Complex(1, 2) + Complex(2, 1) == Complex(3, 3)
def test_add_positive_left_negative_right():
    assert Complex(-5, -5) + Complex(4, 6) == Complex(-1, 1)
def test_add_negative_left_positive_right():
    assert Complex(5, 5) + Complex(-4, -6) == Complex(1, -1)
def test_add_with_real_number_right():
    assert Complex(1, 1) + 1 == Complex(2, 1)
def test_add_with_real_number_left():
    assert 1 + Complex(1, 1) == Complex(2, 1)
def test_add_with_complex_number_right():
    assert Complex(3, 2) + (3 + 2j) == Complex(6, 4)
def test_add_with_complex_number_left():
    assert (3 - 2j) + Complex(1, 1) == Complex(4, -1)

#__sub__ (__rsub__)

def test_sub_positive_left_positive_right():
    assert Complex(5, 5) - Complex(3, 2) == Complex(2, 3)
def test_sub_positive_left_negative_right():
    assert Complex(5, 5) - Complex(-4, -6) == Complex(9, 11)
def test_sub_negative_left_positive_right():
    assert Complex(5, 5) - Complex(4, 6) == Complex(1, -1)
def test_sub_with_real_number_right():
    assert Complex(1, 1) - 1 == Complex(0, 1)
def test_sub_with_real_number_left():
    assert 1 - Complex(1, 1) == Complex(0, -1)
def test_sub_with_complex_number_right():
    assert Complex(4, 2) - (2 + 4j) == Complex(2, -2)
def test_sub_with_complex_number_left():
    assert (5 - 3j) - Complex (2, 1) == Complex(3, -4)

#__mul__ (__rmul__)

def test_mul_positive_left_positive_right():
    assert Complex(2,2) * Complex(5, 2) == Complex(10, 4)
def test_mul_positive_left_negative_right():
    assert Complex (2, 2) * Complex (-1, -2) == Complex(-2, -4)
def test_mul_negative_left_postive_right():
    assert Complex(-1, -4) * Complex(5, 2) == Complex(-5, -8)
def test_mul_with_real_number_right():
    assert Complex(3, 2) * 3 == Complex(9, 2)
def test_mul_with_real_number_left():
    assert 3 * Complex(3, 2) == Complex(9, 2)
def test_mul_with_complex_number_right():
    assert Complex(2, 3) * (2 + 1j) == Complex(4, 3)
def test_mul_with_complex_number_left():
    assert (4 - 2j) * Complex(5, 6) == Complex(20, -12)

#conjugate

def test_conjugate_positive_real_positive_imag():
    assert Complex(3, 2).conjugate() == 1
def test_conjugate_positive_real_negative_imag():
    assert Complex(3, -2).conjugate() == 5
def test_conjugate_negative_real_positive_imag():
    assert Complex(-3, 2).conjugate() == -5
def test_conjugate_negative_real_negative_imag():
    assert Complex(-3, -2).conjugate() == -1

#modulus

def test_modulus_positive_real_positive_imag():
    assert Complex(3, 4).modulus() == 5
def test_modulus_positive_real_negative_imag():
    assert Complex(3, -4).modulus() == 5
def test_modulus_negative_real_positive_imag():
    assert Complex(-3, 4).modulus() == 5
def test_modulus_negative_real_negative_imag():
    assert Complex(-3, -4).modulus() == 5

#__eq__

def test_eq_positive_real_positive_imag():
    assert Complex(1, 1) == Complex(1, 1)
def test_eq_zero_real_zero_imag():
    assert Complex(0, 0) == Complex(0,0)
def test_eq_negative_real_negative_imag():
    assert Complex(-1, -1) == Complex(-1, -1)
def test_eq_with_complex_number_right_of_eq():
    assert Complex(2, 4) == (2 + 4j)
def test_eq_with_complex_number_left_of_eq():
    assert (2 -3j) == Complex(2, -3)
def test_eq_with_real_number_right_of_eq():
    assert Complex(4, 0) == 4
def test_eq_with_real_number_left_of_eq():
    assert -4 == Complex(-4, 0)
def test_eq_positive_real_positive_imag_fail():
    with pytest.raises(Exception):
        assert Complex(1, 1) == Complex(2, 2)
def test_eq_positive_left_of_eq_negative_right_of_eq_fail():
    with pytest.raises(Exception):
        assert Complex(1, 1) == Complex(-1 , -1)

#__neg__

def test_neg_positive_real_positive_imag():
    assert -Complex(2, 3) == Complex(-2, -3)
def test_neg_positive_real_negative_imag():
    assert -Complex(2, -3) == Complex(-2, 3)
def test_neg_negative_real_positive_imag():
    assert -Complex(-2, 3) == Complex(2, -3)
def test_neg_negative_real_negative_imag():
    assert -Complex(-2, -3) == Complex(2, 3)
