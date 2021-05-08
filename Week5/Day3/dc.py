

Other abilities of a Circle instance:


    # Compute the circle’s area
    # Print the circle and get something nice
    # Be able to add two circles together
    # Be able to compare two circles to see which is bigger
    # Be able to compare two circles and see if there are equal

# from math import pi

# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#         self.diameter = radius * 2    

#     def area(self):
#         return pi * self.radius**2

#     def __repr__(self):
#         something_nice = f"Circle with radius = {self.radius}."
#         return something_nice
    
#     def __add__(self, other):
#         if isinstance(other, Circle):
#             return other.diameter + self.diameter
    
#     def __eq__(self, other):
#         if isinstance(other, Circle):
#             return other.diameter == self.diameter

#     def __eq__(self, other):
#             if isinstance(other, SimpleCircle):
#                 return other.diameter == self.diameter


    # Be able to put them in a list and sort them

# after tis point i ams stuck, not sure how to use the decorators for this

# from avi day after:
# @staticmethod
#     def sort_circles(circle_list):
#         circle_list = list(filter(lambda a:isinstance(a, Circle), circle_list))
#         circle_list.sort(key=lambda x:x.area)
#         return circle_list