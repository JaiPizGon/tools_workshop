"""Tests for exercise 4."""

from src.exercise04_mse import mean_squared_error


def test_mean_squared_error_matches_known_result() -> None:
    """Verifies MSE for a small deterministic example."""
    predictions: list[float] = [1.0, 2.0, 3.0]
    targets: list[float] = [1.0, 0.0, 5.0]

    result: float = mean_squared_error(predictions, targets)

    assert abs(result - (8.0 / 3.0)) < 1e-12
