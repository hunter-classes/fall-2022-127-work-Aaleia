s = '''this is a string'''

# d['a'] <-- # of occurences of 'a'

# Count the number of times each letter appears in s
def count_letters(s):
  counts = ()
  for letter in s:
    if letter in counts.keys():
      counts[letter] = counts[letter] + 1
    else:
      counts[letter] = 1
  return counts

def count_words(s):
  counts = {}
  for word in s.split():
    if word in counts.keys():
      counts.setdefault(word,0)
      counts[word] = counts[word] + 1

    return counts
      

letter_counts = count_letters(s)
word_counts = count_words(s)
print(count_letters(s))
print(word_counts(s))