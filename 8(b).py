class Queue_full(Exception):
    def __init__(self):
        Exception.__init__(self)

class Queue_empty(Exception):
    def __init__(self):
        Exception.__init__(self)

class queue:
    def __init__(self,max):
        self.que=[]
        self.max=max
    def insert(self):
        try:
            if len(self.que)>= self.max:
                raise Queue_full()
        except Queue_full:
            print("Queue Overflow! ")
        else:
            self.que.append(input("Enter the element to be inserted to queue"))
    def delete(self):
        try:
            if len(self.que)== 0:
                raise Queue_empty()
        except Queue_empty:
            print("Queue Underflow")
        else:
            del self.que[0]
    def display(self):
        print(self.que)

m = int(input("Enter the maximum number of elements in the queue - "))
q = queue(m)
i = 0
while i != 4:
    i=int(input("1 for insert \n2 for delete \n3 for display \n4 for exit\n "))

    if i == 1:
        q.insert()
    if i == 2:
        q.delete()
    if i == 3:
        q.display()
