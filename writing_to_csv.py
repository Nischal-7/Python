
import csv
file = open('/home/nischal/Python/marksreport.csv','w',newline='\n')
writer = csv.writer(file)
student=[]

firstrow=['USN','NAME','ME','CNS','DBMS','ATC','ADP','UP']
writer.writerow(firstrow)

for i in range(1,11):
    usn=input("Enter the USN of student {}: ".format(i))
    student.append(usn)
    name=input("Enter the NAME: ")
    student.append(name)
    for j in range(1,7):
        marks=input("Enter the marks of Subject {}: ".format(j))
        student.append(marks)
    writer.writerow(student)
    student.clear()
    print('')
file.close()

file = open('/home/nischal/Python/marksreport.csv')
reader = csv.reader(file)
data = list(reader)
print("USN\tNAME\tRESULT\tTOTAL\t\tAVG\t\t  CLASS")

for num in range(1,len(data[:])):
    total = 0
    flag = 1

    for marks in range(2,8):
        total += int(data[num][marks])
        if(int(data[num][marks]) < 50):
            flag = 0

    avg = total/6

    if(flag == 0):
        result = "FAIL"
    else:
        result = "PASS"

    if(result == "FAIL"):
        cls = "No Class"
    elif(avg >= 85):
        cls = "Distinction"
    elif(avg >= 75):
        cls = "First Class"
    elif(avg >= 60):
        cls = "Second Class"
    else:
        cls = "Pass"

    print(data[num][0],"\t",data[num][1],"\t",result,"\t",total,"\t",avg,"\t",cls)

file.close()
