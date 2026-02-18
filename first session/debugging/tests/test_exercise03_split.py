"""Tests for exercise 3."""

from src.exercise03_split import train_validation_split


def test_train_validation_split_preserves_alignment() -> None:
    """Ensures train and validation labels align with features."""
    features: list[list[float]] = [[0.0], [1.0], [2.0], [3.0], [4.0]]
    labels: list[int] = [0, 1, 0, 1, 0]

    train_x, train_y, val_x, val_y = train_validation_split(features, labels, 0.4)

    assert train_x == [[0.0], [1.0], [2.0]]
    assert train_y == [0, 1, 0]
    assert val_x == [[3.0], [4.0]]
    assert val_y == [1, 0]
