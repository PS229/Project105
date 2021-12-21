import csv
import math
import statistics

with open("pro.csv", newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)

totalMarks = 0
totalEntries = len(fileData)

for i in fileData:
    totalMarks = float(i[0]) + totalMarks
mean = totalMarks/totalEntries
add1 = 0
for i in fileData:
    sub = float(i[0]) - mean
    sqr = sub**2
    add1 = sqr + add1
step2 = add1/totalEntries
st_dev = math.sqrt(step2)
print(st_dev)