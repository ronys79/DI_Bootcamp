# import json
# import random

# def get_words_from_file():
#     with open("infile.txt", 'r') as f1:
#         variable = f1.readlines()
#         return variable

# def get_random_sentence(length):
#     variable2 = get_words_from_file()
#     variable3 = random.sample(variable2, length)
#     variable4 = (' '.join(variable3)).lower()
#     return variable4

# def main():
#     print("Create random sentece generator")
#     variable5 = int(input("How long do you want youer sentence to be, has to be between 2 - 20 numbers?"))
#     while 2 <= variable5 <= 20:
#         print("number is too smal or to big try again")
#         variable5 = int(input("How long do you want youer sentence to be, has to be between 2 - 20 numbers?"))
#     # print(get_words_from_file())
#     print(get_random_sentence(variable5))
#         # text = get_words_from_file()
#         # print(get_random_sentence(text))

# main()

# import json

# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# answers = json.loads(sampleJson)


# print(answers["company"]["employee"]["payable"]['salary'])
# answers['company']['employee']['birth_date']= "23/07/1979"

# with open("xp_2.json", "w") as f:
#     json.dump(answers, f)

