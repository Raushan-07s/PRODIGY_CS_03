'''
Task # 03
Password Complexity Checker
Build a tool that assesses the strength of a password based on criteria 
such as length, presence of uppercase and lowercase letters, numbers, and 
special characters. Provide feedback to users on the password's strength.

'''


import re

def assess_password_strength(password):

    score = 0
    feedback = ""


    if len(password) >= 12:
        score += 1
        feedback += "Password length is sufficient (12+ characters).\n"
    else:
        feedback += "Password length is too short (less than 12 characters).\n"

    
    if re.search(r"[A-Z]", password):
        score += 1
        feedback += "Password contains at least one uppercase letter.\n"
    else:
        feedback += "Password lacks uppercase letters.\n"

    
    if re.search(r"[a-z]", password):
        score += 1
        feedback += "Password contains at least one lowercase letter.\n"
    else:
        feedback += "Password lacks lowercase letters.\n"


    if re.search(r"\d", password):
        score += 1
        feedback += "Password contains at least one number.\n"
    else:
        feedback += "Password lacks numbers.\n"


    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        score += 1
        feedback += "Password contains at least one special character.\n"
    else:
        feedback += "Password lacks special characters.\n"

    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback


password = input("Enter a password: ")
strength, feedback = assess_password_strength(password)

print(f"Password strength: {strength}")
print(feedback)