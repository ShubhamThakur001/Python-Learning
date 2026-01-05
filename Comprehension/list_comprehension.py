# [expression for item in iterable if condition]

# Square number
# Print square of 1 to 10

square_list = [x**2 for x in range(1,11)]
print(square_list)

# ✅ Example 2: Filter even numbers

even_list = [x for x in range(1,11) if x%2==0]
print(even_list)

# Example 3 : Filter odd numbers

odd_list = [x for x in range(1,11) if x%2==1]
print(odd_list)

"""
# normal way
result = []
for x in range(5):
    result.append(x)

# comprehension
result = [x for x in range(5)]

"""

"""

📌 Quick Summary
Type	                Output
List Comprehension	    []
Dict Comprehension	    {key: value}
Set Comprehension	    {}
String	join() + list comp

"""
