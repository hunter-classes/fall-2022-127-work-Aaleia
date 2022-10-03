# Write a function called average that takes a list of numbers
# as a parameter and returns the average of the numbers.

def average(list):
    total = 0
    for i in list:
        total = total + i
    return total / len(list)

print(average([1,3,5]))

# Write a function sum_of_squares(xs) that computes the sum of 
# the squares of the numbers in the list xs. For example, 
# sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29.

def sum_of_squares(compute):
    total = 0
    for num in compute:
        num = num ** 2
        total = num + total
    return total

print(sum_of_squares([2,4,3]))