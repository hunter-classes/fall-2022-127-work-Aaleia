def mode(dataset):
  # f = list.count(v)
  maxvalue = max(dataset)
  for v in dataset:
    frequency = len([x for x in dataset])
  mode = [freq in dataset if freq == maxvalue]

dataset = [1,2,3,4,3,4,5,2,3]

def mode(dataset):
  modesofar = dataset[0]
  freqsofar = freq(dataset,modesofar)
  for item in dataset [1:]:
    if freq(dataset,item) > freqsofar:
      modesofar = item
      freqsofar = freq(dataset,item)