def initialize(name):
    result = ""
    first = name[0]
    first = first.upper()
    result = result + first + "."
    space = name.find(' ')
    last = name[space+1:].capitalize()
    result = result + ' ' + last
    return result

print(initialize("james bond"))