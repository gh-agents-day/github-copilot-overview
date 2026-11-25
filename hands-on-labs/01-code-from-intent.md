# Exercise 1: Code Generation from Intent & Code Explanation

[⬅️ Previous: Exercise 0](00-setup-and-clone.md) | [Table of Contents](README.md) | [Next: Exercise 2 ➡️](02-diagnosing-and-fixing-errors.md)

---

## 🎯 Objective
Learn how to implement the overdue fine calculation feature (`calculate_overdue_fine`) using Copilot Chat in Ask mode with the Local Harness, and use `/explain` to inspect the book checkout workflow (`borrow_book`) and spot inventory copy leak hazards.

---

## 📂 Target Files
- `library-system/services/fine_calculator.py`
- `library-system/services/loan_service.py`

---

## 📝 Part A: Code Generation from Intent

### Step 1: Open Copilot Chat Panel
Open the Copilot Chat panel:
- **Windows / Linux:** `Ctrl + Alt + I`
- **macOS:** `Cmd + Shift + I`
- Or click the **GitHub Copilot Chat** icon in the VS Code Activity Bar (left sidebar).

---

### Step 2: Switch to Local Harness & Select "Ask" Mode
1. In the Copilot Chat input box, first **select the Local Harness**.
2. Once the Local Harness is selected, locate the mode selector dropdown and select **Ask** mode.

---

### Step 3: Provide a Simple Intent Prompt with File Reference
In the chat prompt input box, use `#file:` to point to the file and enter this simple prompt:

```text
#file:services/fine_calculator.py
Add a method `calculate_overdue_fine(self, days_overdue: int) -> float`:
- If days_overdue <= 0, return 0.0
- Otherwise, return days_overdue * self.BASE_DAILY_RATE (capped at self.MAX_FINE)
```

---

### Step 4: Insert the Generated Code into `fine_calculator.py`
1. Open `library-system/services/fine_calculator.py` in your editor.
2. Place your cursor on a blank line inside the `FineCalculator` class (after line 7).
3. In the Copilot Chat response:
   - Hover over the generated code block.
   - Click the **Apply in Editor** icon (or **Insert at Cursor** icon).
   - Alternatively, copy the generated method and paste it into `fine_calculator.py`.
4. Save the file (`Ctrl + S` / `Cmd + S`).

Example of what Copilot generates:
```python
    def calculate_overdue_fine(self, days_overdue: int) -> float:
        if days_overdue <= 0:
            return 0.0
        return min(days_overdue * self.BASE_DAILY_RATE, self.MAX_FINE)
```

---

### Step 5 (Optional): Try the Same Prompt with Inline Chat (`Ctrl + I`)
To test the in-editor shortcut:

1. In `services/fine_calculator.py`, place your cursor on a new line inside `FineCalculator`.
2. Press **`Ctrl + I`** (Windows/Linux) or **`Cmd + I`** (macOS).
3. Paste the same simple prompt:
   ```text
   Add method calculate_overdue_fine(self, days_overdue: int) -> float:
   return 0.0 if days_overdue <= 0 else min(days_overdue * self.BASE_DAILY_RATE, self.MAX_FINE)
   ```
4. Press Enter, review the inline diff, and click **Accept** (`Ctrl + Enter`).

---

## 📝 Part B: Code Explanation with `/explain`

### Step 6: Open `loan_service.py` & Highlight `borrow_book`

1. Open `library-system/services/loan_service.py` in VS Code.

2. Highlight/ select the `borrow_book` method (around lines 38 to 85).

---

### Step 7: Submit the `/explain` Command in Copilot Chat
In the Copilot Chat prompt input, type:

```text

/explain

Explain how catalog reservation, membership borrowing quota validation, loan period calculation, and notification dispatch are coordinated here.
Specifically point out:
What happens to the catalog book copy if membership.register_loan fails due to borrow quota limit or unpaid fines?
```

---

### Step 8: Analyze the Explanation
Read Copilot's response carefully:
- **Inventory Copy Leak:** Copilot will spot that `self.catalog.decrement_copy(isbn)` decrements the available copy count in Step 1, but if `self.membership.register_loan(member_id)` returns `False` in Step 2, a `RuntimeError` is raised *without* calling `self.catalog.increment_copy(isbn)` to roll back the reserved copy!
- Keep this finding in mind — you will fix this exact bug in **Exercise 2**!

---

## 💡 Key Takeaways
- Using (Local Harness) in **Ask** mode gives Copilot project-wide awareness while letting you specify precise target files with `#file:`.
- Inline Chat (`Ctrl + I`) allows quick modifications without leaving the editor canvas.
- `/explain` acts as a second pair of eyes during code reviews, spotting edge-case state leaks and missing rollbacks before they hit production.

---

[⬅️ Previous: Exercise 0](00-setup-and-clone.md) | [Table of Contents](README.md) | [Next: Exercise 2 ➡️](02-diagnosing-and-fixing-errors.md)
