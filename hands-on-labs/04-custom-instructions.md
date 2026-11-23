# Exercise 4: Path-Specific Custom Instructions & Generating Documentation

[⬅️ Previous: Exercise 3](03-generating-unit-tests.md) | [Table of Contents](README.md) | [Next: Exercise 5 ➡️](05-custom-agent-and-skills.md)

---

## 🎯 Objective
Learn how to create a **path-specific custom instruction file** in the repository root that applies specifically to documentation files in `docs/` (`applyTo: "docs/**/*.md"`), and use the **Local Agent** to generate comprehensive technical documentation for the entire service layer, covering each service file individually.

---

## 📂 Target Files
- Instruction to create: `.github/instructions/docs.instructions.md` (repository root)
- Doc file to generate: `docs/service_architecture.md`
- Target scope: `library-system/services/` (Application Service Layer)

---

## 📖 Reference Documentation
- **Official Documentation:** [Custom instructions in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions)  
  *Learn how to define repository-wide and path-specific instruction files (`applyTo: "..."`) to customize GitHub Copilot behavior for your team and workflows.*

---

## 📝 Part A: Create Path-Specific Custom Instructions

### Step 1: Create the Instructions File at Workspace Root
You can create this file in either of two ways:

#### Option A: Using the VS Code Command Palette
1. Open the Command Palette (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> / <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>).
2. Type and run: **Chat: New Instructions File...**.
3. Select **`.github/instructions`** at the repository root.
4. Name the file `docs` (VS Code saves it as `.github/instructions/docs.instructions.md`).

#### Option B: Directly in File Explorer
1. In the **repository root directory**, create the folder path `.github/instructions/`.
2. Inside `.github/instructions/`, create a file named `docs.instructions.md`.

---

### Step 2: Add Documentation Standards with `applyTo`
Paste the following content into `.github/instructions/docs.instructions.md`:

````markdown
---
applyTo: "docs/**/*.md"
description: "Standards for technical documentation and Markdown service specifications"
---

# Technical Documentation Standards for Services

When generating or editing documentation files in `docs/`:
- **Document Header:** Include the title, a one-line overview of the service architecture, and target audience.
- **Per-Service Breakdown:** Provide a dedicated section for each service file containing:
  - Service Name & Source File path
  - Core Responsibility & Role in the system
  - Method Signatures Table (`Method`, `Parameters`, `Return Type`, `Exceptions Raised`)
  - Key Dependencies & collaborators
- **End-to-End Interaction Flow:** An executable Python code snippet showing how `CatalogService`, `MembershipService`, `FineCalculator`, and `LoanService` coordinate during borrowing and returning.
- **Domain Safety Rules:** Highlight critical rules (reference-only copies, quota limits, rollback on checkout failure).
````

---

## 📝 Part B: Generate Technical Documentation Using Local Agent

### Step 3: Switch to Local Agent
1. Open the Copilot Chat panel in VS Code (<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> / <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>).
2. Ensure the agent selector is set to **Local Agent**.

---

### Step 4: Ask Copilot to Generate Technical Documentation for the Service Layer
In Copilot Chat, submit the following concise prompt:

```text
Generate a comprehensive technical documentation file `docs/service_architecture.md` for the application service layer following our documentation instructions.

Include documentation for each service file in the service layer, detailing its purpose, method signatures table, exceptions, and an end-to-end Python interaction example.
```

---

### Step 5: Review and Save `docs/service_architecture.md`
1. Inspect Copilot's response:
   - Notice how Copilot reads `.github/instructions/docs.instructions.md` and generates structured sections for each of the 6 service files!
   - Notice how each service includes its methods table, parameter descriptions, exceptions, and an end-to-end coordination snippet.
2. In the workspace root, create the folder `docs/` (if it does not exist).
3. Save the generated content into `docs/service_architecture.md`.

---

### Step 6 (Optional): Try Method Docstrings with Inline Chat (`/doc`)
You can also generate in-code docstrings for individual methods:
1. Open `library-system/services/loan_service.py`.
2. Highlight the `borrow_book` method, press <kbd>Ctrl</kbd> + <kbd>I</kbd>, and type `/doc`.
3. Review the generated Google-style docstring with `Args`, `Returns`, and `Raises`, and click **Accept**.

---

## 💡 Key Takeaways
- Scoping instructions via `applyTo: "docs/**/*.md"` allows teams to maintain uniform technical specifications across all modules.
- Referencing multiple files (`#file:...`) simultaneously with the Local Agent lets Copilot synthesize comprehensive cross-service architecture documentation in a single turn.

---

[⬅️ Previous: Exercise 3](03-generating-unit-tests.md) | [Table of Contents](README.md) | [Next: Exercise 5 ➡️](05-custom-agent-and-skills.md)
