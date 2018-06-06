class student:
    student_count = 0
    python_count = 0

    def __init__(self, name, usn, nsub):
        self.name = name
        self.usn = usn
        self.list = []
        student.student_count += 1
        for i in range(0, nsub):
            x = input("Name of subject : ")
            if x == 'python':
                student.python_count += 1
            self.list.append(x)


stud = []
true = 1
while true:

    ch = int(input(' 1. Add new student\n 2. Check for students in python \n 3. Check number of students: \n 4.check py '))

    if ch == 1:
        n = input("Enter name : ")
        u = input("Enter USN : ")
        no = int(input("Enter number of Subjects : "))
        stud.append(student(n, u, no))

    elif ch == 2:
        print("total number of students in python : ", student.python_count)

    elif ch == 3:
        print(" Total number of students : ", student.student_count)

    else:
        exit()

