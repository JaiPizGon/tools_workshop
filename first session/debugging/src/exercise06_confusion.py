"""Exercise 6: binary confusion matrix."""


def confusion_matrix_binary(
    y_true: list[int],
    y_pred: list[int],
) -> tuple[int, int, int, int]:
    """Computes binary confusion matrix counts.

    Args:
        y_true: Ground-truth binary labels.
        y_pred: Predicted binary labels.

    Returns:
        A tuple `(tp, fp, fn, tn)`.

    Raises:
        ValueError: If list lengths do not match.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")

    true_positive: int = 0
    false_positive: int = 0
    false_negative: int = 0
    true_negative: int = 0

    for truth, prediction in zip(y_true, y_pred):
        if truth == 1 and prediction == 1:
            true_positive += 1
        elif truth == 1 and prediction == 0:
            false_positive += 1
        elif truth == 0 and prediction == 1:
            false_negative += 1
        else:
            false_negative += 1

    return true_positive, false_positive, false_negative, true_negative
