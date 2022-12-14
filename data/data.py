'''
This analysis finds the NYC borough with the greatest number of taxi zones.
'''

import sys
import csv
csv.field_size_limit(sys.maxsize)

read = csv.DictReader(open("taxi_zones.csv"))
zonedata = [x for x in read]
boro = [str(x['borough']) for x in zonedata]

def freq(boro,l):
    return boro.count(l)

Queens = freq(boro,"Queens")
Brooklyn = freq(boro,"Brooklyn")
Manhattan = freq(boro,"Manhattan")
Bronx = freq(boro,"Bronx")
SI = freq(boro,"Staten Island")

boros = {'Queens':Queens, 'Brooklyn':Brooklyn, 'Bronx':Bronx, 'Manhattan':Manhattan, 'Staten Island': SI}
largest = max(boros, key = boros.get)

print(largest,"has the most taxi zones.")