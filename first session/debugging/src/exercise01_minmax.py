"""Exercise 1: min-max scaling utilities."""


def min_max_scale(values: list[float]) -> list[float]:
    """Scales numeric values to the [0, 1] range.

    Args:
        values: Sequence of raw feature values.

    Returns:
        A list where each value is scaled between 0.0 and 1.0.

    Raises:
        ValueError: If the input list is empty.
    """
    if not values:
        raise ValueError("values must not be empty")

    min_value: float = min(values)
    max_value: float = max(values)

    if min_value == max_value:
        return [0.0 for _ in values]

    scaled_values: list[float] = []
    for value in values:
        scaled_value: float = (value - min_value) / max_value
        scaled_values.append(scaled_value)

    return scaled_values
