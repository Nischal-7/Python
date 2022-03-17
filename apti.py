from datetime import date
import csv
import random

op = open('/home/nischal/report.csv', 'w', newline='\n')
opwriter = csv. writer(op)

correct=0
answers = []
n = int(input("Enter the number of questions to be generated: "))
d = int(input("Enter the number of digits either 2 or 3: "))
if d == 2:
    for i in range(n):
        a = random.randint(10,100)
        b = random.randint(10,100)
        print(" ",a)
        print("x",b)
        print("-------")
        answers.append(a*b)

else:
    for i in range(n):
        a = random.randint(100,1000)
        b = random.randint(100,1000)
        print(" ",a)
        print("x",b)
        print("-------")
        answers.append(a*b)
print("Enter the answers")
for i in range(n):
    ip = int(input())
    org = answers[i]
    if org == ip:
        correct += 1

#row = [date.today(), correct, correct*100/n]
row = [date.today(), str(n)+" digits", str(correct)+"/"+str(n), str(correct*100/n)+"%"]
'''row.append(date.today())
row.append(str(n)+" digits")
row.append(str(correct)+"/"+str(n))
row.append(str(correct*100/n)+"%")'''
opwriter.writerow(row)
op.close()
