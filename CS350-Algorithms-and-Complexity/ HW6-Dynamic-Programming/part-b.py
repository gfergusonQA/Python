# Name: Gina Ferguson
# HW: 6, Dynamic Programming
# Part B: Brute-force, Iterative Algorithm for Palindrome Substring
# Language: Python
# See README.txt for instructions to run the code

from runtime_test import runtime_test

# ==========  Palindrome Substring checker  ===================

def is_palindrome(sub): 
    left, right = 0, len(sub) - 1
    while left < right: 
        if sub[left] != sub[right]:
            return False
        left += 1
        right -= 1
    return True

# Substring checking for longest possible, maintaining Brute Force method
# Strategy: 
#   1. Try every possible substring (like in Atul's Video)
#   2. For each substring, check if palindrome w/ is_palindrome helper function
#   3. Track and return lax length observed
# ==================================================================

def longest_substring(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    n = len(s)
    max_len = 0

    for i in range(n):
        for j in range(i, n):
            candidate = s[i:j + 1]
            if is_palindrome(candidate):
                current_len = j - i + 1
                if current_len > max_len:
                    max_len = current_len
    return max_len

# ========== 5 Sample Tests using a dictionary ======================
def run_examples():
    examples = [
        "AGCGT", 
        "abba",
        "banana",
        "racecar",
        "abcde"
    ]
    print("\nRunning 5 example tests:")
    for s in examples:
            length = longest_substring(s)
            print(f"  Input: {s!r:10} Longest palindromic substring length: {length}")

# ======================= Menu Function ===========================
def menu():
    quit_commands = {"4", "q", "Q", "quit", "QUIT", "Quit"}
    choice = None
    while choice not in quit_commands: 
        print("\nWelcome to Gina's Longest Palindrome Substring finder!")
        print("1) Run built-in 5 example tests")
        print("2) Enter your own string")
        print("3) Run runtime test (increasing input lengths)")
        print("4) Quit")

        choice = input("\nEnter choice (1 - 4): ").strip()
        if choice in quit_commands:
            print("Thanks and goodbye!\n\n")
            break
        if choice == "1":
            run_examples()
        elif choice == "2":
            user_input = input("\nEnter a string: ")
            if user_input == "":
                print("You entered an empty string. Please try again.")
            else:
                try:
                    length = longest_substring(user_input)
                    print(f" Input: {user_input!r:10} Longest palindromic substring length is: {length}")
                except TypeError as e:
                    print("Error:", e)
        elif choice == "3":
            runtime_test(longest_substring, "Brute Force")
        else:
            print("\nInvalid! Please try again and stick to the menu options.")


#========================= Run Main Program =========================
if __name__ == "__main__":
    menu()
