import string

while True:
password = input("Enter a password (or 'exit' to quit): ")

if password.lower() == "exit":
    break

score = 0

if len(password) >= 8:
    score += 1
if any(c.islower() for c in password):
    score += 1
if any(c.isupper() for c in password):
    score += 1
if any(c.isdigit() for c in password):
    score += 1
if any(c in string.punctuation for c in password):
    score += 1

if score <= 2:
    print("Password Strength: Weak")
elif score == 3 or score == 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")