'''Extras:
1. Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.
2. Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.
'''

import random

name = ["Oblivian", "Grizelda", "Legolas", "Augustus", "Misery"]
noun = ["legend", "four-slot toaster", "psychic", "crime against humanity", "seven-string guitar"]
verb = ["shred", "buy", "patrol", "expose", "operate"]
adjective = ["green","devilish", "fluffy", "sacred", "domesticated"]
adverb = ["quickly","obscenely","foolishly", "viscerally", "violently"]

file = open("data.dat")
story = file.read().split()

def madlib(story):
  final = []
  for word in story:
    if word == '<NAME>':
      word = word.replace("<NAME>",random.choice(name))
    final = final + [word.replace('<NOUN>', random.choice(noun)).replace("<VERB>", random.choice(verb)).replace("<ADJ>", random.choice(adjective)).replace("<ADVERB>", random.choice(adverb))]
    final_result = " ".join(final)
  return final_result

print(madlib(story))