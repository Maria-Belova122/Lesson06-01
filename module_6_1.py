# ЗАДАНИЕ ПО ТЕМЕ "Зачем нужно наследование"

class Animal:
    alive = True  # живой
    fed = False  # не накормленный

    def __init__(self, name):
        self.name = name  # название животного

    def eat(self, food):
        # Если переданное растение съедобное, т.е. food.edible = True
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True  # накормленный
        # Если переданное растение не съедобное, т.е. food.edible = False
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False  # не живой


class Plant:
    edible = False  # не съедобное

    def __init__(self, name):
        self.name = name  # название растения


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True  # съедобное


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
