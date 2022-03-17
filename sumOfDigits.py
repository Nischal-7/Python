n = input("Enter a number to find the sum of its digits: ")

add = 0
for i in n:
    add += int(i)

print("The sum of the digits is: ", add)