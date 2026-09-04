# Python Static Security Code Analyzer

A lightweight **Static Application Security Testing (SAST)** tool that scans Python source code for common security vulnerabilities and code-quality issues — without ever executing the code.

Built by students of the Software Engineering Department, Egyptian Chinese University (ECU), under the supervision of **Dr. Hossam Reda** (TAs: Asmaa Boghdady, Mohamed Khtab).

---

## Table of Contents

- [Overview](#overview)
- [Motivation](#motivation)
- [How It Works](#how-it-works)
- [Security Rules](#security-rules)
- [Warning Severity Levels](#warning-severity-levels)
- [Output](#output)
- [Core Modules](#core-modules)
- [Key Concepts Demonstrated](#key-concepts-demonstrated)
- [Limitations](#limitations)
- [Authors](#authors)

---

## Overview

Modern software vulnerabilities — from code injection to hardcoded credentials — often originate from patterns that are detectable *before* a single line of code ever runs. This project implements a simplified but functional static analyzer that inspects Python source files using the **Abstract Syntax Tree (AST)**, flagging risky constructs and generating a structured, severity-ranked report.

The analyzer detects:

- Potential security vulnerabilities
- Usage of dangerous functions (`eval`, `exec`)
- Risky system-level calls (`os.system`, `subprocess.call`)
- Hardcoded secrets (e.g. passwords)
- Unused or redundant variables

## Motivation

The project simulates a lightweight version of real-world tools used in industry — SAST scanners, secure code review systems, and DevSecOps pipelines — bridging the gap between academic study of compilers/static analysis and practical, applied cybersecurity tooling.

## How It Works

The system follows a modular pipeline:

```
Input File → AST Parsing → Code Traversal → Rule Engine → Warning Generation → Report Output
```

| Stage | Description |
|---|---|
| **Input Handling** | Accepts a Python source file via the command line. Missing input is handled gracefully with usage instructions. |
| **File Processing** | Opens the file with UTF-8 encoding and error handling to safely process non-standard characters. |
| **AST Parsing** | Converts source code into a structured tree via `ast.parse(code)`. Syntax errors halt analysis immediately. |
| **Code Traversal** | Walks every node of the tree with `ast.walk(tree)`, inspecting assignments, function calls, and attribute access. |
| **Rule Engine** | Evaluates each node against a set of predefined security rules. |
| **Report Output** | Generates severity-classified results, shown in the terminal and saved to a file. |

This modular separation keeps each stage independent, making the analyzer easy to extend with additional rules in the future.

## Security Rules

### 1. Dangerous Function Detection
Flags use of `eval()` and `exec()`, which allow execution of dynamically generated code.
> **Risks:** code injection, execution of untrusted payloads, potential full system compromise.

### 2. System Command Execution Detection
Flags direct OS-level calls such as `os.system()` and `subprocess.call()`.
> **Risks:** unauthorized command execution, file manipulation, execution of malicious scripts.

### 3. Hardcoded Secrets Detection
Flags sensitive values embedded directly in code, e.g.:
```python
password = "123456"
```
> **Risks:** credential exposure, increased damage if source code leaks, violation of secure coding standards.

### 4. Unused Variable Detection
Compares assigned vs. used variables:
```
Unused = Assigned − Used
```
> **Purpose:** improves readability, reduces memory waste, surfaces incomplete logic.

## Warning Severity Levels

| Level | Meaning | Impact |
|---|---|---|
| 🔴 **High** | Critical security risk | System compromise possible |
| 🟡 **Medium** | Moderate risk | Security concern |
| 🟢 **Low** | Code quality issue | Non-critical improvement |

## Output

**Terminal:** results are color-coded in real time (red = high, yellow = medium, green = low) for quick prioritization.

**Report file (`report.txt`):** a persistent, structured log including severity, issue type, line number, description, and analysis timestamp.

**Example:**
```
[HIGH] Dangerous function os.system() at line 12
[MEDIUM] Hardcoded Password at line 8
[LOW] Unused variable: temp (defined at line 20)

===== END REPORT =====
```

## Core Modules

All built using Python's standard library — no external dependencies required.

| Module | Purpose |
|---|---|
| `ast` | Parses source code into a structured, analyzable tree |
| `sys` | Handles command-line arguments |
| `time` | Generates timestamps for traceability |
| `builtins` | Distinguishes built-in functions from user-defined ones during unused-variable detection |

## Key Concepts Demonstrated

- Abstract Syntax Tree (AST) based static analysis
- Static Application Security Testing (SAST) principles
- Security vulnerability detection techniques
- Efficient use of data structures (sets, dictionaries)
- Command-Line Interface (CLI) design
- File handling and encoding management
- Pattern recognition and rule-based logic

## Limitations

This is an academic, simplified implementation rather than an industrial-grade scanner. It does not perform data-flow or taint analysis, cannot resolve dynamic imports, and its rule set covers only a small set of common vulnerability patterns. It should be viewed as a conceptual foundation rather than a production security tool.

## Authors

Software Engineering Department, ECU



**Supervised by:** Dr. Hossam Reda
**Teaching Assistants:** Asmaa Boghdady, Mohamed Khtab
