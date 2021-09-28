import csv
import pandas as pd
import plotly.express as px
with open('Copy+of+data+-+data.csv')as f:
    reader=csv.reader(f)
    filedata = list(reader) 
filedata.pop(0)
totalmarkes = 0
totalenetries = len(filedata)
for markes in filedata:
    totalmarkes += float(markes[1])
mean = totalmarkes/totalenetries
print(mean)
df = pd.read_csv('Copy+of+data+-+data.csv')
figure = px.scatter(df,x = 'date',y='casese')
figure.update_layout(shapes=[
    dict(
        type ='line',
        y0= mean, y1=mean,
        x0 =0, x1=totalenetries
    )
])
figure.show()