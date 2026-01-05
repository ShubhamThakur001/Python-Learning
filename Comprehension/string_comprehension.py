# "".join([expression for char in string if condition])

# ✅ Example 1: Remove vowels

# text = "shubham"
# result = "".join([char for char in text if char not in "aeiou"])
# print(result)

# ✅ Example 2: Uppercase letters only

# text = "SHUbhaM"
# result = "".join([char for char in text if char.isupper()])
# print(result)

# Set comprehension

# Used when you want unique values.
unique_set = {1,2,3,4,1,2,3,5,6,7,1,2}
unique_squares = {x**2 for x in unique_set}
print(unique_squares)
print(type(unique_squares) , type(unique_set))