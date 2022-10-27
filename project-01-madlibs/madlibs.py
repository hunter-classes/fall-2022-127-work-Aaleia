import random

noun = ["person", "squirrel", "villain"]
verb = ["walk", "run", "drive"]

file = open("data.dat")

for x in file:
  x = x.replace("<NOUN>",random.choice(noun))
  x = x.replace("<VERB>",random.choice(verb))
  x = x.replace("<ADJ>",random.choice(adjective))
  x = x.replace("<ADVERB>",random.choice(adverb))

  print(x)