# Exercise 7: Exploring Copilot Agent Types (Local, Copilot SDK, Cloud)

[⬅️ Previous: Exercise 6](06-github-mcp-server.md) | [Table of Contents](README.md) | [Next: Exercise 8 ➡️](08-dotnet-modernization.md)

---

## 🎯 Objective
Learn how to use **Copilot (SDK)** to implement the Loan Renewal feature using the GitHub issue link created in Exercise 6, and use the **Cloud Agent** to develop the Book Reservation feature along with creating and executing its unit test suite.

---

## 📂 Target Scope
- Chat Agent Dropdown (bottom-left of Copilot Chat panel)
- `library-system/services/loan_service.py`
- Loan Renewal Issue link created in Exercise 6

---

## 🧭 The 3 Copilot Agent Types Explained

In the bottom-left corner of the Copilot Chat panel, click the agent selector to see the three available harnesses:

| Agent Type | Where It Runs | Best For |
|:---|:---|:---|
| **💻 Local** | Inside your current VS Code window | Fast interactive coding, inline edits, and questions tied directly to your open files. |
| **🤖 Copilot (SDK)** | In a background agent process | Multi-tasking without blocking your editor; runs code generation independently in the background. |
| **☁️ Cloud** | In GitHub's secure cloud compute | Asynchronous feature development, end-to-end testing, and PR automation on GitHub.com. |

---

## 📝 Step-by-Step Instructions

### Step 1: Assign Loan Renewal to the "Copilot" (SDK) Agent using the Issue Link
The **Copilot (SDK)** agent runs independently in the background Agent Host, freeing your editor session while it works.

1. Open Copilot Chat (<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> / <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>).
2. Click the agent dropdown at the bottom-left of the input box and select **🤖 Copilot**.
3. **Select the Model:** Click the model selector dropdown (next to the agent selector) and choose **Copilot Fusion** (which automatically picks or combines the best models for your task).
4. Paste the issue URL created in Exercise 6 and ask Copilot to implement it:
   ```text
   Implement loan renewal in loan_service.py according to the implementation plan and success criteria in this issue:
   <PASTE_YOUR_COPIED_ISSUE_URL_HERE>
   ```
5. **Observe:** The Copilot SDK agent inspects the issue requirements and writes the `renew_loan` method in the background, keeping your editor buffer responsive and free.

---

### Step 2: Assign Book Reservation & Test Generation to the "Cloud" Agent
Now let's offload a complete feature implementation—the Book Reservation service and its unit test suite—to the **Cloud Agent**!

1. In the agent dropdown at the bottom-left, switch from **Copilot** to **☁️ Cloud**.
2. Submit the following prompt:
   ```text
   Implement the Book Reservation feature for our library system:
   1. In `services/loan_service.py`, add `reserve_book(self, member_id: str, isbn: str)` allowing reservations when `available_copies == 0` and rejecting reference-only books.
   2. Create a test file `tests/test_reservation.py` with pytest test cases covering successful reservations and validation failures.
   3. Run the tests to verify the implementation.
   ```
3. **Observe:**
   - The Cloud Agent plans the implementation, modifies the service, writes the unit tests, and executes verification in GitHub's remote cloud environment without consuming local CPU or memory.

---

## 💡 Key Takeaways
- **Copilot (SDK):** Excels at parallel, non-blocking feature development right from your local machine, driven directly by GitHub issue links.
- **Cloud Agent:** Connects with GitHub's remote environment to handle end-to-end workflows (authoring features, writing test suites, and executing verification) offloaded to the cloud.

---

## 🎓 Congratulations!

You have completed all exercises of the **GitHub Copilot Hands-On Lab**!

### Summary of What You Mastered:
- ✅ **Setup & Template Clone:** Quickstart with an organization template
- ✅ **Code from Intent & Code Explanation:** Prompt-driven code generation, `@workspace` in Ask mode, and `/explain`
- ✅ **Diagnosing & Fixing (`/fix`):** Resolving race conditions & inventory leaks with pytest verification
- ✅ **Generating Unit Tests (Agent Mode):** Automated test file creation with parametrized tests
- ✅ **Path-Specific Instructions:** Scoping documentation standards via `applyTo: "docs/**/*.md"`
- ✅ **Custom Agents & Skills:** Authoring dedicated skills in `.github/skills/` and agent personas in `.github/agents/`
- ✅ **Model Context Protocol (MCP):** Creating GitHub issues directly from chat via GitHub MCP
- ✅ **Agent Harnesses:** Comparing Local, Copilot SDK (Fusion), and Cloud agents

---

[⬅️ Previous: Exercise 6](06-github-mcp-server.md) | [Table of Contents](README.md) | [Next: Exercise 8 ➡️](08-dotnet-modernization.md)
