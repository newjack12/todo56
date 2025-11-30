"""
Calculator module
=================

This module provides basic arithmetic operations with logging.
Each function includes parameter descriptions, return values,
and possible raised exceptions.

Functions:
    add(a, b)
    subtract(a, b)
    multiply(a, b)
    divide(a, b)
"""

from app.logger import logger


def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : int or float
        The first operand.
    b : int or float
        The second operand.

    Returns
    -------
    int or float
        The sum of a and b.

    Examples
    --------
    >>> add(3, 5)
    8
    """
    logger.info(f"Adding {a} + {b}")
    return a + b


def subtract(a, b):
    """
    Subtract b from a.

    Parameters
    ----------
    a : int or float
        The number from which b is subtracted.
    b : int or float
        The number to subtract.

    Returns
    -------
    int or float
        The result of a - b.

    Examples
    --------
    >>> subtract(10, 3)
    7
    """
    logger.info(f"Subtracting {a} - {b}")
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : int or float
        First operand.
    b : int or float
        Second operand.

    Returns
    -------
    int or float
        The product of a and b.

    Examples
    --------
    >>> multiply(4, 6)
    24
    """
    logger.info(f"Multiplying {a} * {b}")
    return a * b


def divide(a, b):
    """
    Divide a by b.

    Parameters
    ----------
    a : int or float
        The numerator.
    b : int or float
        The denominator.

    Returns
    -------
    float
        The result of a / b.

    Raises
    ------
    ValueError
        If b is zero, since division by zero is not allowed.

    Examples
    --------
    >>> divide(10, 2)
    5.0
    """
    if b == 0:
        logger.error("Attempt to divide by zero")
        raise ValueError("Cannot divide by zero")

    logger.info(f"Dividing {a} / {b}")
    return a / b
