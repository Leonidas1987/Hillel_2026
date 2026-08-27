class Ромб:
    def __setattr__(self, name, value):
        if name == "сторона_а":
            if value <= 0:
                raise ValueError("Сторона а повинна бути більше 0")

        if name == "кут_а":
            if value <= 0 or value >= 180:
                raise ValueError("Кут а повинен бути між 0 та 180 градусами")

            object.__setattr__(self, "кут_б", 180 - value)

        object.__setattr__(self, name, value)

    def __init__(self, сторона_а, кут_а):
        self.сторона_а = сторона_а
        self.кут_а = кут_а


ромб = Ромб(10, 60)

print("Сторона а:", ромб.сторона_а)
print("Кут а:", ромб.кут_а)
print("Кут б:", ромб.кут_б)