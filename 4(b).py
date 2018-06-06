class adder:

    def __init__(self):
        self.d = {}
        self.l = []

    def add(self, x, y):
        print("Not implemented")


class Listad(adder):
    def __init__(self, l):
        adder.__init__(self)
        self.l = l

    def add(self, x, y):
        x.l.extend(y.l)
        self.l.extend(x.l)

    def __add__(w, e):
        l = []
        r = Listad(l)
        r.add(w, e)
        return r


class Dictad(adder):

    def __init__(self, d):
        adder.__init__(self)
        for i in d:
            self.d[i] = d[i]

    def add(self, x, y):
        for i in y.d.keys():
            x.d[i] = y.d[i]
        self.d = x.d

    def __add__(x, y):
        d = {}
        r = Dictad(d)
        r.add(x, y)
        return r

#works with dictionary items


d={'a': 1, 'b': 2}
a=Dictad(d)
print(a.d)
d={'c':3,'d':4}
b=Dictad(d)
print(b.d)
d={}
c=Dictad(d)
#c.add(a,b)
c=a+b
print(c.d)

#works with list
l=[1,2,3]
x=Listad(l)
l=[4,5,6]
y=Listad(l)
l=[]
z=Listad(l)
z=x+y
print(z.l)
