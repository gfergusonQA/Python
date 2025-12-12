# Name: Gina Ferguson
# Date: Dec. 3, 2025
# HW: 6 Dynamic Programming
# Part D: Dynamic Programming for longest palindromic substring problem
# Language: Python
# Strategy: 
#   1. Use a memo table to store indices
#   2. Fill the table bottom up
#   3. Track and return the max length of palindromic substring within string
# See README.txt for details on how to run the code

from runtime_test import runtime_test

# ============= Palindrome Substring Checker: ===================
# s = user-input string
# str = string type in Python (represents text)
# isinstance = Python helper function to check class or type (string in this case)

def longest_substring(userChoice):
    if not isinstance(userChoice, str):
        raise TypeError("Input must be a string.")
    n = len(userChoice)
    if n == 0:
        return 0

    # memoTable[i][j] will be True if userChoice[i:j+1] is a palindrome
    memoTable = [[False] * n for _ in range(n)]

    # Every single character is a palindrome of length 1
    max_len = 1

    #1) Length 1 substrings
    for i in range(n):
        memoTable[i][i] = True

    #2) Length 2 substrings
    for i in range(n - 1):
        if userChoice[i] == userChoice[i + 1]:
            memoTable[i][i+1] = True
            max_len = 2

    #3) Length 3 substrings
    for length in range(3, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1

            # Check matching end indices & whether inner substring is a palindrome
            if userChoice[i] == userChoice[j] and memoTable[i + 1][j - 1]:
                memoTable[i][j] = True
                if length > max_len:
                    max_len = length

    return max_len

# ================== 5 Sample Tests Function ==================

def run_examples():
    examples = [
        "AGCGT",
        "abba",
        "banana",
        "racecar",
        "abcde"
    ]
    print("\nRunning 5 example tests:")
    for userChoice in examples:
        length = longest_substring(userChoice)
        print(f" Input: {userChoice!r:10} Longest Palindromic Substring length: {length!r}")

# ================== User-driven Menu ===========================

def menu():
    quit_commands = {"4", "q", "Q", "quit", "QUIT", "Quit"}
    choice = None
    while choice not in quit_commands:
        print("\nWelcome to Gina's Longest Palindrome Substring Finder!")
        print("1) Run built-in 5 example tests")
        print("2) Enter your own string")
        print("3) Run runtime tests (increasing input lengths")
        print("4) Quit")

        choice = input("\nEnter choice (1 - 4): ").strip()
        if choice in quit_commands:
            print("Thanks and goodbye!\n\n")
            break
        if choice == "1":
            run_examples()
        elif choice == "2":
            userChoice = input("\nEnter a string: ")
            if userChoice == "":
                print("\nYou entered an empty string. Please try again.")
            else:
                try:
                    length = longest_substring(userChoice)
                    print(f"Longest palindromic substring length in {userChoice!r:10} is: {length}")
                except TypeError as e:
                    print("Error:", e)
        elif choice == "3":
            runtime_test(longest_substring, "Dynamic Programming")
        else:
            print("\nInvalid! Please try again and stick to the menu options.")

# ================= MAIN PROGRAM ================================

if __name__ == "__main__":
    menu()
