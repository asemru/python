from threading import Thread
import time
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        HP = 100
        Day = 0
        print(f'{self.name} на нас напали!')
        while HP > 0:
            time.sleep(1)
            HP -= self.power
            Day += 1
            print(f'{self.name} сражается {Day} день(дня)..., осталось {HP}')
        print(f'{self.name} одержал победу спустя {Day} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

