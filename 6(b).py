import math


class Circle:

    def __init__(self, radius):
        if radius < 0:
            raise RuntimeError("Negative radius! ")
        else:
            self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def printCircle(self):
        print(self.__str__() + " radius: " + str(self.__radius))


try:
    c1 = Circle(5)
    print("c1's area is :", c1.getArea())
    c2 = Circle(0)
    print("c2's area is ", c2.getArea())
    c3 = Circle(-5)
    print("c3's area is :", c3.getArea())


except RuntimeError as ex:
    print("Invalid radius! ", ex)
