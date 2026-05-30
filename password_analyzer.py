import re
import hashlib
import getpass

common_passwords = [
    "password", "123456", "123456789", "qwerty", "admin",
    "welcome", "letmein", "abc123", "password123", "iloveyou"
]

try:
    password = getpass.getpass("Enter your password: ")
except Exception:
    password = input("Enter your password: ")

score = 0
feedback = []

if password.lower() in common_passwords:
    feedback.append("Avoid using common passwords.")
else:
    score += 1

if len(password) >= 12:
    score += 1
else:
    feedback.append("Use at least 12 characters.")

if re.search(r"[A-Z]", password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter.")

if re.search(r"[a-z]", password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter.")

if re.search(r"\d", password):
    score += 1
else:
    feedback.append("Add at least one number.")

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    feedback.append("Add at least one special character.")

if score <= 2:
    strength = "Weak"
    risk = "High Risk"
elif score <= 4:
    strength = "Medium"
    risk = "Medium Risk"
else:
    strength = "Strong"
    risk = "Low Risk"

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("\nCyber Password Strength Analyzer")
print("--------------------------------")
print(f"Password Strength: {strength}")
print(f"Security Score: {score}/6")
print(f"Risk Level: {risk}")

print("\nSecurity Feedback:")
if feedback:
    for item in feedback:
        print(f"- {item}")
else:
    print("- Password meets strong security requirements.")

print("\nSHA-256 Hash:")
print(hashed_password)

