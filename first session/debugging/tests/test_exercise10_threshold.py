"""Tests for exercise 10."""

from pathlib import Path

from src.exercise10_threshold import (
    load_probabilities_from_csv,
    predictions_from_probabilities,
)


def test_load_probabilities_from_csv_reads_probability_column() -> None:
    """Checks that probability values are loaded from the CSV file."""
    data_file: Path = (
        Path(__file__).resolve().parents[1] / "data" / "model_scores.csv"
    )

    probabilities: list[float] = load_probabilities_from_csv(str(data_file))

    assert probabilities == [0.92, 0.81, 0.5, 0.4, 0.15, 0.65]


def test_predictions_from_probabilities_include_threshold_value() -> None:
    """Verifies threshold comparison behavior for boundary values."""
    probabilities: list[float] = [0.49, 0.5, 0.51]

    predictions: list[int] = predictions_from_probabilities(probabilities, threshold=0.5)

    assert predictions == [0, 1, 1]
