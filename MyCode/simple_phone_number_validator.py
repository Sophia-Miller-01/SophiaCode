# simple_phone_number_validator.py
import re

def validate_phone_number(phone_number):
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    return pattern.match(phone_number) is not None

if __name__ == "__main__":
    phone_number = input("Enter a phone number: ")
    if validate_phone_number(phone_number):
        print("Valid phone number")
    else:
        print("Invalid phone number")
