from time import sleep


class TrafficLight:
    __color = "red"
    timing = {"red": 7, "yellow": 2, "green": 7}

    def running(self):
        print(self.__color)
        sleep(self.timing[self.__color])
        if self.__color == "red":
            self.__color = "yellow"
        elif self.__color == "yellow":
            self.__color = "green"
        elif self.__color == "green":
            self.__color = "red"
        self.running()


traffic = TrafficLight()
traffic.running()
