import json

data = json.load(open('file.json'))
print (data)

datatxt = open('file.txt','r')
print(datatxt.read())

datacsv = open('file.csv','r')
print(datacsv.read())