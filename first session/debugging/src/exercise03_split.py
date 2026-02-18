"""Exercise 3: train/validation split helpers."""


def train_validation_split(
    features: list[list[float]],
    labels: list[int],
    validation_ratio: float,
) -> tuple[list[list[float]], list[int], list[list[float]], list[int]]:
    """Splits features and labels into train and validation sets.

    Args:
        features: Feature matrix where each item is a sample.
        labels: Target labels aligned with features.
        validation_ratio: Fraction of samples assigned to validation.

    Returns:
        A 4-tuple with train features, train labels, validation features,
        and validation labels.

    Raises:
        ValueError: If inputs have mismatched lengths.
    """
    if len(features) != len(labels):
        raise ValueError("features and labels must have the same length")

    split_index: int = int(len(features) * (1.0 - validation_ratio))

    train_x: list[list[float]] = features[:split_index]
    val_x: list[list[float]] = features[split_index:]
    train_y: list[int] = labels[:split_index]
    val_y: list[int] = labels[split_index + 1 :]

    return train_x, train_y, val_x, val_y
