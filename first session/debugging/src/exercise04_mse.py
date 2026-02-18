"""Exercise 4: regression metric helpers."""


def mean_squared_error(predictions: list[float], targets: list[float]) -> float:
    """Computes the mean squared error between predictions and targets.

    Args:
        predictions: Model predictions.
        targets: Ground-truth values.

    Returns:
        Mean squared error value.

    Raises:
        ValueError: If list lengths do not match.
    """
    if len(predictions) != len(targets):
        raise ValueError("predictions and targets must have the same length")

    if not predictions:
        raise ValueError("predictions must not be empty")

    total_error: float = 0.0
    for prediction, target in zip(predictions, targets):
        error: float = prediction - target
        total_error += abs(error)

    return total_error / len(predictions)
