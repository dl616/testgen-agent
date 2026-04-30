```
# TestGen Agent 🚀

A multi-agent system for automated testcase generation, execution, validation, and self-healing using LLMs.

---

## ✨ Features
- Requirement parsing agent
- Testcase generation agent
- Code execution agent
- Validation agent
- 🔥 Auto Fix Agent (self-healing loop)

---

## 🧠 Architecture

Multi-Agent Workflow:

Requirement → Testcase → Execution → Validation → Fix → Re-run

---

## ▶️ Example Output

```bash
[Agent] Parsing requirement...
[Agent] Generating testcases...
[Agent] Running code...
[Agent] Validating results...

==== Test Report ====
Total: 5
Passed: 5
Failed: 0
```

------

## 📌 Use Cases

- Algorithm testing
- Automated QA
- Code evaluation

------

## 🚧 Future Work

- UI interface
- Coverage analysis
- Multi-language support

------

## 🔥 Advanced Feature: Auto Fix Agent

This system supports automatic code repair.

When test cases fail:

1. Analyze execution results
2. Identify logical errors
3. Generate corrected code
4. Re-run tests

👉 This creates a **self-healing system**

------

## ⚙️ How to Run

```
pip install -r requirements.txt
python main.py
```

------

## 📷 Demo

(Add your screenshot here)

------

## 📖 Description

This project demonstrates:

- Multi-agent collaboration
- Long-chain reasoning
- Automated testing and fixing loop using LLMs

