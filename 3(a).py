def add(dict):
    phone = input("enter the name of phone")
    price = int(input("enter the price"))
    dict[phone] = price
    return dict


def search(dict):
    not_serached = input("enter the phone to be searched")
    for keys, values in dict.items():
        if keys == not_serached:
            print("price is: ", values)
            break
    return dict


def sameprice(dict):
    new = {}
    for keys, values in dict.items():
        if values not in new.keys():
            new[values] = []
        new[values].append(keys)
        print("phones with same price is ", new)
    return dict


def remove(dict):
    phone = input("remove which phone?")
    if phone not in dict.keys():
        print("phone not found")
    else:
        del dict[phone]
    return dict


def disp(dict):
    li = []
    for values in dict.values():
        li.append(values)
    li.sort()
    for i in li:
        for keys, values in dict.items():
            if i == values:
                print(keys)
    print("next")


ch = 1
dict = {}
while ch == 1:
    op = int(input("Choose the option\n1.for adding a phone\n2.for searching a phone\n3.find phones with same "
                   "price\n4.delete phone\n5.display sorted dictionary"))
    if op == 1:
        dict =add(dict)
        print(dict)
    elif op == 2:
        search(dict)
    elif op == 3:
        sameprice(dict)
    elif op == 4:
        dict = remove(dict)
        print(dict)
    elif op == 5:
        disp(dict)

ch = int(input("enter one to countinue.."))
