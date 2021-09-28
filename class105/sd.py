import csv
import math
with open('data.csv') as f :
    reader =csv.reader(f)
    filedata = list(reader)
data = filedata[0]
def mean (data):
    n=  len(data)
    total = 0
    for x in data :
        total += int(x)
    mean= total/n 
    return mean 
print(total/n)
squaredlist = []
for number in data :
    a = int(number)-mean(data)
    a = a**2
    squaredlist.append(a) 
sum = 0 
for i in squaredlist :
    sum = sum + i 
result = sum/(len(data)-1)
sd = math.sqrt(result)
print(sd)