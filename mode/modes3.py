import random

def buldRandomList(size,maxvalue):
  result = [random.randrange(maxvalue) for x in range(size)]
  return result

def mode(dataset):
  # f = list.count(v)
  maxvalue = max(dataset)
  for v in dataset:
    frequency = len([x for x in dataset])
  mode = [freq in dataset if freq == maxvalue]

def mode(dataset):
  modesofar = dataset[0]
  freqsofar = freq(dataset,modesofar)
  for item in dataset [1:]:
    if freq(dataset,item) > freqsofar:
      modesofar = item
      freqsofar = freq(dataset,item)

def testMode(size,maxvalue):
  datset = buildRandomList(size,maxvalue)
  # print(dataset)
  m = mode(dataset)
  print(m)