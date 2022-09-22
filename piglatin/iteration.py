import random

# foreach loop

for counter in range(2,20,3):
  print(counter)

for counter in [0,1,2,3,4,]:
  print(counter)

for letter in "this is a sentence":
  print(letter)

# while loop
loop_counter = 0
while random_randrange(0,100) < 80:
  print("hello",loop_counter)
  loop_counter = loop_counter + 1
print("The above loop ran this many times: ",loop_counter)

i = 0
while i < 10:
  print(i)
  i = i + 1

i = 5
while i > 0:
  print(i)
  i = i - 1

s = 'hello world'
i = 0
while i < len(s):
  print(s[i])
  i = i + 1

for i in range (len(s))