# [true_expr if condition else false_expr for item in iterable]

# result = {k: "Even" if k % 2 == 0 else "Odd" for k in range(11)}
# print(result)

# 🔹 Dictionary comprehension syntax
# {key: value_if_true if condition else value_if_false for item in iterable}

# result = ["Even" if x % 2 == 0 else "Odd" for x in range(1,11)]
# print(result)

users = [
    {"name":"shubham","active":True,"age":21},
    {"name":"shubh","active":True,"age":23},
    {"name":"jilani","active":False,"age":25},
    {"name":"harsh","active":True,"age":29},
    {"name":"kunj","active":False,"age":31},
]

result = [u["name"] for u in users if u["age"]> 25]
print(result)



"""
📌 Quick Summary
Type	            Output
List Comprehension	[]
Dict Comprehension	{key: value}
Set Comprehension	{}
String	join() + list comp

"""