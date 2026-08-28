class Romb:
    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Сторона а повинна бути більше 0")

        if name == "corner_a":
            if value <= 0 or value >= 180:
                raise ValueError("Кут а повинен бути між 0 та 180 градусами")

            object.__setattr__(self, "corner_b", 180 - value)

        object.__setattr__(self, name, value)

    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a


romb = Romb(10, 60)

print("Сторона а:", romb.side_a)
print("Кут а:", romb.corner_a)
print("Кут б:", romb.corner_b)