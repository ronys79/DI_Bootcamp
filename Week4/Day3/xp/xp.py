# Exercise 1 : Convert Lists Into Dictionaries

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# answer_1= dict(zip(keys, values))
# print(answer_1)

# Exercise 2 : Cinemax #2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# price = 0

# for age, name in family.items():
#     if age <= 3 :
#         price = 0
#         print(f'{name} pays {price}$')
#     elif age => 3 and age =< 12:
#         price += 10
#         print(f'{name} pays {price}$')
#     elif  age >= 12:
#         price += 15
#         print(f'{name} pays {price}$')
# print(f'The family pays {price}$')

# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

# brand = {
#     "name": "Zara", 
#     "creation_date": 1975, 
#     "creator_name": "Amancio Ortega Gaona", 
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_store": 7000,
#     "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}
#     }
# brand["number_store"] = 2

# for client in brand['type_of_clothes']:
#     print(f"the type of clients are {client}")
# # 5. Add a key called country_creation with a value of Spain.
# brand["country_creation"] = 'Spain'
# print (brand)
# # 6. Check if the key international_competitors is in the dictionary. If it is, add the store .

# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")
#     print(brand)
# else:
#     print("not in dictionary")

# 7. Delete the information about the date of creation.

# del brand['creation_date']
# print(brand)

# 8. Print the last international competitor.

# last_competitor = brand['international_competitors'][-1]
# print(last_competitor)

# 9. Print the major clothes colors in the US.

# print(f"the major clothes' colors in the US are {brand['major_color']['US']}")

# 10. Print the amount of key value pairs (ie. length of the dictionary).
# print(len(brand))
# 11. Print the keys of the dictionary.
# print(brand.keys())
# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000

# more_on_zara = {
# 'creation_date' : 1975,
# 'number_stores': 10000
# }

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# brand.update(more_on_zara)
# print(brand)
# 14. Print the value of the key number_stores. What just happened ?

# print(brand['number_stores'])

# we overwrote the 2 stores appended since it existed on the list already

# Exercise 4 : Disney Characters
# Instructions
# Use this list :


# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

# disney_user_a = {users[i]:i for i in range(0,len(users))}
# print(disney_user_a)

# disney_user_b = dict(enumerate(users))
# print(disney_user_b)

# users = sorted(users)
# disney_user_c = {users[i]:i for i in range(0,len(users))}
# print(disney_user_c)

# for i_characters in users:
#     if 'i' in i_characters:
#         print(i_characters)

# disney_user_e = {users[i]:i for i in range(0,len(users)) if 'M' or 'P' in users[i][0]}
# print(disney_user_e)

# for name in users:
# 	if name[0] in ["M", "P"]:
# 		print(name)

# for mp_characters in users:
#     if 'M' or 'P' in mp_characters[0]:
#         print(mp_characters)

