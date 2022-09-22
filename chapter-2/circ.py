## Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.

pi = 3.14
radius = input("Enter the radius of the circle.")
radius_int = int(radius)

area = (pi * (radius_int**2))

print ("The area of a circle with a radius of", radius, "is", area)