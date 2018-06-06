def initials(name):
    s = ''
    for i in name:
        if i.isupper():
            s = s+i
    return s


name = input(" Enter name : ")
print("Initials are : ", initials(name))
