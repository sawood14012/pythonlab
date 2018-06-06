class MarksNotEligible(Exception):
    def __init__(self):
        pass

try:
    m1 = input("Enter marks in DC : ")
    m2 = input("Enter marks in MP : ")
    m3 = input("Enter marks in CO: ")
    try:
        m1 = int(m1)
        m2 = int(m2)
        m3 = int(m3)
    except ValueError:
        print("Invalid marks! ")
        exit()
    if m1 < 0 or m2 < 0 or m3 < 0:
        raise ValueError
    if m1 < 20 or m2 < 20 or m3 < 20:
        raise MarksNotEligible


except MarksNotEligible:
    print("Not Eligible")
except ValueError:
        print("Cannot have negative marks! ")
else:
    print("Eligible")
