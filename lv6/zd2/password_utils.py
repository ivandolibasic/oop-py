# https://www.geeksforgeeks.org/python-random-module
# https://www.geeksforgeeks.org/python-string-module
# https://www.w3schools.com/python/python_strings.asp
# https://www.w3schools.com/python/python_ref_functions.asp

import random
import string

def generate_password(complexity):
    if complexity == 1:
        chars = string.ascii_letters
        min_length = 8
        required_chars = [string.ascii_lowercase, string.ascii_uppercase]
    elif complexity == 2:
        chars = string.ascii_letters + string.digits
        min_length = 13
        required_chars = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    elif complexity == 3:
        chars = string.ascii_letters + string.digits + string.punctuation
        min_length = 16
        required_chars = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    else:
        return "Invalid complexity"

    while True:
        password = ''.join(random.choice(chars) for _ in range(min_length))
        if all(any(char in password for char in chars) for chars in required_chars):
            break

    return password

# another implementation:
def pass_generator(level):
    if level == 1:
        password = []
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.extend(random.choices(string.ascii_letters, k = 6))
        random.shuffle(password)
        return ''.join(password)
    elif level == 2:
        password = []
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.extend(random.choices(string.ascii_letters + string.digits, k = 10))
        random.shuffle(password)
        return ''.join(password)
    elif level == 3:
        password = []
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
        password.extend(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 12))
        random.shuffle(password)
        return ''.join(password)
    else:
        raise ValueError("Invalid level.")

def check_complexity(password):
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_punctuation = any(char in string.punctuation for char in password)

    if len(password) >= 16 and has_lowercase and has_uppercase and has_digit and has_punctuation:
        return 3
    elif len(password) >= 13 and has_lowercase and has_uppercase and has_digit:
        return 2
    elif len(password) >= 8 and has_lowercase and has_uppercase:
        return 1
    else:
        return 0

def run_demo_zd2():
    for level in range(1, 4):
        password = generate_password(level)
        print(f"Password with level {level}: {password}")
        complexity = check_complexity(password)
        print(f"Password complexity level: {complexity}")

run_demo_zd2()
