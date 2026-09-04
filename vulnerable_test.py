import os
import subprocess

# hardcoded password
password = "admin123"

# variables
a = 10
b = 20
c = 30
d = 40
print(a)

# dangerous functions
eval("a + b")
exec("print(c)")
os.system("echo Hello")
subprocess.call(["echo", "Hello"])

# used variable
result = a + b
print(result)

# unused variables
x = 100
y = 200
