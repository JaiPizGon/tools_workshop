"""Tests for exercise 8."""

from src.exercise08_gradient import gradient_descent_step


def test_gradient_descent_step_moves_against_gradient() -> None:
    """Ensures one update step applies gradient descent direction."""
    weights: list[float] = [1.0, -2.0]
    gradients: list[float] = [0.5, -1.5]

    result: list[float] = gradient_descent_step(
        weights=weights,
        gradients=gradients,
        learning_rate=0.1,
    )

    assert result == [0.95, -1.85]
