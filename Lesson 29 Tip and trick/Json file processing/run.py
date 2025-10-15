import json

dict = {
    "name": "Huong",
    "age": 21,
    "hobbies": ["sleeping", "eating"]
}

print(type(dict))
print(dict)
# convert python dict to json string
json_string = json.dumps(dict)
print(type(json_string))
print(json_string)

# convert json string to python
new_dict = json.loads(json_string)
print(type(new_dict))
print(new_dict)

assert dict == new_dict
print("Okk")

# record python object to file .json
# with open("save.json", "w") as f: # w là phương thức để ghi vào
#     json.dump(dict, f, indent=4)
    
# read json file to python object
with open("save.json") as f:
    my_content = json.load(f)
print(my_content)