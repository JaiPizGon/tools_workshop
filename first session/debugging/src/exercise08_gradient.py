"""Exercise 8: gradient descent parameter update."""


def gradient_descent_step(
    weights: list[float],
    gradients: list[float],
    learning_rate: float,
) -> list[float]:
    """Performs one gradient descent update step.

    Args:
        weights: Current model weights.
        gradients: Gradient for each weight.
        learning_rate: Positive step size.

    Returns:
        Updated weight vector.

    Raises:
        ValueError: If lengths do not match.
    """
    if len(weights) != len(gradients):
        raise ValueError("weights and gradients must have the same length")

    updated_weights: list[float] = []
    for weight, gradient in zip(weights, gradients):
        updated_weight: float = weight + learning_rate * gradient
        updated_weights.append(updated_weight)

    return updated_weights
