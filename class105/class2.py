import csv
from os import makedirs 
import pandas as pd
import plotly.express as px
with open('class2.csv') as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)   
totalmarkes = 0 
totalentries = len(filedata)
for markes in filedata:
    totalmarkes += float(markes[1])
mean =   totalmarkes/totalentries
print(mean)
df=pd.read_csv('class2.csv')
figure = px.scatter(df ,x ='Student Number', y ='Marks' )
figure.update_layout(shapes = [
    dict(
        type = 'line',
        y0 = mean , y1=mean,
        x0 = 0, x1 = totalentries
    )
])
figure.show()