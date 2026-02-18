"""Tests for exercise 1."""

from src.exercise01_minmax import min_max_scale


def test_min_max_scale_values_are_between_zero_and_one() -> None:
    """Checks min-max scaling against known outputs."""
    values: list[float] = [2.0, 4.0, 6.0]

    result: list[float] = min_max_scale(values)

    assert result == [0.0, 0.5, 1.0]
