"""Exercise 7: precision/recall metrics."""


def precision_recall(
    true_positive: int,
    false_positive: int,
    false_negative: int,
) -> tuple[float, float]:
    """Calculates precision and recall from confusion matrix counts.

    Args:
        true_positive: Number of true positives.
        false_positive: Number of false positives.
        false_negative: Number of false negatives.

    Returns:
        A tuple `(precision, recall)`.
    """
    precision_denominator: int = true_positive + false_negative
    recall_denominator: int = true_positive + false_negative

    precision: float = 0.0
    if precision_denominator > 0:
        precision = true_positive / precision_denominator

    recall: float = 0.0
    if recall_denominator > 0:
        recall = true_positive / recall_denominator

    return precision, recall
