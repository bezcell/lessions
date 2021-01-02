class Cloth:
    # type_cloth = 'costume'
    type_cloth = 'coat'
    size = 0

    def __init__(self, type_cloth):
        self.type_cloth = type_cloth

    def set_size(self, size):
        self.size = size

    @property
    def textile(self):
        if self.type_cloth == 'coat':
            res = self.size / 6.5 + 0.5
        else:
            res = 2 * self.size + 0.3
        return res


cloth = Cloth('coat')
cloth.set_size(500)
print(cloth.textile)
