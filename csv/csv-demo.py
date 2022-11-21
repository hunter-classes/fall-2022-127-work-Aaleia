# flawed example using split
f = open("demo.csv")
for line in f.readlines():
  print(line)
  line = line.strip()
  print(line.split(","))

# example using csv module into a list
reader = csv.reader(open("demo.csv"))
for line in reader:
  print(line)

# inefficient way
reader = csv.reader(open("demo.csv"))
full_data = [x for x in reader]
field_names = full_data[0]
data = full_data[1:]

# using the csv dict reader
reader = csv.DictReader(open("data.csv"))
for item in reader:
  print(item)

# using csv.DIctReader to create a list of dictionaries
reader = csv.DictReader(open("data.csv"))
data = []
for item in reader:
  data.append(item)

# using DictReader and list comprehensions
reader = csv.DictReader(open("demo.csv"))
full_data = [x for x in reader]

# get a specific data set using a loop
comedy = []
for item in data:
  comedy.append(int(item['Comedy']))

# get all comedy ratings using a list comprehension
comedy = [int(x['Comedy']) for x in data]

# get all people who like comedy
likes_comedy = [x['Code name'] for x in data if int(x['Comedy'])>7]

# also likes horror
likes_comedy_and_horror = [x for x in likes_comedy if int(x['Horror'])>6]