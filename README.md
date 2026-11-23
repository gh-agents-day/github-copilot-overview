# GitHub Copilot Hands-On Lab: Library Management System

Welcome to the **GitHub Copilot Hands-On Lab** repository! This workshop takes developers, tech leads, and architects through practical AI-assisted coding and advanced **Agentic SDLC** workflows using a realistic Python **Library Management System**.

---

## 📁 Repository Structure

```text
GHCP HOL/
├── README.md                  # Main workshop homepage & quickstart
├── hands-on-labs/             # 📖 STEP-BY-STEP LAB GUIDES (Individual exercise files)
│   ├── README.md              # Exercise index & curriculum map
│   ├── 00-setup-and-clone.md
│   ├── 01-code-from-intent.md
│   ├── 02-diagnosing-and-fixing-errors.md
│   ├── 03-generating-unit-tests.md
│   ├── 04-custom-instructions.md
│   ├── 05-custom-agent-and-skills.md
│   ├── 06-github-mcp-server.md
│   ├── 07-copilot-agents.md
│   └── 08-dotnet-modernization.md
├── legacy-dotnet-app/         # 💻 LEGACY .NET APP: Modernization target for Exercise 8
│   ├── LegacyLibraryReports.csproj # Classic .NET Framework 4.8 XML project
│   ├── packages.config        # Legacy NuGet dependencies (Newtonsoft.Json 9.0.1)
│   ├── App.config             # Classic XML configuration (<appSettings>)
│   ├── Properties/AssemblyInfo.cs # Classic assembly metadata
│   └── Program.cs             # Deprecated APIs (WebClient, MD5CryptoServiceProvider, HttpUtility)
└── library-system/            # 🎯 THE LAB WORKSPACE: Participants work here
    ├── data/
    │   └── library_db.json    # 🗄️ Single JSON file mocking the database (Books, Members, Loans)
    ├── models/
    │   ├── __init__.py
    │   └── library_models.py  # Domain entities (Book, Member, MemberType, LoanRecord, LoanStatus)
    ├── services/
    │   ├── __init__.py
    │   ├── database_service.py# JSON Database mock providing full CRUD operations
    │   ├── catalog_service.py # Book catalog lookup and stock decrement/increment
    │   ├── membership_service.py # Member borrow quota & fine threshold verification
    │   ├── fine_calculator.py # Overdue fine rules (Exercise 1: Code from intent)
    │   ├── notification_service.py # Mock patron notification service
    │   └── loan_service.py    # Loan checkout orchestration (Exercise 1: /explain & Exercise 2: /fix)
    ├── api.py                 # FastAPI application with REST endpoints
    ├── schemas.py             # Pydantic validation models
    ├── main.py                # Server runner (launches Swagger UI directly)
    ├── requirements.txt       # Dependencies (fastapi, uvicorn, pydantic, pytest, httpx)
    ├── pytest.ini             # Pytest discovery configuration
    └── tests/                 # Unit & API test suite (contains initial failing bug test)
        ├── __init__.py
        ├── test_database.py   # CRUD tests for JSON mock database
        ├── test_membership.py # Passing membership tests
        ├── test_loan_service.py # Borrow tests (contains deliberate book copy leak bug)
        └── test_api.py        # FastAPI endpoint integration tests
```

---

## ⚡ Quickstart for Participants

### 1. Prerequisites Check

Make sure you have installed:

- [Visual Studio Code](https://code.visualstudio.com/) with:
  - **GitHub Copilot Chat** extension
  - **Python** extension

- [Python 3.10+](https://www.python.org/)

- [Git](https://git-scm.com/)

---

### 2. Setup the Environment

Complete [Exercise 0](hands-on-labs/00-setup-and-clone.md) to instantiate the template repository (`gh-agents-day/github-copilot-overview`) under your organization, clone it, and install dependencies:

```bash
cd library-system
pip install -r requirements.txt
```

---

### 3. Run the Application

Start the FastAPI application with Swagger UI:

```bash
python main.py
```
- It automatically starts the server and opens the interactive **Swagger UI** in your default web browser at `http://127.0.0.1:8000/docs`.
- The root URL `http://127.0.0.1:8000/` automatically redirects straight to the Swagger documentation.
- You can directly try out all endpoints (`/books`, `/members`, `/loans/borrow`, `/loans/return`) inside Swagger.

#### Run the Unit Test Suite
```bash
pytest
```
> ℹ️ **Expected Test Output:**  
> 15 tests pass and 1 test intentionally fails (`test_borrow_fails_restores_book_copy`), which participants will fix in Exercise 2!

---

### 4. Start the Hands-On Lab

Open the lab index and start with **Exercise 0**:  

👉 **[Hands-On Lab Directory](hands-on-labs/README.md)**

---

## 🧭 Hands-On Exercises Directory

| # | Exercise Guide | Method / Tool | Key Skill Learned |
|:---:|---|---|---|
| **00** | [00-setup-and-clone.md](hands-on-labs/00-setup-and-clone.md) | GitHub Template & Git Clone | Creating repository from `gh-agents-day/github-copilot-overview` and cloning in VS Code |
| **01** | [01-code-from-intent.md](hands-on-labs/01-code-from-intent.md) | Chat Panel (`#file:`, Ask mode) & `/explain` | Implementing fine calculation logic & analyzing checkout flow |
| **02** | [02-diagnosing-and-fixing-errors.md](hands-on-labs/02-diagnosing-and-fixing-errors.md) | Inline Chat (`/fix`) | Fixing catalog book copy leaks during failed checkouts |
| **03** | [03-generating-unit-tests.md](hands-on-labs/03-generating-unit-tests.md) | Local Agent (`@workspace`) in Agent mode | Automatically creating and writing parametrized test files |
| **04** | [04-custom-instructions.md](hands-on-labs/04-custom-instructions.md) | `.github/instructions/docs.instructions.md` | Path-specific instructions (`applyTo: "docs/**/*.md"`) & generating service layer docs |
| **05** | [05-custom-agent-and-skills.md](hands-on-labs/05-custom-agent-and-skills.md) | `.github/skills/`, `.github/agents/` | Authoring a test coverage skill (`SKILL.md`) and dedicated `@test-coverage-agent` persona |
| **06** | [06-github-mcp-server.md](hands-on-labs/06-github-mcp-server.md) | `.vscode/mcp.json` | Configuring GitHub MCP server and creating a "Loan Renewal" issue |
| **07** | [07-copilot-agents.md](hands-on-labs/07-copilot-agents.md) | Chat Agent Dropdown | Copilot SDK (Issue link: Loan Renewal) & Cloud Agent (Book Reservation & Tests) |
| **08** | [08-dotnet-modernization.md](hands-on-labs/08-dotnet-modernization.md) | Copilot Modernization Agent | Modernizing .NET Framework 4.8 console app to cross-platform .NET 10 |

---

## 📖 Official Reference Documentation
- **Custom Instructions:** [Custom instructions in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions)
- **Custom Agents:** [Custom agents in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/custom-agents)
- **MCP Servers:** [Model Context Protocol (MCP) in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
- **GitHub MCP Server:** [GitHub MCP Server Repository (`github/github-mcp-server`)](https://github.com/github/github-mcp-server)
