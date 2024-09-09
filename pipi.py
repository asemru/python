import threading
from queue import Queue
from time import sleep
from random import randint


class Cafe:
    ry = []
    def __init__(self, *tables):
        self.queue = Queue()
        self.table = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.table:
                if table.guest == None:
                    table.guest = guest.name
                    guest.start()
                    print(f'{table.guest} сел(-а) за стол номер {table.number}')
                    self.ry.append(guest)
                    break
            if not guest.is_alive():
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        flag = True
        while not self.queue.empty() or flag:
            for table in self.table:
                guest_name = table.guest
                for guest in self.ry:
                    if guest_name == guest.name:
                        if not guest.is_alive():
                            print(f'{guest.name} покушал(-а) и ушёл(ушла)')
                            print(f'Стол номер {table.number} свободен')
                            table.guest = None
                            guest.join()
                            if not self.queue.empty():
                                guest = self.queue.get()
                                print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                                table.guest = guest.name
                                guest.start()
                        break
            flag = False
            for table in self.table:
                if not table.guest is None:
                    flag = True
                    break



class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
