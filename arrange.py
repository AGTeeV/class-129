import csv

data=[]
with open('archieve.csv') as file:
    reader=csv.reader(file)
    for row in reader:
        data.append(row)
headers=data[0]
planetdata=data[1:]
for i in planetdata:
    i[0]=i[0].lower()
planetdata.sort(key=lambda planetdata:planetdata[0])

with open("sorted.csv","w") as x:
    writer=csv.writer(x)
    writer.writerow(headers)
    writer.writerows(planetdata)

with open("sorted.csv") as input,open("finalsorted.csv","w",newline="") as output:
    writer=csv.writer(output)
    reader=csv.reader(input)
    for i in reader:
        if any(x.strip() for x in i):
            writer.writerow(i)