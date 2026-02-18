"""Tests for exercise 9."""

from src.exercise09_kfold import k_fold_indices


def test_k_fold_indices_cover_all_samples_in_validation() -> None:
    """Checks that validation indices cover every sample exactly once."""
    folds: list[tuple[list[int], list[int]]] = k_fold_indices(n_samples=8, n_folds=4)

    validation_pool: list[int] = []
    for _, validation_indices in folds:
        validation_pool.extend(validation_indices)

    assert sorted(validation_pool) == list(range(8))


def test_k_fold_train_and_validation_do_not_overlap() -> None:
    """Ensures no overlap between train and validation indices."""
    folds: list[tuple[list[int], list[int]]] = k_fold_indices(n_samples=8, n_folds=4)

    for train_indices, validation_indices in folds:
        assert set(train_indices).isdisjoint(set(validation_indices))
