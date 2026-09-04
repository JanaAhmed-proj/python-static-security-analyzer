import os
import subprocess

# hardcoded secret
password = "123456"

# used variables
a = 10
b = 20

# unused variable
temp = 999

# dangerous eval
user_input = "a + b"
result = eval(user_input)

# dangerous exec
exec("print('Hello from exec')")

# command injection risk
cmd = "echo Hello"
os.system(cmd)

# subprocess usage
subprocess.call(["echo", "Hi"])


# SQL injection example
def get_user(cursor, name):
    query = "SELECT * FROM users WHERE name = '%s'" % name
    cursor.execute(query)


# safe usage
total = a + b
print(total)
