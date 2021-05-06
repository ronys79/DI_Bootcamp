# Create a folder with two files : index.py and file.json. Save this code into the json file
# not sure below:
import json

json_file = "file.json"

with open(json_file, 'w') as file_obj:
    json.dump(data, file_obj)

data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

with open('secret.json', 'r') as f:
    family = json.load(f)
for child in family['children']:
    print(f'{family["firstName"]}\'s child {child["firstName"]} is {child["age"]} years old')
    child['favorite_color'] = random.choice(['blue','yellow','green'])
with open('secret.json', 'w') as f:
    json.dump(family, f,indent=2)
print(family)


# Avi's examples to learn done in class
# import json 
# def read_from_secrets():
#     with open('secret.json', 'r') as file_obj:
#         data = json.load(file_obj)
#     return data
# def add_to_secret(data):
#     old_data = read_from_secrets()
# def add_item_to_menu(name,price):
#     menu.append({'name':name, 'price': price })
# def write_to_secrets(data):
#     with open('secret.json', 'w') as file_obj:
#         json.dump(data, file_obj, indent = 2,)
# try:
#     menu = read_from_secrets()
# except json.decoder.JSONDecodeError:
#     menu = []
# while True:
#     name = input('what item would you like to add?')
#     if name == 'quit':
#         break
#     price = input(f'how much does {name} cost?')
#     add_item_to_menu(name,price)
# print(menu)
# write_to_secrets(menu)