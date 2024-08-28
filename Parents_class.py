class Animals:
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed

class Plants:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

    def ty(self):
        self.edible = True


class Mammal(Animals):
    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        elif food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predator(Animals):
    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        elif food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Flower(Plants):
    pass

class Fruit(Plants):
    def ty(self):
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
p2.ty()

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)