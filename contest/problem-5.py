'''
5. Tuples

● Problem: "Coordinates Translator"

○ Description: A program is given a tuple representing (x, y) coordinates (e.g.,
(10, 5)). You need to unpack the tuple into two separate variables, x_coord
and y_coord. Then, create a new tuple where the coordinates are swapped to
(y, x) and print the new tuple.
○ Input Example: point = (15, 22)
○ Expected Output: (22, 15)
'''

co_ord = eval(input("Enter as tuple:")) #using int will return it as a string

x_coord, y_coord = co_ord
# print(x_coord)
# print(y_coord)

(y,x) = (x_coord,y_coord)

print((x,y))