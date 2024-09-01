import tkinter
class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.vin = __vin
        self.num = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_number(self.num)

    def __is_valid_vin(self, vin_number):
        if vin_number != int(vin_number):
            raise IncorrectVinNumber('Некорректный тип vip номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectCarNumbers('Неверный диапазон для vin номера')
        return True

    def __is_valid_number(self, numbers):
        if numbers != str(numbers):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True
class IncorrectVinNumber (Exception):
    pass



class IncorrectCarNumbers(Exception):
    pass

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc)
except IncorrectCarNumbers as exc:
  print(exc)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc)
except IncorrectCarNumbers as exc:
  print(exc)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc)
except IncorrectCarNumbers as exc:
  print(exc)
else:
  print(f'{third.model} успешно создан')