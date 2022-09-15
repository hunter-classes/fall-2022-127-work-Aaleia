from test import testEqual

# 7 - Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

def is_even(n):
  if n % 2 == 0:
      return True
  else:
      return False

testEqual(is_even(64), True)
testEqual(is_even(23), False)

print(is_even(32))
print(is_even(13))

result = is_even(18)
print("Result for 18 is:" ,result)
result = is_even(9)
print("Result for 9 is:" ,result)

# 8 - Now write the function is_odd(n) that returns True when n is odd and False otherwise.

def is_odd(n):
  if n % 2 != 0:
      return True
  else:
      return False

testEqual(is_odd(64), False)
testEqual(is_odd(23), True)

print(is_odd(32))
print(is_odd(13))

result = is_odd(18)
print("Result for 18 is:" ,result)
result = is_odd(9)
print("Result for 9 is:" ,result)

# 10 - Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side.

def is_rightangled(a, b, c):
    if abs(a**2 + b**2 - c**2) < 0.001:
      return True
    else:
      return False

testEqual(is_rightangled(3, 4, 5), True)
testEqual(is_rightangled(3, 4, 6), False)

# 11 - Extend the above program so that the sides can be given to the function in any order.

def is_rightangled(a, b, c):
    if abs(a**2 + b**2 - c**2) < 0.001 or abs(b**2 + c**2 - a**2) <   0.001 or abs(c**2 + a**2 - b**2) < 0.001:
      return True
    else:
      return False

testEqual(is_rightangled(5, 4, 3), True)
testEqual(is_rightangled(5, 5, 2), False)

# hello_name - Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!"

def hello_name(name):
  return "Hello " + name + "!"

# make_out_word - Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
def make_out_word(out, word):
  return out[0:2] + word + out[2:]

# first_two - Given a string, return the string made of its first two characters.
def first_two(str):
  return str[0:2]

print(hello_name("Genesis"))
print(make_out_word("<<>>","cider"))
print(first_two("crabapples"))