def bondify(name):
    result = ""
    space = name.find(" ")
    first = name[0].upper() + name[1:space]
    last = name[space+1].upper() + name[space+2:]
    result = last + ", " + first + " " + last
    return result
print(bondify("james bond"))

def piglatin(word):
    if word[0] in "a,e,i,o,u" :
        return word + "yay"
    else:
        return word [1:] + word[0] + "ay" 

result = piglatin("create")
print(result)
result = piglatin("bond")
print(result)