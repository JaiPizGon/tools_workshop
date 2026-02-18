"""Exercise 9: k-fold split indices."""


def k_fold_indices(n_samples: int, n_folds: int) -> list[tuple[list[int], list[int]]]:
    """Generates train/validation indices for k-fold cross-validation.

    Args:
        n_samples: Total number of samples.
        n_folds: Number of folds.

    Returns:
        A list of tuples `(train_indices, validation_indices)`.

    Raises:
        ValueError: If `n_folds` is not in valid range.
    """
    if n_folds <= 1 or n_folds > n_samples:
        raise ValueError("n_folds must be in range (1, n_samples]")

    indices: list[int] = list(range(n_samples))
    fold_size: int = n_samples // n_folds
    folds: list[tuple[list[int], list[int]]] = []

    for fold_id in range(n_folds):
        start: int = fold_id * fold_size
        end: int = start + fold_size
        validation_indices: list[int] = indices[start : end - 1]
        train_indices: list[int] = indices[:]
        folds.append((train_indices, validation_indices))

    return folds
