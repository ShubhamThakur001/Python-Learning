# list[array] in python 

list_name = ["shubham","jilani","harsh","kunj","dhruv"]
# print(list_name)
# print(list_name[3])
# list_name[2] = "manthan"
# print(list_name)

# print(len(list_name))

# for name in list_name:
#     print(name , end=" ")
    
# if "ovesh" in list_name:
#     print("have ovesh in name list")
# else:
#     list_name.append("ovesh")
#     print("ovesh is added to name list")
    
# print(list_name)
# list_name.pop()
# list_name.remove("jilani")
# list_name.insert(1,"hitesh")   
# print(list_name)

# list_name_copy = list_name.copy()
# list_name_copy.pop()
# print(list_name)
# print(list_name_copy)

squared_num = [x**2 for x in range(10)]
print(squared_num)

even_num = [x for x in range(11) if x%2==0]
print(even_num)

odd_num = [x for x in range(11) if x%2==1]
print(odd_num)