#1: findLargest(l) which takes in a list of numbers and returns the
#   value of the smallest number

def findlargest(lst):

    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num

    return smallest

list1 = [45,6,78,12,789,14]
result = findlargest(list1)
print('1:',list1,'-->',result)

#2: freq(l,v) which takes a list of numbers (l) and a value (v).
#   The function will return the frequency of v, that is, the number of
#   times that v appears in l.

 def freq(l,v):
    frequency = 0
    for num in l:
        if num == v:
            frequency = frequency + 1
    return frequency

list2 = [7,5,6,4,7,8,5,6,7]
value = 7
result = (freq(list2,value))
print('2: # of',value,'in',list2,'-->',result)