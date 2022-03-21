import pprint
marks = {}.fromkeys(['Math', 'English', 'Science'],0)
print(marks)

#------------------------------------------------------------------

squares = {x:x*x for x in range(1,11)}
for i in squares:
    print(squares[i])

#------------------------------------------------------------------

text = 'Hello world! This is Nischal, new to the Python world. Python is so interesting.'
count = {}

for char in text:
    count.setdefault(char, 0)
    count[char] += 1
print(count)
pprint.pprint(count)

#------------------------------------------------------------------

d = {k:v for (k,v) in squares.items() if v<70}
print(d)