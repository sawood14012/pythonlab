n = 1
li = []
while n != 'quit':
    li.append(n)
    n = input()
li.pop(0)           # removes the additional 1 that we added
#print(li)
for item in li[::-1]:
    print(item)

