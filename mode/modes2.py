import random

def buildRandomList(size,maxvalue):
  result = []
  for x in range(size):
    result.append(random.randrange(maxvalue))
  return result

# OR

def buldRandomList(size,maxvalue):
  result = [random.randrange(maxvalue) for x in range(size)]
  return result



def freq(l,v):
  frequency = 0
  for num in l:
    if num == v:
      frequency = frequency + 1
  return frequency

dataset = [7,5,6,4,7,8,5,6,7]
   
# OR use list comprehensions

def freq(dataset,v):
  result = len([x for x in dataset if x==7])
  return result

def findLargest(lst):
  largest = lst[0]
  for num in lst:
    if num < largest:
      largest = num

    return largest