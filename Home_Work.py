class Vehicle:

    __color_variants = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.model = str(__model)
        self.engine_power = __engine_power
        self.color = __color

    def get_model(self):
        print(f'Модель {self.model}')

    def get_horsepower(self):
        print(f'Мощность двигателя {self.engine_power}')

    def get_color(self):
        print(f'Цвет транспорта {self.color}')

    def print_info(self):
        print(f'Модель - {self.model} \nМощность двигателя - {self.engine_power} \nЦвет транспорта - {self.color}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        b = 0
        self.new_color = new_color.lower()
        for i in self.__color_variants:
            if i != str(self.new_color):
               b += 1
        if b != 5:
            self.color = str(self.new_color)
        else:
            print(f'Нельзя заменить на {self.new_color}')


class Sedan(Vehicle):
    __passengers_limit = 5




# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()












