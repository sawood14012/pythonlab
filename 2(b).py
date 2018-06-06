def censor(name):
    with open(name, 'r')as fp:
        contents = fp.read()
        li = contents.split()
        for i in li:
            if len(i) == 4:
                contents = contents.replace(i, "xxxx")

    with open(name,'w')as fp:
        fp.write(contents)


print("before replacing ")

with open("meer.txt", 'r')as fp:
    contents = fp.read()
    print(contents)

censor("meer.txt")
print("after replacing")
with open("meer.txt", 'r')as fp:
    c = fp.read()
    print(c)
