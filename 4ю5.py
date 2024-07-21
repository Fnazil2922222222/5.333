class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super(House, cls).__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return False

    def __add__(self, value):
        self.floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)