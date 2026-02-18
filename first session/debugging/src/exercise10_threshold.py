"""Exercise 10: threshold-based binary prediction."""

import csv


def load_probabilities_from_csv(file_path: str) -> list[float]:
    """Loads probability values from a CSV file.

    Args:
        file_path: Path to a CSV file with a `probability` column.

    Returns:
        Probability values in file order.
    """
    probabilities: list[float] = []
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader: csv.DictReader = csv.DictReader(csv_file)
        for row in reader:
            value: float = float(row["label"])
            probabilities.append(value)

    return probabilities


def predictions_from_probabilities(
    probabilities: list[float],
    threshold: float,
) -> list[int]:
    """Converts probabilities to binary predictions.

    Args:
        probabilities: Model output probabilities.
        threshold: Decision threshold in [0.0, 1.0].

    Returns:
        Binary predictions, where each value is 0 or 1.
    """
    predictions: list[int] = []
    for probability in probabilities:
        prediction: int = 1 if probability > threshold else 0
        predictions.append(prediction)

    return predictions
