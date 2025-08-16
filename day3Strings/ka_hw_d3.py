from idlelib.debugobj_r import remote_object_tree_item

print('====================================')
print('============= Beginner =============')
print('====================================\n')

print('----------=====TASK 1=====----------')
print('Reverse a string Input: "hello" → Output: "olleh" Hint: Use slicing with a step of -1.')
def reverse_string(prop: str):
    return prop[::-1]

def reverse_string1(prop: str):
    reversed_string=''
    for char in prop:
        reversed_string=char + reversed_string
    return reversed_string

def reverse_string2(prop: str):
    return "".join(reversed(prop))

string = input("Enter a string: ")
print(f'#V1\nInput = {string}\nOutput = {reverse_string(string)}')
print(f'#V2\nInput = {string}\nOutput = {reverse_string1(string)}')
print(f'#V3\nInput = {string}\nOutput = {reverse_string2(string)}')

print('----------=====TASK 2=====----------')
print("Count vowels in a string Input: \"programming\" → Output: 3 Hint: Loop through characters and check if they are in 'aeiou'.")
def get_vowels_count(prop: str):
    vowels_count = 0
    for vowel in ['a', 'e', 'o', 'u', 'i']:
        vowels_count+=prop.lower().count(vowel)
    return vowels_count

def get_vowels_count1(prop: str):
    vowels = 'aeiou'
    return sum(1 for char in prop.lower() if char in vowels) #https://docs.python.org/3/reference/expressions.html#generator-expressions

string = input("Enter a string: ")
print(f'#V1\nInput = {string}\nOutput = {get_vowels_count(string)}')
print(f'#V2\nInput = {string}\nOutput = {get_vowels_count1(string)}')

print('----------=====TASK 3=====----------')
print('Check if a string is a palindrome Input: "madam" → Output: True Hint: Compare the string with its reversed version.')
def is_palindrome(prop: str):
    return prop == prop[::-1]

string = input("Enter a string: ")
print(f'Input = {string}\nOutput = {is_palindrome(string)}')

print('----------=====TASK 4=====----------')
print('Change string to title case using title() Input: "hello world" → Output: "Hello World" Hint: Use str.title() directly.')
def change_to_tile(prop: str):
    return prop.title()

string = input("Enter a string: ")
print(f'Input = {string}\nOutput = {change_to_tile(string)}')

print('----------=====TASK 5=====----------')
print('Remove all spaces from a string Input: " Python is fun " → Output: "Pythonisfun" Hint: Use replace(" ", "") or split() + join().')
def remove_spaces(prop: str):
    return prop.replace(' ', '')

def remove_spaces1(prop: str):
    return ''.join(prop.split(' '))

string = input("Enter a string: ")
print(f'#V1\nInput = {string}\nOutput = {remove_spaces(string)}')
print(f'#V2\nInput = {string}\nOutput = {remove_spaces1(string)}')

print('====================================')
print('=========== Intermediate ===========')
print('====================================\n')

print('----------=====TASK 6=====----------')
print('Count occurrences of a substring using count() Input: "banana", substring "na" → Output: 2 Hint: Use str.count(substring).')
def count_substrings(prop: str, substr: str):
    return prop.count(substr)

def count_substrings1(prop: str, substr: str):
    return sum(1 for i in range(len(prop) - len(substr) +1) if prop[i:i + len(substr)] == substr )

string = input("Enter a string: ")
substring = input("Enter a substring: ")
print(f'#V1\nInput:\nstring = {string}\nsubstring = {substring}\nOutput = {count_substrings(string, substring)}')
print(f'#V2\nInput:\nstring = {string}\nsubstring = {substring}\nOutput = {count_substrings1(string, substring)}')

print('----------=====TASK 7=====----------')
print('Replace all occurrences of a word using replace()\n'+
        'Input: "I like cats", replace "cats" with "dogs" → Output: "I like dogs"\n' +
        'Hint: Use str.replace(old, new).')
def replace_substring(prop: str, substr: str, new_substr: str):
    return prop.replace(substr, new_substr)

string = input("Enter a sentence: ")
substring = input("Enter a ward that you want to replace: ")
new_substring = input("Enter a new ward that you want to use as replacement: ")
print(f'Input = {string}\nword to replace = {substring}\nreplacement = {new_substring}\nOutput = {replace_substring(string, substring, new_substring)}')

print('----------=====TASK 8=====----------')
print('Check if a string starts and ends with the same letter\n' +
'Input: "level" → Output: True\n' +
'Hint: Compare string[0] with string[-1].')
import re

def compare_first_last_letter(prop: str):
    letters = re.findall(r"[a-z]", prop.strip().lower())
    return len(letters) > 0 and letters[0] == letters[-1]

sentence = input("Enter a sentence: ")
print(f'Input = {sentence}\nAre the first and the last letter equal? - {compare_first_last_letter(sentence)}')

print('----------=====TASK 9=====----------')
print('Remove punctuation from a string\n' +
'Input: "Hello, world!" → Output: "Hello world"\n' +
'Hint: Use string.punctuation from string module + comprehension.')
import string

def remove_punctuation(prop: str):
    return ''.join(char for char in prop if char not in  string.punctuation)

sentence = input("Enter a sentence: ")
print(f'Input = {sentence}\nOutput = {remove_punctuation(sentence)}')

print('----------=====TASK 10=====----------')
print('Format a string using format()\n'+
'Input: "My name is {name} and I am {age} years old", name="Alice", age=25\n' +
'Output: "My name is Alice and I am 25 years old"\n' +
'Hint: Use .format(name="Alice", age=25).')

def apply_format(name: str, age: str):
    return 'My name is {name} and I am {age} years old'.format(name=name, age=age)

def apply_format1(dictionary_person):
    return 'My name is {name} and I am {age} years old'.format(name=dictionary_person['name'], age=dictionary_person['age'])

name_val = input("Enter name: ")
age_val = input("Enter age: ")

person = {
    'name': name_val,
    'age': age_val,
}
print(f'#V1\nInput:\nname = {name_val}\nage = {age_val}\nOutput = {apply_format(name_val, age_val)}')
print(f'#V2\nInput:\nname = {name_val}\nage = {age_val}\nOutput = {apply_format1(person)}')

print('====================================')
print('============= Advanced =============')
print('====================================\n')

print('----------=====TASK 11=====----------')
print('Find all unique words in a string\n'+
'Input: "apple orange apple banana" → Output: ["apple", "orange", "banana"]\n' +
'Hint: Use split() + set().')

def find_unic_words(prop):
    return list(set(prop.split()))

sentence = input("Enter a sentence: ")
print(f'Input = {sentence}\nOutput = {find_unic_words(sentence)}')

print('----------=====TASK 12=====----------')
print('Find the longest word in a sentence\n' +
'Input: "Python is amazing" → Output: "amazing"\n'+
'Hint: Use max(words, key=len) after splitting.')

def find_largest_ward(prop: str):
    return max(prop.split(), key=len)

sentence = input("Enter a sentence: ")
print(f'Input = {sentence}\nOutput = {find_largest_ward(sentence)}')

print('----------=====TASK 13=====----------')
print('Check if two strings are anagrams\n' +
'Input: "listen", "silent" → Output: True\n'+
'Hint: Sort both strings and compare.')

def check_anagrams(first_ward, second_ward):
    return sorted(first_ward) == sorted(second_ward)

f_word = input("Enter the first ward: ")
s_word = input("Enter the second word: ")
print(f'Input:\nFirst ward = {f_word}\nSecond ward = {s_word}\nOutput = {check_anagrams(f_word, s_word)}')

print('----------=====TASK 14=====----------')
print('Split a string into chunks of N characters\n' +
'Input: "abcdefgh", N=3 → Output: ["abc", "def", "gh"]\n'+
'Hint: Use slicing in a loop: [s[i:i+N] for i in range(0, len(s), N)].')

def slice_into_chunks_n(prop, n):
    return [prop[i:i + n] for i in range(0, len(prop), n)]

word = input("Enter a ward: ")
chunk_len = int(input("Enter N: "))
print(f'Input:\nWard = {word}\nN = {chunk_len}\nOutput = {slice_into_chunks_n(word, chunk_len)}')

print('----------=====TASK 15=====----------')
print('Compress a string using run-length encoding\n' +
'Input: "aaabbc" → Output: "a3b2c1"\n'+
'Hint: Loop through the string, count consecutive characters.')

def compress_str(prop: str):
    result = []
    count = 1

    for i in range(1, len(prop)):
        if prop[i] == prop[i - 1]:
            count += 1
        else:
            result.append(prop[i - 1] + str(count))
            count = 1
    result.append(prop[-1] + str(count))
    return "".join(result)

from itertools import groupby

def compress_str1(prop: str):
    return ''.join(f'{ch}{len(list(group))}' for ch, group in groupby(prop))

word = input("Enter a ward: ")
print(f'Input:\nWard = {word}\nOutput = {compress_str(word)}')
print(f'Input:\nWard = {word}\nOutput = {compress_str1(word)}')
