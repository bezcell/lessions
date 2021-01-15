class MyException(Exception):
    def __init__(self, text):
        self.txt = text


class Storage:
    square = 0
    unit_count = 0
    unit_cost = 0
    storage_data = {}

    def __init__(self, square, unit_count, unit_cost, storage_data):
        self.square = float(square)
        self.unit_count = int(unit_count)
        self.unit_cost = float(unit_cost)
        self.storage_data = storage_data

    def to_storage(self, product, count, department):
        if self.validate_count(count) and self.validate_department_product(department, product):
            self.storage_data[product][department] += int(count)
            return True
        else:
            return False

    @staticmethod
    def validate_count(count):
        try:
            if not isinstance(count, int):
                raise MyException("Количество должно быть целым числом!")
        except MyException as msg:
            print(f"Ошибка: {msg}")
            return False
        else:
            return True

    def validate_department_product(self, department, product):
        try:
            if product not in self.storage_data:
                raise MyException("Такого продукта не существует!")
            elif department not in self.storage_data[product]:
                raise MyException("Такого отдела не существует!")
        except MyException as msg:
            print(f"Ошибка: {msg}")
            return False
        else:
            return True


class Equipment:
    price = 100
    unit_place = 1
    unit_num = 0
    color = 'gray'


class Printer(Equipment):
    price = 1000
    barcode = 'PR-123'
    unit_num = 234


class Scanner(Equipment):
    barcode = 'SC-33'
    unit_num = 235
    color = 'black'


class Xerox(Equipment):
    price = 5000
    barcode = 'X-5-ET'
    unit_num = 237
    unit_place = 2


storage_data = {
    'printer': {
        'main': 0,
        'second': 10,
        'other': 500
    },
    'scanner': {
        'main': 1000,
        'second': 0,
        'other': 5
    },
    'xerox': {
        'main': 0,
        'second': 0,
        'other': 0
    },
}
# площадь склада, количество свободных мест, стоимость одного места
my_storage = Storage(5000, 20000, 15, storage_data)

# добавим 50 принтеров в отдел main
my_storage.to_storage('printer', 50, 'main')
# добавим 57 сканеров в отдел other
my_storage.to_storage('xerox', 50, 'other')
# добавим невалидный товар
my_storage.to_storage('pencil', 10, 'third')

print(my_storage.storage_data)
