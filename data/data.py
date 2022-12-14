'''
Extra: Use more than one data source and have your analysis compare, contrast, or correlate them.

This analysis finds the NYC borough with the greatest number of taxi zones and the borough with the largest population to determine if there is a present correlation between the two values.
'''

import sys
import csv
csv.field_size_limit(sys.maxsize)

read = csv.DictReader(open("taxi_zones.csv"))
zonedata = [x for x in read]
boro = [str(x['borough']) for x in zonedata]

def freq1(boro,l):
    return boro.count(l)

Queens = freq1(boro,"Queens")
Brooklyn = freq1(boro,"Brooklyn")
Manhattan = freq1(boro,"Manhattan")
Bronx = freq1(boro,"Bronx")
SI = freq1(boro,"Staten Island")

boros = {'Queens':Queens, 'Brooklyn':Brooklyn, 'Bronx':Bronx, 'Manhattan':Manhattan, 'Staten Island': SI}
largest = max(boros, key = boros.get)

print(largest,"has the most taxi zones.")

with open('Population.csv') as file:
  header = next(file)
  list = csv.reader(file)
  for row in list:
    split = str([x[1] for x in enumerate(list) if x[0] in [3]]).split(", ")
    q_population = split[2].replace("'",'')

with open('Population.csv') as file:
  header = next(file)
  list = csv.reader(file)
  for row in list:
    split = str([x[1] for x in enumerate(list) if x[0] in [1]]).split(", ")
    k_population = split[2].replace("'",'')

with open('Population.csv') as file:
  header = next(file)
  list = csv.reader(file)
  for row in list:
    split = str([x[1] for x in enumerate(list) if x[0] in [2]]).split(", ")
    m_population = split[2].replace("'",'')

with open('Population.csv') as file:
  header = next(file)
  list = csv.reader(file)
  for row in list:
    split = str([x[1] for x in enumerate(list) if x[0] in [0]]).split(", ")
    b_population = split[2].replace("'",'')

with open('Population.csv') as file:
  header = next(file)
  list = csv.reader(file)
  for row in list:
    split = str([x[1] for x in enumerate(list) if x[0] in [4]]).split(", ")
    si_population = split[2].replace("'",'')

pops = {'Queens':q_population, 'Brooklyn':k_population, 'Bronx':b_population, 'Manhattan':m_population, 'Staten Island': si_population}
largest_pop = max(pops, key = pops.get)

print(largest_pop,"has the largest population.")

if largest == largest_pop:
  print("There is a correlation between population size and number of taxi zones.")
else:
  print("Population size does not determine number of taxi zones.")