"""
Docstring for Comprehension.nested_comprehension
    Nested comprehension means using one loop inside another loop in a single line.
    It is mainly used for 2D lists (matrices), combinations, and flattening data.
"""
# Normal
# result = []
# for i in range(3):
#     for j in range(3):
#         result.append((i,j))
# print(result)

# nested-comprehension
# result = [(i, j) for i in range(3) for j in range(3)]
# print(result)

# create a 3*3 matrix

# matrix = [[j for j in range(3)] for i in range(3)]
# print(matrix)


matrix = [[1,2],[3,4],[5,6]]
flat = [num for row in matrix for num in row]
print(flat)