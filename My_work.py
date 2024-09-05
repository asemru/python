class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError
        else:
            self.step = step
        self.pointer = start

    def __iter__(self):
        if (self.step > 0 and self.pointer < self.stop) or (self.step < 0 and self.pointer > self.stop):
            print(self.pointer, end=' ')
        return self


    def __next__(self):
        self.pointer += self.step
        if (self.step > 0 and (self.pointer < self.stop or self.pointer == self.stop)) or (self.step < 0 and (self.pointer > self.stop or self.pointer == self.stop)):
            return self.pointer
        else:
            print('\n')
            raise StopIteration()



try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')

for i in iter3:
    print(i, end=' ')

for i in iter4:
    print(i, end=' ')

for i in iter5:
    print(i, end=' ')












