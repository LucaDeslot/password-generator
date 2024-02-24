import random
import string


def get_random_char():
    return random.choice(string.ascii_letters + string.digits + string.punctuation)


def get_random_number():
    return random.randint(0, 9)


def get_random_special_char():
    special_chars = string.punctuation
    return random.choice(special_chars)


def get_number_of_uppercase_letters(password):
    count = 0
    for char in password:
        if char.isupper():
            count += 1
    return count


def get_number_of_numbers(password):
    count = 0
    for char in password:
        if char.isdigit():
            count += 1
    return count


def get_number_of_special_chars(password):
    count = 0
    for char in password:
        if char in string.punctuation:
            count += 1
    return count
