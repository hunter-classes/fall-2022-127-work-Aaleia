## 1. Write a function to find the smallest value in a listKfind smallest in a list of items

def smallest(i):
    smallest = min(i)
    return smallest

list1 = [1,2,3,4,5]
result = smallest(list1)
print("#1: ",list1, "->", result)
    
## 2. Write a function that returns a new list that contains all the odd items in the original list

def odditems(l):
    odd = []
    for i in list:
        if i % 2 != 0:
            odd.append(i)
    return odd

list2 = [1,2,3,4,5]
result = odd(list2)
print("#2: ",list2, "->",result)

## 3. Write a function that takes a string and returns a new string where all the words are capitalized
    
def capitalize(sentence):
    result_list = []
    for word in sentence.split():
        cap_word = word.capitalize()
        result_list.append(cap_word)
    result = ""
    result = " ".join(result_list)
    return result

sentence3 = "this is a string"
result = capitalize(sentence3)
print("#3. ",sentence3, "->",result)

## 4. Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case

def uppercase(string):
    str1 = []
    for word in string.split():
        if len(word) > 5:
            upper_word = word.upper()
            str1.append(upper_word)        
    result = " "
    result = " ".join(str1)
    return result

sentence4 = "this is a new string"
result = uppercase(sentence4)
print("#4. ",sentence4, "->",result)

## 5. Write a function that takes a list of numbers and returns a new
# list with each item squared

def squared(list):
    new = []
    for num in list:
        new.append(num**2)
    return new

list5 = [2,3,4]
result = squared(list5)
print("#5. ", list5, "->", result)

## 6. Write a function that takes two lists of numbers and returns a new
# list where each item is the corresponding values of the original
# lists added together. Ex [1,2,3] and [10,20,30] would return the
# list [11,22,33]

def addtogether(l1, l2):
    new = []
    for i in range(len(l1)):
        a = l1[i] + l2[i]
        new.append(a)
    return new

l1 = [1,2,3]
l2 = [4,5,6]
result = addtogether(l1, l2)
print("#6. ",l1, l2, "->", result)

## 10. Count how many words in a list have length 5

def countWords(list):
    word = 0
    for w in list:
        if len(w) == 5:
            word = word + 1
    return word

words = ["hello", "goodbye", "see", "you", "later"]
result = countWords(words)
print("#10. ",words, "->", result)