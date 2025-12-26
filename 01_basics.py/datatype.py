"""
    mutable > can be change
        > ex : list , set , dictionary , Bytearray , array
    
    unmutable > cant be change
        > ex : integers,floating-point numbers , boolean , strings , tuples , frozen set , bytes

    data types 
    
        > Number 
        > String
        > List
        > Tuple
        > Dictionary
        > Set
        > File
        > Boolean
        > None 
        > functions , modules , classes
        
        > advance : decorator , Generators , iterators 
        
"""

# x = 10
# y = x

# x = 15
# # print(x)
# # print(y)

# username = "shubham@1234"
# print(username)

# myList = [123,"chai",3.14]
# print(len(myList))

# myDict = {"name":"shubham" , "age":21 , "gender" : "male"}
# print(myDict["name"])

# myTuple = (1,2,3,4)
# print(myTuple[1])
# print(myTuple[3])

# a=5
# b=2

# a=a+2
# print(a)

# myListOne = [1,2,3]
# myListTwo = myListOne

# myListOne[0] = 5
# print(myListOne , myListTwo)

# l1 = [1,2,3]
# l2 = l1[:]
# print(l1,l2)
# l1[1] = 20
# print(l1,l2)

l1 = [1,2,3]
l2 = l1

print(l1==l2)
l2 = [1,2,3]
print(l1 is l2)

