import string


# Tasks Beginner (★☆☆)
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


# Intermediate (★★☆)
# 6. Count occurrences of a substring using count()
def count_occurrences_basic(string_input: str, substring_input: str):
    return string_input.count(substring_input)


def count_occurrences_advanced(string_input: str, substring_input: str) -> int:
    if substring_input == "":
        return 0
    string_input = string_input.lower()
    substring_input = substring_input.lower()
    return string_input.count(substring_input)

print('NOTE: сount считает только не перекрывающие совпадения!!!')

print(count_occurrences_basic(string_input="banana", substring_input = "na"))
print(count_occurrences_advanced(string_input="baNanA", substring_input="nA"))


# 7. Replace all occurrences of a word using replace()
def replace_all_occurrences(string_input: str, old: str, new: str) -> str:
    return string_input.replace(old, new)


print(replace_all_occurrences(string_input="I like cats", old="cats", new="dogs"))


# 8. Check if a string starts and ends with the same letter
def check_start_and_end_letter(string_input:str) -> bool:
    return string_input[0] == string_input[-1]


print(check_start_and_end_letter(string_input="level"))


# 9. Remove punctuation from a string
def remove_punctuation(string_input: str) -> str:
    return "".join(char for char in string_input if char not in string.punctuation)


print(remove_punctuation(string_input="Hello, World!"))


# 10. Format a string using format()
def format_string(string_input: str, name: str, age: int) -> str:
    return string_input.format(name=name, age=age)


print(format_string(string_input="My name is {name} and I am {age} years old", name="Alice", age=25))


# Advanced (★★★)
# 11. Find all unique words in a string
def find_all_unique_words(string_input: str) -> list:
    return list(set(string_input.split()))


print(find_all_unique_words(string_input="apple orange apple banana"))


# 12. Find the longest word in a sentence
def find_longest_word(string_input: str) -> str:
    words = string_input.split()
    return max(words, key=len)


print(find_longest_word(string_input="Python is amazing"))


# 13. Check if two strings are anagrams
def check_if_anagrams(first_string: str, second_string: str) -> bool:
    first_string = ''.join(char for char in first_string.lower() if char.isalnum())
    second_string = ''.join(char for char in second_string.lower() if char.isalnum())
    return sorted(first_string) == sorted(second_string)


print(check_if_anagrams(first_string="listen", second_string="silent"))
