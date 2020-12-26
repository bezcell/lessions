class Car:
    speed = 0
    color = 'black'
    name = 'Default car'
    is_police = False

    def go(self):
        print(f"{self.name} now starting")

    def stop(self):
        print(f"{self.name} now stop")

    def turn(self, direction):
        print(f"{self.name} now move to {direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    color = 'yellow'
    name = 'Town Ace'

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости!")


class SportCar(Car):
    speed = 300
    color = 'red'
    name = 'Lamborgini'


class WorkCar(Car):
    speed = 40
    name = 'Bobcat'

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости!")


class PoliceCar(Car):
    speed = 240
    color = 'blue/white'
    name = 'Bobik'
    is_police = True


car_police = PoliceCar()
print(car_police.speed, car_police.color, car_police.name, car_police.is_police)

car_sport = SportCar()
print(car_sport.speed, car_sport.color, car_sport.name, car_sport.is_police)

car_town = TownCar()
print(car_town.speed, car_town.color, car_town.name, car_town.is_police)

car_work = WorkCar()
print(car_work.speed, car_work.color, car_work.name, car_work.is_police)

car_police.go()
car_sport.stop()

car_town.go()
car_town.speed = 20
car_town.turn('west')
car_town.show_speed()
car_town.speed = 100
car_town.show_speed()


