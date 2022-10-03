# Starting with the list of the previous exercise,
# write Python statements to do the following:
# Append “apple” and 76 to the list.
# Insert the value “cat” at position 3.
# Insert the value 99 at the start of the list.
# Find the index of “hello”.
# Count the number of 76s in the list.
# Remove the first occurrence of 76 from the list.
# Remove True from the list using pop and index.

list1 = [76, 92.3, 'hello', True, 4, 76]
list1.append('apple')
list1.append(76)
list1.insert(3, 'cat')
list1.insert(0, 99)
print(list1.index('hello'))
print(list1.count(76))
list1.remove(76)
list1.pop(list1.index(True))
print(list1)