# {key_expression: value_expression for item in iterable if condition}

# Example 1 > Number > Square

square_dict = {x:x**2 for x in range(1,11)}
print(square_dict)

# ✅ Example 2: Filter dictionary

dict = {"Shubham": 78,"jilani": 93,"harsh": 89,"kunj": 84}
passed = {k:v for k,v in dict.items() if v >= 80}
print(passed,dict)