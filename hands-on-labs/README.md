# GitHub Copilot Hands-On Lab: Library Management System

Welcome to the **Hands-On Lab exercises** for GitHub Copilot. Each lab is a self-contained guide with exact prompts, target files, and verification steps.

---

## 🗺️ Learning Path

| # | Lab Guide | Focus Area | Target File(s) | Estimated Time |
|:---:|---|---|---|:---:|
| **00** | [Exercise 0: Setup – Create Repository from Template & Clone](00-setup-and-clone.md) | Template instantiation (`gh-agents-day/github-copilot-overview`) & clone | Workspace root | 5 min |
| **01** | [Exercise 1: Code Generation from Intent & Code Explanation](01-code-from-intent.md) | Local Agent (`@workspace`), Ask mode, `#file:`, and `/explain` | `library-system/services/fine_calculator.py`, `services/loan_service.py` | 12 min |
| **02** | [Exercise 2: Diagnosing & Fixing Errors](02-diagnosing-and-fixing-errors.md) | Chat command `/fix` & test verification | `library-system/services/loan_service.py` | 10 min |
| **03** | [Exercise 3: Generating Unit Tests](03-generating-unit-tests.md) | Local Agent (`@workspace`) in Agent mode & `#file:` | `library-system/services/fine_calculator.py` | 10 min |
| **04** | [Exercise 4: Path-Specific Instructions & Generating Documentation](04-custom-instructions.md) | Path-specific instructions (`applyTo: "docs/**/*.md"`) & service layer architecture docs | `.github/instructions/docs.instructions.md`, `docs/service_architecture.md` | 10 min |
| **05** | [Exercise 5: Custom Agent & Skills](05-custom-agent-and-skills.md) | Defining test coverage skill (`SKILL.md`) and `@test-coverage-agent` persona | `.github/skills/`, `.github/agents/` | 10 min |
| **06** | [Exercise 6: GitHub MCP Server & Creating Issues](06-github-mcp-server.md) | Configure GitHub MCP and create "Loan Renewal" issue | `.vscode/mcp.json` | 8 min |
| **07** | [Exercise 7: Exploring Copilot Agent Types (Local, SDK, Cloud)](07-copilot-agents.md) | Copilot SDK (Issue link: Loan Renewal) & Cloud Agent (Book Reservation & Tests) | Chat Agent Dropdown | 10 min |
| **08** | [Exercise 8: .NET Application Modernization with GitHub Copilot](08-dotnet-modernization.md) | Modernizing .NET Framework 4.8 to .NET 10 SDK style & modern APIs | `legacy-dotnet-app/` | 10 min |

---

## 🚀 How to Complete the Labs
1. Complete [Exercise 0](00-setup-and-clone.md) to generate your repository from the template and clone it locally.
2. In VS Code terminal, install dependencies:
   ```bash
   cd library-system
   pip install -r requirements.txt
   ```
3. Progress sequentially through each exercise from **00 to 08**.
4. Every step provides exact prompts, expected outcomes, and commands to verify your work.

---

## 📖 Official VS Code Agent Customization References
- [Custom instructions in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions)
- [Custom agents in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/custom-agents)
- [Model Context Protocol (MCP) in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
