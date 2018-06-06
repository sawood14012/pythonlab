class city:
    def __init__(self,city,place=[]):
        self.city=city
        self.place=place

    def add_place(self,place):
        self.place.append(place)

    def remove_palace(self,place):
        if place in self.place:
            self.place.remove(place)

    def display(self):
        print(self.place)

newcity=city(input("enter a place"))
while 1:
    print("\n1:add a place\n2:remove a place\n3:display a place")
    ch=int(input("enter your choice"))
    if ch==1:
        newcity.add_place(input("enter a place"))
    elif ch==2:
        newcity.remove_palace(input("delete a place"))
    else:
        newcity.display()