import random
random_list = []
for i in range(20):
    random_list.append(random.randrange(5,15))

odds = []
for item in random_list:
    if item%2==1:
        odds.append(item)

squares = []
for item in random_list:
    squares.append(item*item)
    
def square(x):
    return x*x

counting = [x for x in range(5,10)]
tens_v2 = [10 for x in range(15)]
random_list_v2 = [random.randrange(5,10) for x in range(20)]
random_list_v3 = [random.randrange(x) for x in range(0,100,5)]
sentence = 'now is the winter of our discontent'

## mapping function
upper_case = [word.capitalize() for word in sentence.split()]

sqlist = [x*x for x in random_list_v3]