"""Exercise 5: feature standardization."""


def standardize_feature(values: list[float]) -> list[float]:
    """Standardizes a feature column to zero mean and unit variance.

    Args:
        values: Raw values of one feature.

    Returns:
        Standardized values.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")

    mean_value: float = sum(values) / len(values)
    variance: float = sum((value - mean_value) ** 2 for value in values) / len(values)

    if variance == 0.0:
        return [0.0 for _ in values]

    standardized: list[float] = []
    for value in values:
        standardized_value: float = (value - mean_value) / variance
        standardized.append(standardized_value)

    return standardized
