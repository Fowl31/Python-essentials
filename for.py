#!/usr/bin/env python3

STRONG_LEN = 12
MIN_DIGITS = 2
MIN_CHAR = 4
MIN_SPECIAL = 1
SPECIAL = ['@', '#', '$', '%', '&', '*']

digit_counter = 0
character_counter = 0
special_counter = 0
met_requirements = False

while not met_requirements:
    password = input("Enter a password: ")

    # Count the number of digits in the password
    for character in password:
        if ord(character) >= ord("0") and ord(character) <= ord("9"):
            digit_counter += 1

    for ch in password:
        if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
            character_counter += 1

    for ch in password:
        if ch in SPECIAL:
            special_counter += 1

    if digit_counter >= MIN_DIGITS:
        if character_counter > 0:
            if special_counter> 0:
                if len(password) > 11:
                    met_requirements = True
                    print("Strong password entered")
    print("You havent entered a strong password")

