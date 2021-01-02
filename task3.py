class Cell:
    count_cells = 0

    def __init__(self, count_cells):
        self.count_cells = count_cells

    def __add__(self, other):
        self.count_cells += other.count_cells
        return self

    def __sub__(self, other):
        res = self.count_cells - other.count_cells
        if res > 0:
            self.count_cells = res
            return self
        else:
            print("Ошибка вычитания клеток!")

    def __mul__(self, other):
        res = self.count_cells * other.count_cells
        return Cell(res)

    def __truediv__(self, other):
        res = self.count_cells // other.count_cells
        return Cell(res)

    def make_order(self, cells_in_row):
        res = ""
        cc = self.count_cells
        while cc > 0:
            cir = cells_in_row
            while cir > 0 and cc > 0:
                res += "*"
                cir -= 1
                cc -= 1
            res += "\n"
        return res


cell_1 = Cell(50)
cell_2 = Cell(45)

order = cell_1.make_order(13)
print(order)
