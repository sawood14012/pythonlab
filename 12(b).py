def patition(ls):
    result=[]
    for name in ls:
        if name[0].lower() in 'abcdefghijklm':
            result.append(name)
    print(result)
patition(['Eleanorr','Eelyo','Sammy','Owen','Gavin'])