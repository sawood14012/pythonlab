def subsetsum(ls,target):
    pos=0
    while pos<len(ls)and ls[pos]<=target:
        pos+=1
    for i in range(pos+1):
        for j in range(i):
            for k in range(j):
                if ls[i]+ls[j]+ls[k]==target:
                     return True

    return False
print("enter the list of numbbers:")
ls=list(map(int,input().split()))
print("enter the target")
target=int(input())
ls.sort()
print(subsetsum(ls,target))