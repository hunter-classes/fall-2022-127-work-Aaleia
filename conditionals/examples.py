def is_even(n):
  if n % 2 == 0:
      return True
  else:
      return False

def is_even_short_version(n):
    return n%2 == 0

def is_odd(n):
    return not(is_even(n))

result = is_even(18)
print("Result for 18 is:" ,result)
result = is_even(9)
print("Result for 9 is:" ,result)

result = is_odd(18)
print("Result for 18 is:" ,result)
result = is_odd(9)
print("Result for 9 is:" ,result)

def isRightAngle(a,b,c):
  """
  c is longest
  """
  sum = a*a + b*b
  return abs (math.sqrt(sum)-c) < 0.001

def isRightAngle2(a,b,c):
  """
  any order for sides
  """
  sum = a*a + b*b
  return isRightAngle(a,b,c) or \
          isRightAngle(b,c,a) or \
          isRightAngle(c,a,b)

print(isRightAngle(5,3,4)) # will not recognize because a is largest
print(isRightAngle2(5,3,4))