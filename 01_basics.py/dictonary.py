"""
    Dictonary in python
        > {"key":"value"}
"""

person_dict = {
    "name":"shubham",
    "age":21,
    "address_city":"vadodara",
    "address_state":"gujarat"
}

# print(person_dict.get("name"))
# person_dict["address"]="mumbai"
# print(person_dict)

# for detail in person_dict:
#     print(detail,person_dict[detail],end=", ")
    
# for key,value in person_dict.items():
#     print(key,value)
    
# if "name" in person_dict:
#     print("name is present")

# person_dict["email"]="xyz@gmail.com"
# print(len(person_dict))

# person_dict.pop("name")
# person_dict.popitem()
# print(person_dict)

# del person_dict["age"]
# print(person_dict)


# person_dict_copy = person_dict.copy()

# print(person_dict_copy) 

person_details = {
    "personal_info":{
        "name":"shubham",
        "age":21,
        "gender":"male"  
    },
    "address":{
        "city":"vadodara",
        "state":"gujarat",
        "zipcode":390014,
    },
    "contact_details":{
        "phone_number":"1234567890",
        "email":"abc@gmail.com"
    }
}

# print(person_details["personal_info"]["name"])

# for key,value in person_details.items():
#     print(key,value)
    
# squared_num = {x:x**2 for x in range(6)}
# print(squared_num)
# print(squared_num.clear())

# keys = ["shubham","jilani","harsh"]
# gender = "male"

# new_dict = dict.fromkeys(keys,gender)
# print(new_dict)
# new_dict = dict.fromkeys(keys,keys)
# print(new_dict)

