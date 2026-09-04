# Python Static Security Analyzer — Project Documentation

## 1. Project Overview

This project implements a lightweight static security analyzer for Python source code. The program examines a Python file **without executing it**, parses the source code into an Abstract Syntax Tree (AST), and searches for selected security and code-quality issues.

The analyzer currently identifies four main categories of findings:

- Hard-coded passwords or password variables — reported as **MEDIUM** severity.
- Use of `eval()` and `exec()` — reported as **HIGH** severity.
- Use of `os.system()` and `subprocess.call()` — reported as **HIGH** severity.
- Assigned variables that are not subsequently used — reported as **LOW** severity.

## 2. Methodology

The scanner follows a static-analysis workflow:

1. It receives the target Python file through the command line.
2. It reads the source code and passes it to Python's built-in `ast` module.
3. The resulting Abstract Syntax Tree is traversed using `ast.walk()`.
4. During traversal, the program inspects assignments, function calls, and variable references.
5. Detected findings are stored with their line number, severity level, vulnerability type, and descriptive message.

## 3. Main Components

| Component | Description |
|---|---|
| **AST Parsing** | Converts Python source code into a structured tree so the analyzer can inspect program constructs rather than relying only on text matching. |
| **Security Rules** | Detects selected dangerous calls and possible hard-coded credentials. |
| **Variable Analysis** | Tracks assigned and used variable names to identify simple unused-variable cases. |
| **Severity Classification** | Findings are categorized as HIGH, MEDIUM, or LOW. |
| **Terminal Reporting** | Uses ANSI escape codes to display severity levels in different terminal colors. |
| **File Reporting** | Creates a clean `report.txt` file containing the detected findings and generation time. |

## 4. How to Run

```bash
python scanner.py <file.py>
```

The analyzer is intended to be run from a terminal. The input argument specifies the Python source file to scan. If the file contains invalid Python syntax, the program reports the syntax error and stops instead of continuing with an invalid AST.

## 5. Example Detection Logic

For example, if the scanned program contains `eval(user_input)`, the analyzer recognizes the call as a potentially dangerous operation and produces a HIGH-severity warning. Similarly, a variable named `password` assigned directly in the source is reported as a potential hard-coded secret.

## 6. Limitations

This implementation is a lightweight **educational** static analyzer rather than a complete security auditing framework. Its rules are pattern-based and therefore may produce false positives or miss vulnerabilities that require deeper data-flow or control-flow analysis. For example, it does not currently determine whether a value assigned to a variable actually contains a secret, nor does it perform taint analysis to track untrusted input into dangerous sinks.

## 7. Academic Significance

The project demonstrates practical application of:

- Static program analysis
- Abstract syntax trees
- Source-code inspection
- Vulnerability classification
- Automated reporting

It also provides a foundation that can be extended with additional security rules, data-flow analysis, configuration files, severity scoring, and integration into software-development workflows.

## 8. Complete Source Code

See [`scanner.py`](./scanner.py) for the full, runnable source code.
