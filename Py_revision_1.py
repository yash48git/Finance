# =====================================
# PYTHON DATA STRUCTURES REVISION
# =====================================

# -----------------------------
# 1️⃣ LISTS
# -----------------------------
# Ordered, mutable, allows duplicates
# Syntax: [element1, element2, element3]

fruits = ["apple", "banana", "cherry"]
print(fruits)                # ['apple', 'banana', 'cherry']

# Common Operations
fruits.append("orange")      # Add element to end
fruits.insert(1, "mango")    # Insert at specific index
fruits.remove("banana")      # Remove first occurrence
popped = fruits.pop()        # Remove last element
fruits.sort()                # Sort ascending
fruits.reverse()             # Reverse order
print(fruits)

# Slicing
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1:4])          # [2, 3, 4]
print(numbers[::-1])         # Reversed list

# Use Cases:
# ✅ Storing multiple items in order
# ✅ When frequent insertions/deletions are needed


# -----------------------------
# 2️⃣ TUPLES
# -----------------------------
# Ordered, immutable, allows duplicates
# Syntax: (element1, element2, element3)

coordinates = (10, 20, 30)
print(coordinates[0])        # 10

# Tuple Unpacking
x, y, z = coordinates
print(x, y, z)

# Single element tuple needs a comma
single = (5,)
print(type(single))          # <class 'tuple'>

# Use Cases:
# ✅ Fixed data (e.g., coordinates)
# ✅ As dictionary keys (since immutable)


# -----------------------------
# 3️⃣ SETS
# -----------------------------
# Unordered, mutable, no duplicates
# Syntax: {element1, element2, element3}

unique_numbers = {1, 2, 3, 3, 2, 1}
print(unique_numbers)        # {1, 2, 3}

# Common Operations
unique_numbers.add(4)
unique_numbers.remove(2)
unique_numbers.discard(10)   # Doesn’t raise error if not found

# Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))            # {1,2,3,4,5,6}
print(A.intersection(B))     # {3,4}
print(A.difference(B))       # {1,2}

# Use Cases:
# ✅ Removing duplicates
# ✅ Mathematical operations (union, intersection)


# -----------------------------
# 4️⃣ DICTIONARIES
# -----------------------------
# Key-value pairs, mutable, unordered (Python 3.7+ keeps insertion order)
# Syntax: {key: value, key2: value2}

student = {
    "name": "Yash",
    "age": 21,
    "college": "IIT Delhi"
}
print(student["name"])       # Access value
student["age"] = 22          # Update value
student["branch"] = "B.Tech" # Add new key
del student["college"]       # Delete key

# Methods
print(student.keys())        # dict_keys(['name', 'age', 'branch'])
print(student.values())      # dict_values([...])
print(student.items())       # dict_items([...])
print(student.get("age"))    # Safer access than []

# Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print(squares)

# Use Cases:
# ✅ Mapping relationships (e.g., name → score)
# ✅ Fast lookups


# -----------------------------
# 5️⃣ ARRAYS (from array module)
# -----------------------------
# More memory-efficient for numerical data
# Syntax: array(typecode, [elements])

from array import array

nums = array('i', [1, 2, 3, 4, 5])  # 'i' means signed integer
nums.append(6)
nums.remove(2)
print(nums)                         # array('i', [1,3,4,5,6])

# Iterate
for n in nums:
    print(n, end=" ")

# Use Cases:
# ✅ Numerical operations (when using standard library only)
# ✅ When memory efficiency matters
# (NumPy arrays are preferred for data science tasks)


# -----------------------------
# 6️⃣ STRINGS (behave like sequences)
# -----------------------------
# Immutable, ordered, iterable

text = "Python"
print(text[0])             # 'P'
print(text[1:4])           # 'yth'
print(text[::-1])          # 'nohtyP'

# Common Methods
print(text.lower())        # 'python'
print(text.upper())        # 'PYTHON'
print(text.replace("Py", "My"))  # 'Mython'
print(" ".join(["Learn", "Python"]))  # 'Learn Python'

# Use Cases:
# ✅ Text processing, parsing, formatting
# ✅ Building user interfaces or output


# -----------------------------
# 7️⃣ LIST COMPREHENSIONS
# -----------------------------
# Short syntax for creating lists

squares = [x**2 for x in range(1, 6)]
print(squares)  # [1,4,9,16,25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)   # [0,2,4,6,8]

# Nested example
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)

# Use Cases:
# ✅ Compact loops
# ✅ Quick transformations of data
