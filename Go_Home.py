class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += int(dy)

class Horse:
    x_distance = 0
    sound = 'Frrr'
    def run(self, dx):
        self.x_distance += int(dx)



class Pegasus(Eagle, Horse):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        print(self.x_distance, self.y_distance)


    def voice(self):
        print(self.sound)




p1 = Pegasus()
print(Pegasus.mro())
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
