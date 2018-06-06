count = 0


def is_abecedarian(w):
    global count

    l = list(w)
    l = [ord(i) for i in l]
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            return False
    count += 1
    return True, count


n = int(input("Number of words you want to check : "))
for i in range(n):
    is_abecedarian(input("Enter the word : "))

print("\nNumber of abecedarian words : ", count)
