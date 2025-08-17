- https://metanit.com/python/tutorial/5.1.php
- https://metanit.com/python/tutorial/5.2.php
- https://metanit.com/python/tutorial/5.3.php
- https://ru.hexlet.io/courses/python-declarative-programming/lessons/generator-expressions/theory_unit

#Tasks
Beginner (★☆☆)
1. Reverse a string
Input: "hello" → Output: "olleh"
Hint: Use slicing with a step of -1.

2. Count vowels in a string
Input: "programming" → Output: 3
Hint: Loop through characters and check if they are in 'aeiou'.

3. Check if a string is a palindrome
Input: "madam" → Output: True
Hint: Compare the string with its reversed version.

4. Change string to title case using title()
Input: "hello world" → Output: "Hello World"
Hint: Use str.title() directly.

 5. Remove all spaces from a string
Input: " Python is fun " → Output: "Pythonisfun"
Hint: Use replace(" ", "") or split() + join().

##Intermediate (★★☆)
6. Count occurrences of a substring using count()
Input: "banana", substring "na" → Output: 2
Hint: Use str.count(substring).

7. Replace all occurrences of a word using replace()
Input: "I like cats", replace "cats" with "dogs" → Output: "I like dogs"
Hint: Use str.replace(old, new).

8. Check if a string starts and ends with the same letter
Input: "level" → Output: True
Hint: Compare string[0] with string[-1].

9. Remove punctuation from a string
Input: "Hello, world!" → Output: "Hello world"
Hint: Use string.punctuation from string module + comprehension.

10. Format a string using format()
Input: "My name is {name} and I am {age} years old", name="Alice", age=25
Output: "My name is Alice and I am 25 years old"
Hint: Use .format(name="Alice", age=25).

##Advanced (★★★)
11. Find all unique words in a string
Input: "apple orange apple banana" → Output: ["apple", "orange", "banana"]
Hint: Use split() + set().

12. Find the longest word in a sentence
Input: "Python is amazing" → Output: "amazing"
Hint: Use max(words, key=len) after splitting.

13. Check if two strings are anagrams
Input: "listen", "silent" → Output: True
Hint: Sort both strings and compare.

14. Split a string into chunks of N characters
Input: "abcdefgh", N=3 → Output: ["abc", "def", "gh"]
Hint: Use slicing in a loop: [s[i:i+N] for i in range(0, len(s), N)].

15. Compress a string using run-length encoding
Input: "aaabbc" → Output: "a3b2c1"
Hint: Loop through the string, count consecutive characters.
