"""Tests for exercise 6."""

from src.exercise06_confusion import confusion_matrix_binary


def test_confusion_matrix_binary_counts_are_correct() -> None:
    """Checks confusion matrix tuple for a fixed example."""
    y_true: list[int] = [1, 0, 1, 0, 1, 0]
    y_pred: list[int] = [1, 1, 0, 0, 1, 0]

    result: tuple[int, int, int, int] = confusion_matrix_binary(y_true, y_pred)

    assert result == (2, 1, 1, 2)
