class Stationery:
    title = ''

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = 'pen'

    def draw(self):
        print("Запуск отрисовки ручкой.")


class Pencil(Stationery):
    title = 'pencil'

    def draw(self):
        print("Запуск отрисовки карандашом.")


class Handle(Stationery):
    title = 'handle'

    def draw(self):
        print("Запуск отрисовки маркером.")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
