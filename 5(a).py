def vowelCount(str):
    vowel_list = ['a','e','i','o','u']
    str = str.lower()
    for i in range(97, 123):
        count = 0
        for j in str:
            if ord(j) == i:
                if j in vowel_list:
                    count += 1
        if count != 0:
            print("vowel", chr(i), ":", count)

vowelCount('Le Tour De france')

