# menu = [
#     {
#         'name': 'Soup',
#         'price': 10,
#         'spice_level': 'B',
#         'gluten_index': False
#     },
#     {
#         'name': 'Hamburger',
#         'price': 15,
#         'spice_level': 'A',
#         'gluten_index': True
#     },
#     {
#         'name': 'Salad',
#         'price': 18,
#         'spice_level': 'A',
#         'gluten_index': False
#     },
#     {
#         'name': 'French fries',
#         'price': 5,
#         'spice_level': 'C',
#         'gluten_index': False
#     },
#     {
#         'name': 'Beef bourguignon',
#         'price': 25,
#         'spice_level': 'B',
#         'gluten_index': True
#     },
# ]
# class MenuManager:
#     def __init__(self, menu):
#         self.menu = menu
#     def add_item(self, **new_item):
#         self.menu.append(new_item)
#     def update_item(self, **item_to_update):
#         for item in self.menu:
#             if item_to_update['name'] == item['name']:
#                 item['price'] = item_to_update['price']
#                 item['spice_level'] = item_to_update['spice_level']
#                 item['gluten_index'] = item_to_update['gluten_index']
#                 return
#         print('The item you want to update does not exist.')
#     def display_menu(self):
#         for item in self.menu:
#             print(f'{self.menu.index(item) + 1}: {item}')

#     def remove_item(self, **remove_item):
#         for item in self.menu:
#             if remove_item['name'] == item['name']:
#                 self.menu.remove(item)
#                 print(f'{self.menu.index(item) + 1}: {item}')
#                 return
#             else:
#                 print(f'{item} not in the menu')
# m1 = MenuManager(menu)

# remove_item(Soup)


# # Create a method called remove_item(name). 
# # This method should check if the dish is in the menu, if the dish exists then delete it 
# # and print the updated dictionary. If not notify the manager that the dish is not in the menu.

# Exercise 1 : Call History
# Instructions
# Create a class called Phone. This class takes a parameter called phone_number. 
# When instantiating an object create an attribute called call_history which value is 
# an empty list.

# class Phone:
#     def __init__(self, phone_number):
#         self.phone_number = phone_number
#         self.call_history = []
#         self.message = []

# # Add a method called call that takes both self and other_phone 
# # (i.e another Phone object) as parameters. The method should print a string stating 
# # who called who, and add this string to the phone’s call_history.

#     def call(self, other_phone):
#         call_string = f 'self.phone_number  was called by {other_phone}
#         pass

# # Add a method called show_call_history. This method should print the call_history.

#     def show_call_history:
#         for line in self.call_history:
#         print(line)

# # Create a method called send_message which is similar to the call method. 
# # Each message should be saved as a dictionary with the following keys:
# # to
# # from
# # content

#     def send_message(self, msg_txt, msg_sender):
#         msg_string = self.message.append({'TO': msg_sender, 'FROM': self, 'CONTENT': msg_txt})

# # Create the following methods: show_outgoing_messages(self), 
# # show_incoming_messages(self), show_messages_from(self, number)

# class Phone:
#     def __init__(self, phone_number, full_name):
#         self.phone_number = phone_number
#         self.full_name = full_name
#         self.call_history = []
#         self.messages = []
#         self.contacts = []
#     def call(self, other_phone_number, caller):
#         if caller:
#             for contact in self.contacts:
#                 if contact['phone_number'] == other_phone_number:
#                     call_info = f'{self.full_name} called {contact["full_name"]}'
#                     self.call_history.append(call_info)
#                     print(call_info)
#                     return
#             call_info = f'{self.full_name} called {other_phone_number}'
#             self.call_history.append(call_info)
#             print(call_info)
#         else:
#             for contact in self.contacts:
#                 if contact['phone_number'] == other_phone_number:
#                     call_info = f'{contact["full_name"]} called {self.full_name}'
#                     self.call_history.append(call_info)
#                     print(call_info)
#                     return
#             call_info = f'{other_phone_number} called {self.full_name}'
#             self.call_history.append(call_info)
#             print(call_info)
#     def show_call_history(self):
#         for call in self.call_history:
#             print(f'{self.call_history.index(call) + 1}: {call}')
#     def send_message(self, **message_info):
#         self.messages.append(message_info)
#     def show_messages(self):
#         for message in self.messages:
#             print(f'{self.messages.index(message) + 1}: {message}')
#     def show_outgoing_messages(self):
#         counter = 1
#         for message in self.messages:
#             if message['sent_from'] == self.phone_number:
#                 print(f'{counter}: {message}')
#                 counter += 1
#     def show_incoming_messages(self):
#         counter = 1
#         for message in self.messages:
#             if message['to'] == self.phone_number:
#                 print(f'{counter}: {message}')
#                 counter += 1
#     def add_contact(self, **contact_info):
#         self.contacts.append(contact_info)
#     def __repr__(self):
#         return self.phone_number
# p1 = Phone('123456789', 'chaim wiesner')


class Farm:
    def __init__(self, farm_name, animals={}):
        self.farm_name = farm_name
        self.animals = animals

    def add_animal(self, new_animal, quantity = 1):
        if new_animal in self.animals:
            self.animals[new_animal] += quantity
        else:
            self.animals[new_animal] = quantity

    def get_info(self):
        output = f'\n{self.farm_name}\'s farm\n\n'
        for key, val in self.animals.items():
            output += f'{key} : {val}\n'
        output += f'\n     E-I-E-I-0!\n'
        return output

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())


# 5. Test your code and make sure you get the same results as the example above.

# 6. Bonus: nicely line the text in columns as seen in the example above. Use string formatting.