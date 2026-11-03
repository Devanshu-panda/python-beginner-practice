common_pass = {"password", "password123", "admin123", "12345678", "qwerty123"}
special_char = "!@#$%^&*()_+-={}[]|\"\'<>,.?/~`"
attempt = 0

def validate_password(password):
    score = 0
    is_valid = True
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        is_valid = False
    else:
        score += 1
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        is_valid = False
    else:
        score += 1
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        is_valid = False
    else:
        score += 1
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        is_valid = False
    else:
        score += 1
    if not any(char in special_char for char in password):
        print("Password must contain at least one special character.")
        is_valid = False
    else:
        score += 1
    if ("qwerty" in password.lower()) or ("1234" in password) or ("abcd" in password.lower()):
        print("Password must not contain common sequences like 'qwerty', '1234', or 'abcd'.")   
        is_valid = False
    else:
        score += 1
    if password.lower() in common_pass:
        print("Password is too common. Please choose a more unique password.")
        is_valid = False
    else:
        score += 1
    if any(char.isspace() for char in password):
        print("Password must not contain spaces.")
        is_valid = False
    if is_valid:
        print("Password is valid.")
    else:
        print("Password is invalid.")
    return score, is_valid
    
def password_strength(score):
    if 0 <= score <= 3:
        print("Password strength: Weak")
    elif 4 <= score <= 5:
        print("Password strength: Moderate")
    elif 6 <= score <= 7:
        print("Password strength: Strong")

while True:
    password = input("Enter a Password: ")
    score, is_valid = validate_password(password)
    password_strength(score)
    attempt += 1
    if is_valid:
        break

print(f"\nPassword accepted after {attempt} attempt(s).")