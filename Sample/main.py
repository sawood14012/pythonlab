from Sample import stack

ch = 1
stack1=stack.Getstack()
while ch == 1:
    op = int(input("1. To check if empty \n 2. To return index of top element of stack \n 3. Push  \n 4. Pop"))
    if op == 1:
        true_or_false = stack.Isempty(stack1)
        print("status of empty :",  true_or_false)
    elif op == 2:
        index = stack.Top(stack1)
        print("index of top element:",index)
    elif op == 3:
        ele = int(input("enter element to be pushed"))
        stack.Push(ele,stack1)
    elif op == 4:
        ele = stack.Pop(stack1)
        if ele != -1:
            print("element popped out is:",ele)
        else:
            print("no more elements to pop")
    ch = int(input("enter 1 to continue"))

