# This file is a helper function to import
# for testing string inputs lengths of multiple, increasing lengths

import time
import random
import string

def generate_random_string(n):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))

def runtime_test(algorithm_function, label):
    sizes = [
            10,
            50,
            100,
            200,
            500,
            1000,
            2000,
            5000,
            10000
            ]
    print(f"\nRuntime Test for {label!r:10}")
    print("-----------------------------------------")

    for n in sizes:
        test_string = generate_random_string(n)
        start = time.time()
        algorithm_function(test_string)
        end = time.time()
        duration = end - start
        print(f"String length = {n!r:10} took {duration:.8f} seconds.")
