class Worker:
    name = ''
    surname = ''
    position = 'Директор'
    __income = {}

    def set_income(self, new_income):
        self.__income = new_income

    def get_income(self):
        return self.__income


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self.get_income()['wage'] + self.get_income()['bonus']


pos = Position()
pos.name = 'Григорий'
pos.surname = 'Чернов'
pos.position = 'Директор'
pos.set_income(new_income={'wage': 10000, 'bonus': 2000})
print(pos.name, pos.surname, pos.position)

print(pos.get_full_name())
print(pos.get_total_income())
