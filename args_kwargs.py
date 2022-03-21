def add(*n):
    total = 0
    for i in n:
        total += i
    return total

def food(**kwargs):
    print(kwargs)

print(add(2,3,4,5,6,7))
print(add(2,45,92))
food(fruits='Apple', Vegitables='Carrot')