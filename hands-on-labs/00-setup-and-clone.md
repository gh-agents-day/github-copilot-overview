# Exercise 0: Setup – Create Repository from Template & Clone

[Table of Contents](README.md) | [Next: Exercise 1 ➡️](01-code-from-intent.md)

---

## 🎯 Objective
Create your personal workshop repository from the organization template (`gh-agents-day/github-copilot-overview`) and clone it locally into Visual Studio Code.

---

## 📝 Step-by-Step Instructions

### Step 1: Create Repository from Template
1. Open your browser and navigate to the template repository:
   👉 **`https://github.com/gh-agents-day/github-copilot-overview`**
2. Click the green **"Use this template"** button at the top right and select **"Create a new repository"**.
3. In the repository creation settings:
   - **Owner:** Select your assigned organization.
   - **Repository name:** Enter `github-copilot-overview-<your-name>` (or your preferred name).
   - **Visibility:** Select **Public** or **Internal** (as instructed by your trainer).
4. Click **"Create repository"**.

---

### Step 2: Clone the Repository to Your Local Machine
1. On your newly created repository page on GitHub, click the green **"Code"** button.
2. Under the **HTTPS** tab, copy the repository clone URL.
3. Open your terminal (PowerShell, Bash, or Command Prompt) and run:
   ```bash
   git clone <YOUR_COPIED_REPO_URL>
   ```
4. Navigate into the cloned folder:
   ```bash
   cd github-copilot-overview*
   ```

---

### Step 3: Open in Visual Studio Code & Install Dependencies
1. Open the project in VS Code:
   ```bash
   code .
   ```
2. In VS Code, open a new terminal (<kbd>Ctrl</kbd> + <kbd>`</kbd>).
3. Navigate into the application folder and install dependencies:
   ```bash
   cd library-system
   pip install -r requirements.txt
   ```
4. Verify your GitHub Copilot Chat extension is active and signed in.

---

## 💡 Key Takeaways
- Starting from an organization template ensures every attendee begins with identical starter code, tests, and database mocks.
- Working inside your own cloned repository gives you full permissions to commit changes, author branches, and test Copilot Cloud agents.

---

[Table of Contents](README.md) | [Next: Exercise 1 ➡️](01-code-from-intent.md)
