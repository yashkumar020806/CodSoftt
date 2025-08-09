import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return ""

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols
    password = ""
    for i in range(length):
        password += random.choice(all_chars)

    return password

def main():
    print("PASSWORD GENERATOR")
    try:
        length = int(input("Enter password length: "))
        result = generate_password(length)
        if result != "":
            print("Generated Password:", result)
    except:
        print("Invalid input. Please enter a number.")

main()
