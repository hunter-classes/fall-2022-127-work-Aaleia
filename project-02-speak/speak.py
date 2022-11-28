'''
Extras:
1. Store translations in a file named pirate.dat. The file should have lines in the form “word:translation.”
2. Handle upper and lower case.
'''

input1 = open('input.txt').read()
split = input1.split()

# Build a translation dictionary from data.dat
data = open('pirate.dat').read()
dictionary = dict(x.split(':') for x in data.split('\n'))

def pirate(split):
  i = []
  for item in split:
    # Allow for translation even if the original word is capitalized
    if item[0].isupper() == True:
      item = item.lower()
      if item in dictionary.keys():
        i.append(dictionary[item])
      else:
        i.append(item[0].upper() + item[1:])
    else:
      if item in dictionary.keys():
        i.append(dictionary[item])
      else:
        i.append(item)
  result = " ".join(i)
  
  # Capitalize the first letter of every sentence
  sentences = result.split('. ')
  capitalize = []
  for sent in sentences:
    capitalized = sent[0].upper() + sent[1:]
    capitalize.append(capitalized)
  result = ". ".join(capitalize)
  
  return result

print("Original:", input1,"\n")
print("Pirate Translation:", pirate(split))