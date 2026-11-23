# Exercise 2: Diagnosing & Fixing Errors with `/fix`

[⬅️ Previous: Exercise 1](01-code-from-intent.md) | [Table of Contents](README.md) | [Next: Exercise 3 ➡️](03-generating-unit-tests.md)

---

## 🎯 Objective
Learn how to fix a failing test using `/fix` by implementing book copy rollback logic when member checkout validation fails in `borrow_book`.

---

## 📂 Target Files
- `library-system/services/loan_service.py`
- `library-system/tests/test_loan_service.py`

---

## 📝 Step-by-Step Instructions

### 1. Run the test suite to observe the failure
Open your terminal in `library-system/` and run:
```bash
pytest
```

**Observed Output:**
```text
FAILED tests/test_loan_service.py::test_borrow_fails_restores_book_copy
AssertionError: Book copy leak! Expected 2 copies, but catalog has 1
```
*Notice: Because borrowing validation failed (member had unpaid fines), the decremented book copy was never released back into the catalog!*

### 2. Highlight the failing logic
In `library-system/services/loan_service.py`, highlight the membership validation block inside `borrow_book`:
```python
        # Validate member quota and fine standing
        if not self.membership.register_loan(member_id):
            raise RuntimeError(
                f"Member '{member.name}' has exceeded borrow quota ({member.active_loans_count}/{member.max_borrow_limit}) or has outstanding fines."
            )
```

### 3. Open Inline Chat (`Ctrl + I` / `Cmd + I`)
With the code highlighted, press `Ctrl + I` (or `Cmd + I`) and type:

```text
/fix
When membership.register_loan(member_id) is False:
1. Release the reserved book copy back to the catalog using self.catalog.increment_copy(isbn).
2. Then raise the RuntimeError.
```

### 4. Review and Accept the diff
Copilot will propose calling `self.catalog.increment_copy(isbn)` before raising the exception.  
Click **Accept** (`Tab` or Enter).

### 5. Verify the fix
In your terminal, re-run `pytest`:
```bash
pytest
```

**Expected Result:**
All tests now pass! The catalog book copy leak has been resolved.

---

## 💡 Key Takeaways
- `/fix` can be triggered from either the Chat panel or Inline Chat (`Ctrl + I`).
- Combining a failing test output with `/fix` gives the model the exact assertion criteria it needs to generate a 100% accurate fix.

---

[⬅️ Previous: Exercise 1](01-code-from-intent.md) | [Table of Contents](README.md) | [Next: Exercise 3 ➡️](03-generating-unit-tests.md)
