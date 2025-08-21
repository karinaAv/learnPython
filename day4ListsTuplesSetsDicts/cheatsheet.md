# ✅ PYTHON LIST CHEAT SHEET FOR TEST AUTOMATION

# 📌 BASIC OPERATIONS
my_list = ["a", "b", "c"]
my_list[0]        # First item: 'a'
my_list[-1]       # Last item: 'c'
my_list[1:3]      # Slice: ['b', 'c']
len(my_list)      # Length of list

# 🔁 LOOPING
for item in my_list:
    print(item)

for i, item in enumerate(my_list):
    print(f"Index {i}: {item}")

# ✅ CONDITIONALS
assert "a" in my_list
assert any(my_list)
assert all([bool(x) for x in my_list])

# 🧪 LIST COMPREHENSION
squares = [x**2 for x in range(5)]
non_empty = [x for x in ["a", "", "b"] if x]

# 🔧 MAP, FILTER, JOIN
nums = [1, 2, 3]
strs = list(map(str, nums))         # ['1', '2', '3']
evens = list(filter(lambda x: x % 2 == 0, nums))
print(", ".join(strs))             # '1, 2, 3'

# ✂️ STRIP, SPLIT, JOIN
raw = ["  Alice  ", " Bob"]
clean = [name.strip() for name in raw]
normalized = [" ".join(name.strip().split()) for name in raw]

# 🔄 FLATTEN NESTED LIST
nested = [[1, 2], [3], [4, 5]]
flat = [x for row in nested for x in row]

# 🆚 COMPARE LISTS
actual = ["a", "b"]
expected = ["a", "b"]
for i, (a, e) in enumerate(zip(actual, expected)):
    assert a == e, f"Mismatch at {i}: expected {e}, got {a}"

# 🔢 SORTING
words = ["banana", "Apple"]
sorted_words = sorted(words, key=str.lower)

# ✅ SETS FOR ORDER-INDEPENDENT CHECKS
set1 = {"Yes", "No"}
set2 = set(["No", "Yes", "Yes"])
assert set2 <= set1

# 🧰 USEFUL TOOLS
from itertools import product
browsers = ["Chrome", "Firefox"]
roles = ["Admin", "User"]
all_combos = list(product(browsers, roles))

# ⚙️ GENERATORS

def generate_users():
    for i in range(10000):
        yield f"user_{i}"

# MEMORY-EFFICIENT LOG SCAN
with open("test.log") as f:
    for line in f:
        if "ERROR" in line:
            print(line)

# 🎯 WHEN TO USE WHAT:
# - list: when order matters and you need mutability
# - set: when order doesn't matter, and you want uniqueness
# - map/filter: to transform or filter lists without loops
# - join/split/strip: for cleaning and formatting string lists
# - zip/enumerate: to compare or track index during loops
# - sorted(key=...): custom sort logic
# - generators: for large/test data without using too much memory

[//]: # (a, b = [1, 2]           # a=1, b=2)

[//]: # (x, y, z = &#40;10, 20, 30&#41;  # кортеж/список/любой итерируемый)

[//]: # ()
[//]: # (Andreeva Margarita, [21/08/2025 5:51 pm])

[//]: # (вложенная распаковка &#40;x, &#40;y, z&#41;&#41; = &#40;1, &#40;2, 3&#41;&#41;     # x=1, y=2, z=3)
