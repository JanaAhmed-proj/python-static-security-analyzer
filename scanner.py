import ast
import sys
import time
import builtins

# Colors
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

# check input file
if len(sys.argv) < 2:
    print("Usage: python scanner.py <file.py>")
    exit()

filename = sys.argv[1]
print("Scanning:", filename)

# read file safely
with open(filename, "r", encoding="utf-8", errors="ignore") as f:
    code = f.read()

# parse AST safely
try:
    tree = ast.parse(code)
except SyntaxError as e:
    print("Syntax Error in file:", e)
    exit()

# reports
file_report = []
file_report.append("===== SECURITY REPORT =====\n")
file_report.append(f"Generated at: {time.ctime()}\n\n")

assigned = {}
used = set()
warnings = []

# scan AST
for node in ast.walk(tree):
    # assignments
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):
                assigned[target.id] = node.lineno
                if target.id.lower() == "password":
                    warnings.append((
                        node.lineno,
                        "MEDIUM",
                        "HARD_CODED_SECRET",
                        f"[MEDIUM] Hardcoded Password at line {node.lineno}\n"
                    ))

    # function calls
    if isinstance(node, ast.Call):
        # direct calls
        if isinstance(node.func, ast.Name):
            if node.func.id == "eval":
                warnings.append((
                    node.lineno,
                    "HIGH",
                    "DANGEROUS_CALL",
                    f"[HIGH] Dangerous function eval() at line {node.lineno}\n"
                ))
            if node.func.id == "exec":
                warnings.append((
                    node.lineno,
                    "HIGH",
                    "DANGEROUS_CALL",
                    f"[HIGH] Dangerous function exec() at line {node.lineno}\n"
                ))

        # attribute calls
        if isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name):
                if node.func.value.id == "os" and node.func.attr == "system":
                    warnings.append((
                        node.lineno,
                        "HIGH",
                        "DANGEROUS_CALL",
                        f"[HIGH] Dangerous function os.system() at line {node.lineno}\n"
                    ))
                if node.func.value.id == "subprocess" and node.func.attr == "call":
                    warnings.append((
                        node.lineno,
                        "HIGH",
                        "DANGEROUS_CALL",
                        f"[HIGH] Dangerous function subprocess.call() at line {node.lineno}\n"
                    ))

    # track used variables
    if isinstance(node, ast.Name):
        if isinstance(node.ctx, ast.Load):
            if node.id not in dir(builtins):
                used.add(node.id)

# unused variables
unused = set(assigned.keys()) - used
for var in unused:
    if var.lower() != "password":
        line = assigned[var]
        warnings.append((
            line,
            "LOW",
            "UNUSED_VAR",
            f"[LOW] Unused variable: {var} (defined at line {line})\n"
        ))

# sort by line number
warnings.sort(key=lambda x: x[0])

# output
for _, severity, wtype, msg in warnings:
    # terminal colors
    if severity == "HIGH":
        print(RED + msg + RESET, end="")
    elif severity == "MEDIUM":
        print(YELLOW + msg + RESET, end="")
    else:
        print(GREEN + msg + RESET, end="")

    # save to file (clean format)
    file_report.append(f"{severity} - {wtype} - {msg}")

print("\n===== END REPORT =====")
file_report.append("\n===== END REPORT =====\n")

# save report
with open("report.txt", "w", encoding="utf-8") as f:
    f.write("".join(file_report))
