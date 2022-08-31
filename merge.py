import csv

data1 = []
data2 = []
with open('final2.csv') as file:
    reader=csv.reader(file)
    for row in reader:
        data1.append(row)
headers1=data1[0]
planetdata1=data1[1:]

with open('finalsorted.csv') as file:
    reader=csv.reader(file)
    for row in reader:
        data2.append(row)
headers2=data2[0]
planetdata2=data2[1:]

headers=headers1+headers2
planetdata=[]
for i,data in enumerate(planetdata1):
    planetdata.append(planetdata1[i]+planetdata2[i])

with open("merged.csv","a+") as x:
    writer=csv.writer(x)
    writer.writerow(headers)
    writer.writerows(planetdata)

with open("merged.csv") as input,open("finalmerged.csv","a+",newline="") as output:
    writer=csv.writer(output)
    reader=csv.reader(input)
    for i in reader:
        if any(x.strip() for x in i):
            writer.writerow(i)