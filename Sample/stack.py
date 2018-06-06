def Getstack():
    stack1 = []
    return stack1


def Isempty(stack1):
    if len(stack1) == 0:
        return True
    else:
        return False


def Top(stack1):
    return len(stack1)-1          # last pushed element
                                # if no element is there ,itll return top as -1


def Push(element,stack1):
    stack1.append(element)


def Pop(stack1):
    if stack1:
        last_ele = stack1[len(stack1)-1]
        del stack1[len(stack1)-1]
        return last_ele
    else:
        return -1

