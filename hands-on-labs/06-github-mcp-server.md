# Exercise 6: GitHub Model Context Protocol (MCP) Server & Creating Issues

[⬅️ Previous: Exercise 5](05-custom-agent-and-skills.md) | [Table of Contents](README.md) | [Next: Exercise 7 ➡️](07-copilot-agents.md)

---

## 🎯 Objective
Learn how to configure and authenticate the official GitHub MCP server in VS Code using the [github/github-mcp-server](https://github.com/github/github-mcp-server) reference, and use Copilot to author and create an issue on GitHub detailing the implementation plan and success criteria for **Renewing a Loan**.

---

## 📂 Target Configuration File
- `.vscode/mcp.json` (workspace root)

---

## 📖 Reference Documentation

- **Official Documentation:** [Model Context Protocol (MCP) in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)  
  *Learn how to configure MCP servers in `.vscode/mcp.json` to extend Copilot Chat with custom tools, databases, and third-party APIs.*

---

## 📝 Step-by-Step Instructions

### Step 1: Configure the GitHub MCP Server
Model Context Protocol (MCP) enables Copilot Chat to communicate directly with GitHub APIs to search, create, and manage issues and pull requests using the official hosted GitHub Copilot MCP endpoint.

1. In your workspace root, create or update `.vscode/mcp.json` with the HTTP endpoint configuration (referencing [github/github-mcp-server](https://github.com/github/github-mcp-server)):

   ```json
   {
     "servers": {
       "github": {
         "type": "http",
         "url": "https://api.githubcopilot.com/mcp/"
       }
     }
   }
   ```

2. **Save and Authenticate:**

   - As and when you save `.vscode/mcp.json`, VS Code detects the MCP configuration.

   - When you start or run a prompt using the GitHub MCP server, VS Code will prompt you with an authentication dialog asking you to **Sign in with your GitHub credentials**.

   - Click **Allow** / **Sign in** and complete the standard GitHub authentication flow in your browser.

   - Once authenticated, Copilot gains secure access to your GitHub through the GitHub MCP server.

---

### Step 2: Create the Loan Renewal Issue via GitHub MCP
Ask Copilot to inspect the service and create the issue with an implementation plan and success criteria directly on GitHub:

1. Open Copilot Chat (<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> / <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>).

2. **Select the Local Harness and Local Agent:**

   - In the bottom-left of the Copilot Chat input box, check the agent selection dropdown.
   - Ensure the harness is set to **Local**

3. Enter the following prompt:

   ```text

   Using the GitHub MCP server, create a new issue titled "Feature: Loan Renewal" for #file:library-system/services/loan_service.py:
   - Allow members to extend their loan due_date by 14 days if the loan is ACTIVE.
   - Automatically define the Overview, Implementation Plan (methods, parameters, validation checks), and Success Criteria checklists.

   ```
4. Copilot analyzes `loan_service.py`, generates the structured issue body, and calls the GitHub MCP tool to post it directly to your repository.

5. Open the newly created issue on GitHub and have a look.

---

## 💡 Key Takeaways

- The [github/github-mcp-server](https://github.com/github/github-mcp-server) provides a standardized protocol for connecting AI coding assistants to GitHub issues, PRs, and commits.

- You can query, inspect, and create GitHub issues without switching context to the browser.

- In **Exercise 7**, we will paste this issue link into the **Copilot (SDK)** agent to drive implementation, and assign **Book Reservation** to the **Cloud Agent**!

---

[⬅️ Previous: Exercise 5](05-custom-agent-and-skills.md) | [Table of Contents](README.md) | [Next: Exercise 7 ➡️](07-copilot-agents.md)
