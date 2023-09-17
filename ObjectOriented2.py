import math
class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        delta_y =  self.coor2[1]-self.coor1[1]
        delta_x = self.coor2[0]-self.coor1[0]
        return math.sqrt(delta_y**2+ delta_x**2)

    def slope(self):
        delta_y =  self.coor2[1]-self.coor1[1]
        delta_x = self.coor2[0]-self.coor1[0]
        return delta_y / delta_x


class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (math.pi)*(self.radius**2)*(self.height)

    def surface_area(self):
        return (2*(math.pi)*self.radius) * (self.radius + self.height)
