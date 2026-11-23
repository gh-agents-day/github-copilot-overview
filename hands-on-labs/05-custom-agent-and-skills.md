# Exercise 5: Creating a Skill and a Custom Agent to Improve Test Coverage

[⬅️ Previous: Exercise 4](04-custom-instructions.md) | [Table of Contents](README.md) | [Next: Exercise 6 ➡️](06-github-mcp-server.md)

---

## 🎯 Objective
Learn how to define a reusable **Skill** with an explicit name, directory structure, and path (`.github/skills/improve-test-coverage/SKILL.md`), and author a **Custom Agent** (`.github/agents/test-coverage-agent.agent.md`) that explicitly references and executes that skill to analyze `catalog_service.py` and generate unit tests.

---

## 📂 Target Files to Create

| Entity | Exact File Name & Workspace Path | Description |
|:---|:---|:---|
| **Skill File** | `.github/skills/improve-test-coverage/SKILL.md` | Defines the step-by-step test coverage analysis instructions and output format |
| **Agent File** | `.github/agents/test-coverage-agent.agent.md` | Defines the `@test-coverage-agent` persona, tool permissions, and references the skill |

> **Directory Layout in Repository Root:**
> ```text
> .github/
> ├── skills/
> │   └── improve-test-coverage/
> │       └── SKILL.md              <-- Skill file name and exact path
> └── agents/
>     └── test-coverage-agent.agent.md  <-- Custom agent definition
> ```

---

## 📖 Reference Documentation
- **Official Documentation:** [Custom agents in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/custom-agents)  
  *Learn how to define custom agents with tailored system prompts, specialized tool capabilities, and reusable skills using `.github/agents/`.*

---

## 📝 Part A: Create the Skill File

### Step 1: Create the Skill Directory & File
1. In your workspace root (outside `library-system/`), create the folder path:  
   👉 `.github/skills/improve-test-coverage/`
2. Inside that folder, create the skill definition file:  
   👉 **`SKILL.md`**  
   *(Full path: `.github/skills/improve-test-coverage/SKILL.md`)*

### Step 2: Add Skill Instructions to `SKILL.md`
Paste the following content into `.github/skills/improve-test-coverage/SKILL.md`:

````markdown
---
name: improve-test-coverage
description: Analyzes source files and the README of a folder, compares them with the existing tests, and adds missing tests to improve coverage. Use when asked to improve test coverage, find untested code, or fill test gaps.
---

# Improve Test Coverage Skill

Follow these steps in order when analyzing test coverage for a service file:

## 1. Gather Behaviour
- Inspect the targeted service file (e.g., `library-system/services/catalog_service.py`).
- For each public method, note its inputs, outputs, edge cases, and raised exceptions.
- Read the project `README.md` and note documented domain rules (e.g., reference books cannot be borrowed).

## 2. Map Existing Tests
- Read the existing test suite in `library-system/tests/` and identify untested methods for this service.

## 3. Find the Gaps
Build a gap list identifying:
- Public methods with missing tests (e.g., `search_by_genre`, `is_available`, `decrement_copy`, `increment_copy`).
- Untested boundary conditions: 0 available copies, reference-only books.

## 4. Write the Tests
- Add tests to `library-system/tests/test_<service_name>.py` (e.g., `tests/test_catalog_service.py`). Do not modify source code.
- Use `pytest`, one behaviour per test, and `@pytest.mark.parametrize` for boundary conditions.
- Reuse existing fixtures; do not duplicate setup code.

## 5. Report Format
Start the reply with:

`🧪 Test Coverage Report - <target_service>`

Then output this table, one row per gap found:

| Source | Gap | Test added | Status |
|---|---|---|---|
| `<file>::<method>` | `<untested behaviour>` | `<test name>` | ✅ pass / ❌ fail (bug) |

End the reply with:

`Result: <n> gaps found, <m> tests added, <k> passing`
````

---

## 📝 Part B: Create the Custom Agent File

### Step 3: Create the Agent File
1. In your workspace root, create the folder path:  
   👉 `.github/agents/`
2. Inside that folder, create the agent definition file:  
   👉 **`test-coverage-agent.agent.md`**  
   *(Full path: `.github/agents/test-coverage-agent.agent.md`)*

### Step 4: Add Custom Agent Definition
Paste the following content into `.github/agents/test-coverage-agent.agent.md`:

````markdown
---
name: test-coverage-agent
description: Improves test coverage by finding untested code and adding pytest tests using the improve-test-coverage skill.
tools: ['codebase', 'search', 'editFiles', 'runTests', 'runCommands']
---

You are a Test Coverage Engineer specialist agent.

- **Primary Skill:** For any request about test coverage, untested code, or missing tests, invoke and strictly follow the `.github/skills/improve-test-coverage/SKILL.md` skill instructions and report format.
- Only create or edit files inside `library-system/tests/`. Never change source code.
- Always run `pytest` before reporting results.
- If the user asks for anything unrelated to testing, reply that you only work on test coverage.
````

---

## 📝 Part C: Run the Custom Agent

### Step 5: Select the Custom Agent in Chat
1. Open the Copilot Chat panel (<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> / <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>).
2. Click the agent dropdown at the bottom-left of the input box and select **test-coverage-agent** (or type `@test-coverage-agent`).

### Step 6: Trigger the Skill on a Single Service
Submit the following prompt:

```text
Improve the test coverage for #file:library-system/services/catalog_service.py using our improve-test-coverage skill.
```

### Step 7: Verify the Skill Execution
Observe Copilot's response:
- Verify that Copilot references `SKILL.md` (`.github/skills/improve-test-coverage/SKILL.md`).
- Verify the output begins with:
  `🧪 Test Coverage Report - catalog_service.py`
- Confirm it lists the gaps in a table (e.g., `search_by_genre`, `is_available`), creates `library-system/tests/test_catalog_service.py`, and runs the tests to confirm they pass!

---

## 💡 Key Takeaways
- **Skills (`.github/skills/<skill-name>/SKILL.md`):** Reusable, structured procedures with defined workflows and report templates.
- **Custom Agents (`.github/agents/<agent-name>.agent.md`):** Specialized persona configurations that tie together role prompts, tool capabilities, and target skills.

---

[⬅️ Previous: Exercise 4](04-custom-instructions.md) | [Table of Contents](README.md) | [Next: Exercise 6 ➡️](06-github-mcp-server.md)
