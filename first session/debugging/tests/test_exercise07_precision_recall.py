"""Tests for exercise 7."""

from src.exercise07_precision_recall import precision_recall


def test_precision_and_recall_follow_definitions() -> None:
    """Verifies precision and recall for known counts."""
    precision, recall = precision_recall(true_positive=8, false_positive=2, false_negative=4)

    assert abs(precision - 0.8) < 1e-12
    assert abs(recall - (8.0 / 12.0)) < 1e-12
