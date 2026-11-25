# Exercise 3: Generating Unit Tests with Agent Mode

[⬅️ Previous: Exercise 2](02-diagnosing-and-fixing-errors.md) | [Table of Contents](README.md) | [Next: Exercise 4 ➡️](04-custom-instructions.md)

---

## 🎯 Objective
Learn how to use **Agent mode** in the Local Harness to automatically create and write unit tests for the overdue fine calculator (`calculate_overdue_fine`) into a new test file.

---

## 📂 Target Files
- Source: `library-system/services/fine_calculator.py`
- Test file to create: `library-system/tests/test_fine_calculator.py`

---

## 📝 Step-by-Step Instructions

### 1. Open and inspect `fine_calculator.py`
Open `library-system/services/fine_calculator.py` in VS Code to see the `calculate_overdue_fine` method implemented in Exercise 1.

### 2. Open Copilot Chat and switch to Local Harness & Agent Mode

1. Open the GitHub Copilot Chat panel in VS Code (<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> / <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>).

2. Set the dropdown to **Local**.

3. Switch the mode dropdown from **Ask** to **Agent**.
   > 💡 In **Agent mode**, Copilot can directly propose and create new files in your project workspace.

### 3. Ask Copilot to create the test file

In the Chat panel input box, enter the prompt:

```text

Create a new test file tests/test_fine_calculator.py with pytest unit tests for FineCalculator.calculate_overdue_fine in #file:services/fine_calculator.py:
- Test days_overdue <= 0 returns 0.0
- Test 5 days overdue returns 2.50
- Test 150 days overdue caps at 50.0
Use @pytest.mark.parametrize and a pytest fixture and don't do test run.

```

### 4. Review and Accept the New File

1. In Agent mode, Copilot will generate the tests and prompt you to create/apply the changes to `tests/test_fine_calculator.py`.
2. Click **Keep** / **Accept** to save `tests/test_fine_calculator.py`.

Example generated test structure:
```python
import pytest
from services.fine_calculator import FineCalculator

@pytest.fixture
def calculator():
    return FineCalculator()

def test_on_time_returns_zero(calculator):
    assert calculator.calculate_overdue_fine(0) == 0.0
    assert calculator.calculate_overdue_fine(-1) == 0.0

@pytest.mark.parametrize("days, expected_fine", [
    (5, 2.50),     # 5 * 0.50 = 2.50
    (10, 5.00),    # 10 * 0.50 = 5.00
    (150, 50.00),  # Capped at 50.00
])
def test_overdue_fine_calculation(calculator, days, expected_fine):
    assert calculator.calculate_overdue_fine(days) == expected_fine
```

### 5. Run the new test suite

In your terminal, execute:
```bash
pytest tests/test_fine_calculator.py -v
```

**Expected Result:**
All generated tests pass with green checkmarks!

---

## 💡 Key Takeaways
- Switching to **Agent mode** allows Copilot to autonomously create new test files and edit workspace files directly.
- Referencing `#file:services/fine_calculator.py` grounds Copilot in the exact business logic and constants (`BASE_DAILY_RATE`, `MAX_FINE`).
- Asking for `@pytest.mark.parametrize` produces clean, maintainable table-driven tests.

---

[⬅️ Previous: Exercise 2](02-diagnosing-and-fixing-errors.md) | [Table of Contents](README.md) | [Next: Exercise 4 ➡️](04-custom-instructions.md)
