d = {}
d[2] = 12345
d[5] = "hello"
d['hello'] = 'world'
d['list']=[2,3,4,5,6]
d[ (1,2) ] = 55
print(d)
d['list']  = 55.3
print(d)

person = {'first' : 'John',
         'last' : 'Smith',
         'age' : 50
         'height' : 60}
persn['age'] = person['age'] + 1

print(person)

k = person.keys()
print(k)
for item in k:
  print('person[',item'] = ',person[item])

# convert dict_keys into a list:
klist = [x for x in person,keys()]
print(klist)

# pull out the values and convert to a list
vlist = [x for x in person.values()]

yt = ('hello',44,34.5)
a,b,c = yt

for k,v in person.items():
  print(k,v)

for k in person.keys():
  print(k,person[k])

s1 = {'name':'a','id':1, 'scores',:[100,90,85]}
s2 = {'name':'b','id':2, 'scores',:[98,85]}
s3 = {'name':'c','id':3, 'scores',:[99,76,88,82]}
s4 = {'name':'d','id':4, 'scores',:[98]}

student_list = [s1,s2,s3,s4]
student_dict = {}
for item in student_list:
  student_dict[item['id']] = item