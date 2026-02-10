import re
import hashlib

def encrypt(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def check_strength(pwd):
    if len(pwd) < 8:
        return False
    if not re.search("[A-Z]", pwd):
        return False
    if not re.search("[a-z]", pwd):
        return False
    if not re.search("[0-9]", pwd):
        return False
    if not re.search("[!@#$%^&*]", pwd):
        return False
    return True

print("=== User Registration ===")

user = input("Username: ")
pwd = input("Password: ")

if not check_strength(pwd):
    print("Password too weak!")
    quit()

saved_pwd = encrypt(pwd)
print("Account created successfully!")

print("\n=== Login ===")

attempts = 3

while attempts > 0:
    u = input("Username: ")
    p = input("Password: ")

    if u == user and encrypt(p) == saved_pwd:
        print("Access Granted ✅")
        break
    else:
        attempts -= 1
        print("Wrong details. Attempts left:", attempts)

if attempts == 0:
    print("Account locked ❌")
