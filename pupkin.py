import threading
import random
import time
class Bank:
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        for __ in range(1, 101):
            i = random.randint(50, 500)
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            self.balance += i
            print(f'Пополнение: {i}, Баланс: {self.balance}')
            time.sleep(0.001)


    def take(self):
        for _ in range(1, 101):
            i1 = random.randint(50, 500)
            print(f'Запрос на -> {i1}')
            if i1 <= self.balance:
                self.balance -= i1
                print(f'Снятие: {i1}, Ваш текуший баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')





