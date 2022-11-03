#1: findLargest(l) which takes in a list of numbers and returns the
#   value of the largest number

def findLargest(lst):

    largest = lst[0]
    for num in lst:
        if num < largest:
            largest = num

    return largest

list1 = [45,6,78,12,789,14]
result = findLargest(list1)
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



import datetime
import random

def findLargest(dataset):
    largeSoFar = dataset[0]
    for item in dataset[1:]:
        if item > largeSoFar:
            largeSoFar = item
    return largeSoFar



def freq(dataset,v):
    # since this loops over the
    # entire data set once
    # it takes n time 
    #count = 0
    #for item in dataset:
    #    if item == v:
    #        count = count + 1
    #return count
    return len([x for x in dataset if x == v])

def buildRandomList(size,maxvalue):
    #result = []
    #for x in range(size):
    #    result.append(random.randrange(maxvalue))
    #return result
    result = [random.randrange(maxvalue) for x in range(size)]
    return result 


def mode(dataset):
    """
    Returns a mode of the dataset, that is
    the value that appears most frequently
    if multiple values appear the same # of times and are
    most frequent, return any of them.
    Ex: mode([5,4,5,6,7,8,5,4]) --> 5 since 5 appears the most
    mode([5,5,5,4,4,4,2,2,7,7,8,8,9]) --> return 5 or 4 since
    both of those values appear 3 times which is the most
    Strategy:
    assume the first value is the mode
    we can grab its frequency
    for each remaining item in the dataset:
      count that items frequence and see if it's the new
      mode so far    
    """
    modeSoFar = dataset[0]
    freqSoFar = dataset.count(modeSoFar)
    for item in dataset[1:]: #outer loop -> n
        # calling freq each time is n
        # if freq(dataset,item) > freqSoFar:
        if dataset.count(item) > freqSoFar:
            modeSoFar = item
            freqSoFar = dataset.count(item)
    return modeSoFar



    # assume all values in dataset
    # are between 0 and 99 inclusive
dataset = [random.randrange(100) for i in range(100)]
list = []
for index in range(100):
  list.append(random.randrange(0,100))
def fastMode(dataset):
    # 1. make a list of 100 slots
    # and set them all to 0
    # this will store our tallies
  tallies = [0]*100
    # 2. Loop through our dataset
    # and for each item incremement
    # (add 1) to the appropriate
    # slot in the tallies list
  for i in dataset:
    tallies[i] += 1
    # 3. the index with the highest
    # value in tallies is the mode
    mode = tallies.index(max(tallies))
  return mode

result = fastMode(dataset)
print("Faster mode -->", result)