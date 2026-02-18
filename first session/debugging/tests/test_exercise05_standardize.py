"""Tests for exercise 5."""

from src.exercise05_standardize import standardize_feature


def test_standardized_values_have_unit_variance() -> None:
    """Checks a known standardized output pattern."""
    values: list[float] = [1.0, 2.0, 3.0]

    result: list[float] = standardize_feature(values)

    expected: list[float] = [-1.224744871391589, 0.0, 1.224744871391589]
    for actual, exp in zip(result, expected):
        assert abs(actual - exp) < 1e-12
