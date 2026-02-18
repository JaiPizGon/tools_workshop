"""Exercise 2: sigmoid activation."""

import math


def sigmoid(value: float) -> float:
    """Computes the sigmoid activation of a scalar value.

    Args:
        value: Input scalar.

    Returns:
        Sigmoid-transformed value in the range (0, 1).
    """
    return 1.0 / (1.0 + math.exp(value))
