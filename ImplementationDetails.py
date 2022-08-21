import random
import string

chars_in_pwd = string.ascii_lowercase + " "
bobs_password = "super strong password"
password_database = {
    "sam": "hypothetical password ",
    "rob": "another hypothetical password",
    "bob": bobs_password,
    "testPcWith31Char": "p7!Q49Vf4lgm@71FYqE%m6GywfxS#Aj",
    "lastpass": "y500%WScPT%L"  # Generate new passwords at: https://www.lastpass.com/features/password-generator
}


def random_str(size, allowed_chars_in_pwd=chars_in_pwd):
    return ''.join(random.choices(allowed_chars_in_pwd, k=size))


def check_password(user, guess):
    """
    Simulated default way of implementing equals method under the hood.

    :param user: user name we wish to try to crack from our {$password_database} of users
    :param guess: a password guess we wish to check to see if its correct
    :return: True if the password is the correct for the username provided, false otherwise
    """
    actual = password_database[user]

    if len(guess) != len(actual):
        return False

    for i in range(len(actual)):
        if guess[i] != actual[i]:
            return False
    return True
