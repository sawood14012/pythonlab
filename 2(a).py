class vehical:
    def __init__(self, typen):

        self.vehical_typen = typen

    def type(self):
        return self.vehical_typen

class bike(vehical):
    def __init__(self, name, typen):
            vehical.__init__(self, typen)
            self.name = name

    def dis(self):
        return self.name


class car(vehical):
    def __init__(self, name, typen):
            vehical.__init__(self, typen)
            self.name = name

    def disply1(self):
        print(self.type())
        return self.name



class pedalbikes(bike):
    def __init__(self, name, typen, pedalno):
            bike.__init__(self,name,typen)
            self.pedalsno = pedalno

    def displ(self):
        print(self.name)
        print(self.type())
        return self.pedalsno


class motorbikes(bike):
    def __init__(self, name, typen, motorno):
            bike.__init__(self,name,typen)
            self.mot = motorno

    def disply3(self):
        print(self.name)
        print(self.type())
        return self.mot


x = motorbikes("pulsar", "twowheeler", 1100)
y = pedalbikes("hercules","cycle",1200)
z = car("jeep", "Suv")
print(x.disply3())
print(y.displ())
print(z.disply1())


