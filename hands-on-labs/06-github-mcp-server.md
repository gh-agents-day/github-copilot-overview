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
  
- **Official Repository:** [GitHub MCP Server (`github/github-mcp-server`)](https://github.com/github/github-mcp-server)  
  *The official Model Context Protocol (MCP) server provided by GitHub, exposing GitHub API tools (issues, pull requests, repository contents, branches, and commits) to AI coding assistants.*

---

## 📝 Step-by-Step Instructions

### Step 1: Configure the GitHub MCP Server
Model Context Protocol (MCP) enables Copilot Chat to safely communicate directly with GitHub APIs to search, create, and manage issues and pull requests.

1. In your workspace root, create or inspect `.vscode/mcp.json` (referencing [github/github-mcp-server](https://github.com/github/github-mcp-server)):
   ```json
   {
     "mcpServers": {
       "github": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-github"],
         "env": {
           "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
         }
       }
     }
   }
   ```
   > 💡 *Note:* The `@modelcontextprotocol/server-github` package is the standard npx distribution for the [GitHub MCP Server](https://github.com/github/github-mcp-server).

2. **Authenticate with GitHub:**
   - If prompted by VS Code to allow the GitHub MCP server, click **Allow** / **Sign in to GitHub**.
   - Ensure your environment token or GitHub CLI (`gh auth status`) is active and has access to your repository.

---

### Step 2: Create the Loan Renewal Issue via GitHub MCP
Ask Copilot to inspect the service and create the issue with an implementation plan and success criteria directly on GitHub:

1. In Copilot Chat (<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> / <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>), enter:
   ```text
   Using the GitHub MCP server, create a new issue titled "Feature: Loan Renewal" for #file:library-system/services/loan_service.py:
   - Allow members to extend their loan due_date by 14 days if the loan is ACTIVE.
   - Automatically define the Overview, Implementation Plan (methods, parameters, validation checks), and Success Criteria checklists.
   ```
2. Copilot analyzes `loan_service.py`, generates the structured issue body, and calls the GitHub MCP tool to post it directly to your repository.
3. Open the newly created issue on GitHub (or check the link returned in chat) and **copy its issue URL** (e.g., `https://github.com/<org>/<repo>/issues/1`) — you will pass this link to the Copilot SDK agent in **Exercise 7**!

---

## 💡 Key Takeaways
- The [github/github-mcp-server](https://github.com/github/github-mcp-server) provides a standardized protocol for connecting AI coding assistants to GitHub issues, PRs, and commits.
- You can query, inspect, and create GitHub issues without switching context to the browser.
- In **Exercise 7**, we will paste this issue link into the **Copilot (SDK)** agent to drive implementation, and assign **Book Reservation** to the **Cloud Agent**!

---

[⬅️ Previous: Exercise 5](05-custom-agent-and-skills.md) | [Table of Contents](README.md) | [Next: Exercise 7 ➡️](07-copilot-agents.md)
