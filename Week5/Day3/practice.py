# class Circle:
#     color = "red"

#     def __init__(self, diameter):
#         self.diameter = diameter

#     def grow(self, factor=2):
#         self.diameter = self.diameter * factor

#     def get_color(self):
#        return Circle.color

# circle1 = Circle(2)
# print(circle1.color)
# print(Circle.color)
# print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)

# class Man():
#     sex = "Male"

#     def __init__(self, name):
#         self.name = name

#     @staticmethod
#     def get_nicknames():
#         return ["Bro", "Dude", "Buddy"]

# me = Man( "rony")
# print(Man.get_nicknames()[2])

# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val

#     @classmethod
#     def get_count(cls):
#         return cls.count

# object_1 = MyClass(10)
# print("\nValue of object : %s" % object_1.get_val())
# print(MyClass.get_count())

# object_2 = MyClass(20)
# print("\nValue of object : %s" % object_2.get_val())
# print(MyClass.get_count())

# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = self.filterint(val)
#         MyClass.count += 1

#     @staticmethod
#     def filterint(value):
#         if not isinstance(value, int):
#             print("Entered value is not an INT, value set to 0")
#             return 0
#         else:
#             return value


# a = MyClass('5')
# b = MyClass(10)
# c = MyClass(15)

# print(a.val)
# print(b.val)
# print(c.val)
# print(a.filterint(100))

# class PrintList(object):

#     def __init__(self, my_list):
#         self.mylist = my_list

#     def __repr__(self):
#         return str(self.mylist)


# printlist = PrintList(["a", "b", "c"])
# print(printlist.__repr__())

# from faker import Faker
# fake = Faker()
# print(fake.date())

# from faker import Faker
# fake = Faker()

# def create_file(num):
#     f = open("datefile" + num + ".txt", "w")
#     for _ in range(100):
#         f.write(f"{fake.date()}\n")
#     f.close()
# print(fake.date())


# create_file('1')
# create_file('2')
# print(fake.address())

# import sys
# import typing

# from tabulate import tabulate

# def main(file1, file2):
#     file1_contents = extract_file_contents(file1)
#     file2_contents = extract_file_contents(file2)

#     display_files(file1_contents, file2_contents)

#     dates = sorted(set(file1_contents).union(file2_contents))
#     print(dates[len(dates) // 2])

# def display_files(file1_contents, file2_contents):
#     table = {
#         'file1': file1_contents,
#         'file2': file2_contents
#     }
#     print(tabulate(table))

# def extract_file_contents(file_path: str) -> typing.List[str]:
#     """ 
#     Extract file contents and strip whitespaces from each row.
#     : param file_path: The path to the file to extract
#     : return: A list of date data rows
#     """ 

#     with open(file_path, 'r') as f:
#         file_contents = f.readlines()
#     new_file_contents = []
#     for date_data_record in file_contents:
#         date_data_record = date_data_record.strip()
#         if date_data_record:
#             new_file_contents.append(date_data_record)
#     return new_file_contents

# if __name__ == '__main__':
#     args = sys.argv[1:]
#     if len(args) != 2:
#         print(f"Expected two arguments as files. Got {len(args)} instead.")
#         sys.exit(1)
#     main(*args)

import datetime

today_date = datetime.date.today()
actual_datetime = datetime.datetime.now()
in_15_hours = actual_datetime + datetime.timdelta(hours=15, minutes=10)

print(f"Today is the {today_date.strftime("%d/%m")}")
print(f"In 15 hours and 10 minutes it will be the {in_15_hours.strftime("%d/%m")}")
