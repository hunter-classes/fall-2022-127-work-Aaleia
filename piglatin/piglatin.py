def bondify(name):
    result = ""
    space = name.find(" ")
    first = name[0].upper() + name[1:space]
    last = name[space+1].upper() + name[space+2:]
    result = last + ", " + first + " " + last
    return result
print(bondify("james bond"))

def piglatinify(word):
    if word[-1] in ".,!?:;-" :
        if word[0].isupper() :
            if word[0] in "AEIOU" :
                result = word[0:-1] + "yay" + word[-1]
            else:
                result = word[1].upper() + word[2:-1] + word[0].lower() + "ay" + word[-1]
        if word[0].islower() :
            if word[0] in "aeiou" :
                result = word[0:-1] + "yay" + word[-1]
            else:
                result = word[1:-1] + word[0] + "ay" + word[-1]
    else:
        if word[0].isupper() :
            if word[0] in "AEIOU" :
                result = word + "yay"
            else:
                result = word[1].upper() + word[2:] + word[0].lower() + "ay"
        if word[0].islower() :
            if word[0] in "aeiou" :
                result = word + "yay"
            else:
                result = word[1:] + word[0] + "ay"
    return result

test_word = "able"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "cable"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Able"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Cable"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "able."
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "cable!"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Able-"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Cable;"
result = piglatinify(test_word)
print(test_word," -> ",result)