#abc abstract base class,ABC abstractmethod
from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        print("more than 2 sides")
class Triangle(Polygon):
    def sides(self):
        print("3")
    def info(self):
        print("triangle info")
class Rect(Polygon):
    def sides(self):
        print("4")
t1=Triangle()
t1.sides()
print("hell")
