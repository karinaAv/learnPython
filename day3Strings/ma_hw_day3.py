# 1. Reverse a string Input
def reverse_input(string_input: str):
    return string_input[::-1]


print(reverse_input(string_input="hello"))


# 2. Count vowels in a string Input
def count_vowels_basic(string_input: str):
    vowels = []
    for char in string_input.lower():
        if char in "aeiou":
            vowels.append(char)
    return len(vowels)


def count_vowels_advanced(string_input: str):
    return sum(char in "aeiou" for char in string_input.lower())


print(count_vowels_basic(string_input="programming"))
print(count_vowels_advanced(string_input='programming'))


# 3. Check if a string is a palindrome
def check_palindrome(string_input: str):
    return string_input == string_input[::-1]


print(check_palindrome(string_input="madam"))


# 4. Change string to title case using title()
def change_string_to_title_case(string_input: str):
    return string_input.title()


print(change_string_to_title_case(string_input="hello world"))


# 5. Remove all spaces from a string
def remove_all_spaces_basic(string_input: str):
    return "".join(string_input.split())


def remove_all_whitespace_advanced(string_input: str) -> str:
    return "".join(char for char in string_input if not char.isspace())


print(remove_all_spaces_basic(string_input=" Python is fun "))
print(remove_all_whitespace_advanced(string_input=" Python is fun "))
