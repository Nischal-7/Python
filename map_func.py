def addition(n):
	return n + n

numbers = (1, 2, 3, 4)
result = set(map(addition, numbers))
print(result)

#------------------------------------------------------------

a = "hello"
mylist = list(a)
print(mylist)

#------------------------------------------------------------

word =['sat', 'bat', 'cat']
listObj = list(map(list,word))
strObj = list(map(str, word))
print(listObj)
print(strObj)

#------------------------------------------------------------

resu = list(map(int, input().strip().split()))[:3]
print(resu)
