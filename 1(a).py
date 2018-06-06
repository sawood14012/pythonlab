import random

def rotateleft(num):
    a = [num[1],num[2],num[0]]
    return a

num = [random.randint(0,9)for i in range(3)]
print(num)
print(rotateleft(num))