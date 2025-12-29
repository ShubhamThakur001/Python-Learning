"""
Docstring for 03_loops.while_loop

    while condition:
        #some work
    
    Break : used to terminate the loop when encountered 
    
    Continue : terminates execution in the currect iteration and conditions of the loop with the next iteration 
"""

# count = 1

# while count <= 10:
#     print(count , end=" ")
#     count+=1
    



# Questions

"""
print numbers from 1 to 100

number = 1

while number < 101:
    print(number)
    number += 1

"""

"""
print numbers from 100 to 1  

number = 100

while number > 0:
    print(number)
    number -= 1
    
"""

"""
print the multipication table of a number n

n = 10
count = 1
while count < 11:
    print(n, "*" ,count ,"=" , n*count)
    count +=1
    
"""

"""
print the elements of the following list using a loop
    [1,4,9,16,25,36,49,64,81,100]

list = []
count = 1

while count < 11 :
    n = count * count
    list.append(n)
    count += 1
    
print(list)

"""

"""
search for a number x in this tople using loop

my_tuple = (1,4,9,16,25,36,49,64,81,100)
x=25
i=len(my_tuple)-1
while i >= 0:
    if my_tuple[i] == x:
        print("Found")
        break
    i -= 1
"""
