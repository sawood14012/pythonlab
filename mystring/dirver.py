from mystring import *
x = 1
while x:
    print("\n1. Palindrome \n2. CamelCase \n3. Count no. of vowels \n4. Exit")
    ch = int(input("Enter Choice\n"))
    if ch != 4:
        str = input("Enter string\n")
        if ch == 1:
            palin.pal(str)
        elif ch == 2:
            camel.cam(str)
        elif ch == 3:
            countvow.countv(str)
    else:
        x=0
1
