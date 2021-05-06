# Download this text file http://www.practicepython.org/assets/nameslist.txt and do the following steps

# Read the file line by line

# file1 = open('practice.txt', 'r')
# line = file1.read

# for line in file1:
#     print(line)

# Read only the 5th line of the file
# file2 = open('practice.txt', 'r')
# line = file2.readline(5)
# print(line)

# # Read all the file and return it as a list of strings. 
# Then split each word

# practice = 'practice.txt'
# with open(practice) as f1:
#     for line in f1:
#         row = line.split(",")
#         print(line)

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# file1 = open('practice.txt', 'r')
# line = file1.read()
# darth = line.count("Darth")
# luke = line.count("Luke")
# lea = line.count("Lea")
# print('Number of occurrences of Darth:', darth, "and Lea: ", lea, "and Luke:", luke)
# file1.close()

# Append your first name at the end of the file

# Open a file with access mode 'a'
# practice = open('practice.txt', 'a+')
# # Append 'hello' at the end of file
# practice.write('Rony')
# print(practice)
# Close the file

# Open the file in append & read mode ('a+')
# with open("practice.txt", "a+") as practice:
#     # Move read cursor to the start of file.
#     practice.seek(0)
#     # If file is not empty then append '\n'
#     data = practice.read(100)
#     if len(data) > 0 :
#         practice.write("\n")
#     # Append text at the end of file
#     practice.write("Rony")

# Append "SkyWalker" next to each first name "Luke"
# with open("practice.txt", "a+") as practice:
#     for line in practice:

# practice = open('practice.txt', 'a+')
# for i in practice:
#     if i == "Luke" :
# f.close()

# with open("practice.txt", "a+") as practice:
#     for luke in practice:
#         new_string = luke.replace("Luke", "Luke Skywalker")
#         new_strings.append(new_string)
#         print(new_strings)

# practice = ('practice.txt')

# with open("practice.txt") as f1:
#     for line in f1:
#         if line.startswith("Luke"):
#             line.replace('Luke", "Luke Skywalker")
#         print(line)