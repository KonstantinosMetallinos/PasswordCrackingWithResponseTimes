import itertools
import time
import timeit

import numpy as np

from ImplementationDetails import *


def crack_length(user, max_len=33, allowed_chars_in_pwd=chars_in_pwd, verbose=False) -> int:
    trials = 2000
    repeat = 10
    nth_smallest_element = 2
    times = np.empty(max_len)

    # Try guessing a password of every length between 0 to maxLen-1
    for i in range(max_len):
        i_time = timeit.repeat(stmt="check_password(user,x)",
                               setup=f'user={user!r};x=random_str({i!r}, {allowed_chars_in_pwd!r})',
                               globals=globals(),
                               number=trials,
                               repeat=repeat)

        # Take the nth fastest time of that list to respond. Workaround background tasks interfering with CPU contention
        i_time.sort()
        times[i] = (i_time[:nth_smallest_element])[-1]

    if verbose:
        most_likely_n = np.argsort(times)[::-1][:5]
        print(most_likely_n, times[most_likely_n] / times[most_likely_n[0]])

    most_likely_n = int(np.argmax(times))
    return most_likely_n


def crack_password(user, length, allowed_chars_in_pwd=chars_in_pwd, verbose=False):
    guess = random_str(length, allowed_chars_in_pwd)
    counter = itertools.count()
    trials = 1000
    while True:
        i = next(counter) % length
        for c in allowed_chars_in_pwd:
            alt = guess[:i] + c + guess[i + 1:]

            alt_time = timeit.repeat(stmt='check_password(user, x)',
                                     setup=f'user={user!r};x={alt!r}',
                                     globals=globals(),
                                     number=trials,
                                     repeat=10)
            guess_time = timeit.repeat(stmt='check_password(user, x)',
                                       setup=f'user={user!r};x={guess!r}',
                                       globals=globals(),
                                       number=trials,
                                       repeat=10)

            if check_password(user, alt):
                return alt

            if min(alt_time) > min(guess_time):
                guess = alt
                if verbose:
                    print(guess)


def main(user, all_chars=False, verbose=True):
    # Can change this variable to all chars for demos.
    if all_chars:
        allowed_chars_in_pwd = string.ascii_letters + string.digits + string.punctuation + " "
    else:
        # Redundant statement, but adding for PEP8 warnings.
        allowed_chars_in_pwd = chars_in_pwd

    last_predicted_length = -1
    length = 0
    while last_predicted_length != length:
        last_predicted_length = length
        length = crack_length(user, allowed_chars_in_pwd=allowed_chars_in_pwd, verbose=verbose)

    print(f"using most likely length {length}")

    if user == "bob" and length != len(bobs_password):
        # hasn't happened yet.
        print("Failed to predict correct password length - exiting...")
        exit(1)

    start_time = time.time()
    password = crack_password(user, length, chars_in_pwd, verbose=verbose)
    print(f"\nPassword Cracked:'{password}'")
    print(f"Password length {len(password)}, and it took: {(time.time() - start_time)} seconds")


if __name__ == "__main__":
    main(user="bob", all_chars=False, verbose=True)
