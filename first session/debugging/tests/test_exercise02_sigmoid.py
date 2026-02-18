"""Tests for exercise 2."""

import math

from src.exercise02_sigmoid import sigmoid


def test_sigmoid_matches_reference_value() -> None:
    """Compares sigmoid output against mathematical reference."""
    value: float = 2.0

    result: float = sigmoid(value)
    expected: float = 1.0 / (1.0 + math.exp(-value))

    assert abs(result - expected) < 1e-12
