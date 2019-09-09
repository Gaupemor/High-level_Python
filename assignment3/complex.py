#!/usr/bin/env python

""" Contains the class 'Complex'.
"""

import math

class Complex:
    """ A Complex object represents a complex number.

    Attributes:
        real (int || float): Represents the real number.
        imag (int || float): Represents the imaginary number.
    """

    def __init__(self, r, i):
        self.real = r
        self.imag = i

    # Assignment 3.3

    def conjugate(self):
        """ Calculates the conjugate of the complex number.

        Returns:
            int || float: The conjugate of the Complex object that called the method.

        Example:
            >>> Complex(3, 2).conjugate()
            1
        """
        return self.real - self.imag

    def modulus(self):
        """ Calculates the modulus of the complex number.

        Returns:
            int || float: The modulus of the Complex object that called the method.

        Example:
            >>> Complex(3, 4).modulus()
            5
        """
        return math.sqrt((self.real)**2 + (self.imag)**2)

    def __add__(self, other):
        """ Adds the complex number with another complex or real number.

        Args:
            other (Complex || complex || int || float): Second addend of the addition.

        Returns:
            Complex: Sum of the addition.

        Examples:
            >>> print(Complex(1, 1) + Complex(1, 1))
            2 + 2i
            >>> print(Complex(1, 1) + 1)
            2 + i

        """
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.real + other, self.imag)
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """ Subtracts a complex or real number from the complex number.

        Args:
            other(Complex || complex || int || float): Subtrahend of the subtraction.

        Returns:
            Complex: Difference of the subtraction.

        Examples:
            >>> print(Complex(2, 2) - Complex(1, 1))
            1 + i
            >>> print(Complex (2, 2) - 1)
            1 + 2i
        """
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.real - other, self.imag)
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """ Multiplies a complex or real number with the complex number.

        Args:
            other(Complex || complex || int || float): Multiplier of the multiplication.

        Returns:
            Complex: Product of the multiplication.

        Examples:
            >>> print(Complex(2, 2) * Complex(1, 2))
            2 + 4i
            >>> print(Complex (2, 2) * 2)
            4 + 2i
        """
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.real * other, self.imag)
        return Complex(self.real * other.real, self.imag * other.imag)

    def __eq__(self, other):
        """ Compare the complex number to a another complex or real number.

        Args:
            other(Complex || complex || int || float ): Second expression to compare the complex number to.

        Returns:
            bool: True if the values of the complex numbers are equal, False otherwise.

        Example:
            >>> Complex(2, 2) == Complex(2, 2)
            True
            >>> Complex(2, 2) == Complex(1, 1)
            False
            >>> Complex(4, 0) == 4
            True
        """
        if isinstance(other, int) or isinstance(other, float):
            if self.imag == 0 and self.real == other:
                return True
            return False
        if self.real == other.real and self.imag == other.imag:
            return True
        return False

    # Assignment 3.4

    def __radd__(self, other):
        """ Handles addition if a non Complex object calls __add__ on a Complex object.

        Args:
            other(int || float): The original number that tried to call __add__.

        Returns:
            Complex: Calls addition from the Complex object and returns the result.

        Example:
            >>> print(2 + Complex(2, 2))
            4 + 2i
        """
        return self + other

    def __rsub__(self, other):
        """ Handles subtraction if a non Complex object calls __sub__ on a Complex object.

        Args:
            other(int || float): The original number that tried to call __sub__.

        Returns:
            Complex: Calls subtraction from the Complex object and returns the result.

        Example:
            >>> print(1 - Complex(1, 1))
            -i
        """
        return -self + other

    def __rmul__(self, other):
        """ Handles multiplication if a non Complex object calls __mul__ on a Complex object.

        Args:
            other(int || float): The original number that tried to call __mul__.

        Returns:
            Complex: Calls multiplication from the Complex number and returns the result.

        Example:
            >>> print(2 * Complex(2, 2))
            4 + 2i
        """
        return self * other

    # Help methods

    def __neg__(self):
        """ Inverts the complex number.

        Returns:
            Complex: The inverted (negative) complex number. Inverts bothe the real and negative value.

        Example:
            >>> print(-Complex(2, 2))
            -2 - 2i
            >>> print(-Complex(-2, -2))
            2 + 2i
        """
        return Complex(-self.real, -self.imag)

    def __str__(self):
        """ Stringifies the complex number.

        Returns:
            string: The complex number strinigified on the format: [real number] +/- [imaginary number]i

        Example:
            >>> str(Complex(1, -1))
            '1 - i'
            >>> print(Complex(0, 2))
            2i
        """
        if self.imag == 0:
            return f"{self.real}"
        elif self.real == 0:
            if self.imag == 1:
                return "i"
            elif self.imag == -1:
                return "-i"
            return f"{self.imag}i"
        elif self.imag < 0:
            if self.imag == -1:
                return f"{self.real} - i"
            return f"{self.real} - {abs(self.imag)}i"
        else:
            if self.imag == 1:
                return f"{self.real} + i"
            return f"{self.real} + {self.imag}i"
