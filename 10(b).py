L = [1, 2, 3]

try:
    print(" Printing L[4] : ", L[4])
except IndexError:
    print("Invalid Index !")

try:
    print(" l+'msrit' : ", 1+'msrit')
except TypeError:
    print("Oops! It's a TypeError")
