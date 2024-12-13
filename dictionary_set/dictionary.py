info = {
    "name" : "Shaidul islam",
    "age" : 25,
    "city" : "Dhaka",
    "country" : "Bangladesh",
    "phone" : "01712345678",
    "email" : "shaidulislam@gmail.com",
    "is_adult": True,
    "subject" : ['Math', 'Science', 'English', 'Bangla', 'History'],
    "address" : {
        "street" : "Dhanmondi",
        "apartment" : "House # 12",
        "floor" : 5,
        "flat" : 101
        }
}

#print(info['subject'][1])
#print(info['address']['street'])

info["name"] = "Shohan"
info["sername"] = "Khan"

#print(info)
# print(len(info))
# info.keys()
# print(info.keys())
# create_list = list(info.keys())
# print(create_list)
# print(len(create_list))
# create_tuple = tuple(info.keys())
# print(create_tuple)

# print(info.values())
# print(list(info.values()))

# list_cast = list(info.items())
# print(list(list_cast[1]))

# print(info.get('name'))

new_dict = {
    "result" : {
        "math" : 56,
        "science" : 78,
        "english": 45,
        "bangla" : 90,
        "Python" : 89
    }
}

info.update(new_dict)
print(info)


# null_dict = {}

# print(null_dict)
# null_dict["name"] = "Nihal"
# null_dict["sername"] = "Khan"
# null_dict["age"] = 25

# print(null_dict)