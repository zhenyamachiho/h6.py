import random
list = [random.randint(0, 100) for i in range(0, int(input()))]
print(list)
min = int(input())
max = int(input())
for i in list:
    if min <= i <= max:
        print(list.index(i))
