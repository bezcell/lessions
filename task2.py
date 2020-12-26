class Road:
    def __init__(self, length, width):
        self.__length = int(length)
        self.__width = int(width)

    def calc_asphalt(self, mass, height):
        res = self.__length * self.__width * mass * height
        return f"{res} т"


road = Road(1000, 3)
print(road.calc_asphalt(mass=25, height=5))
