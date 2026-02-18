# Debugging Workshop: Machine Learning and Deep Learning

This repository contains **10 debugging exercises** for teaching purposes.

- These exercises are **not graded**.
- Students should debug using:
  - `pytest` test files
  - direct debugging from Python source files
  - notebook debugging with code that calls functions from `src`

## Repository Structure

- `data/`: small datasets used by exercises
- `src/`: buggy ML/DL utility functions
- `tests/`: pytest files for test-driven debugging
- `notebook/`: notebook-based debugging exercise

## Setup

1. Open this folder in VS Code.
2. Create and activate a Python environment.
3. Install pytest:

```bash
pip install pytest
```

4. Run all tests:

```bash
pytest -q
```

## How Students Should Work

### A) Debug from tests (`pytest`)

1. Run a specific test file (for example):

```bash
pytest -q tests/test_exercise01_minmax.py
```

2. Open the test and set breakpoints.
3. Start debugging the test in VS Code.
4. Step into the called function in `src`.
5. Verify variable values and fix logic to satisfy the function contract.

### B) Debug directly from Python source

1. Open a file in `src`.
2. Add a temporary `if __name__ == "__main__":` block if needed.
3. Call the function with representative values.
4. Run and debug that Python file directly.
5. Inspect variables and control flow to validate behavior.

### C) Debug from notebook

1. Open `notebook/debug_notebook_exercise.ipynb`.
2. Run cells in order.
3. Set breakpoints in notebook code and in the imported file under `src`.
4. Step from notebook cell execution into the Python function implementation.

## Exercise List

Each exercise has one function in `src` and one test file in `tests`.

1. **Exercise 1**
   - File: `src/exercise01_minmax.py`
   - Test: `tests/test_exercise01_minmax.py`
   - Goal: Implement min-max scaling so outputs are correctly mapped to the range `[0, 1]`.

2. **Exercise 2**
   - File: `src/exercise02_sigmoid.py`
   - Test: `tests/test_exercise02_sigmoid.py`
   - Goal: Compute the sigmoid activation for a scalar input according to its standard mathematical definition.

3. **Exercise 3**
   - File: `src/exercise03_split.py`
   - Test: `tests/test_exercise03_split.py`
   - Goal: Split features and labels into training and validation sets while preserving data alignment.

4. **Exercise 4**
   - File: `src/exercise04_mse.py`
   - Test: `tests/test_exercise04_mse.py`
   - Goal: Compute mean squared error between predictions and targets.

5. **Exercise 5**
   - File: `src/exercise05_standardize.py`
   - Test: `tests/test_exercise05_standardize.py`
   - Goal: Standardize a feature to zero mean and unit variance.

6. **Exercise 6**
   - File: `src/exercise06_confusion.py`
   - Test: `tests/test_exercise06_confusion.py`
   - Goal: Compute binary confusion matrix counts in the order `(tp, fp, fn, tn)`.

7. **Exercise 7**
   - File: `src/exercise07_precision_recall.py`
   - Test: `tests/test_exercise07_precision_recall.py`
   - Goal: Compute precision and recall from confusion matrix counts using standard formulas.

8. **Exercise 8**
   - File: `src/exercise08_gradient.py`
   - Test: `tests/test_exercise08_gradient.py`
   - Goal: Apply one gradient descent update step to model weights.

9. **Exercise 9**
   - File: `src/exercise09_kfold.py`
   - Test: `tests/test_exercise09_kfold.py`
   - Goal: Build k-fold train/validation index splits with proper coverage and no overlap.

10. **Exercise 10**
    - File: `src/exercise10_threshold.py`
    - Test: `tests/test_exercise10_threshold.py`
    - Notebook: `notebook/debug_notebook_exercise.ipynb`
    - Goal: Load probability values from CSV and convert them to binary predictions using a threshold rule.

## Teaching Notes

- All `src` functions include type hints and Google-style docstrings.
- Use these tasks to practice reading test expectations, tracing execution, and validating behavior.
- Encourage students to run one test file at a time while debugging.
