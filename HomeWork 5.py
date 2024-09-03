import random
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y , first, second)))




def get_advanced_writer(file_name):
    def write_everything(*data_set):
        a = open(file_name, 'a', encoding='utf-8')
        for i in data_set:
            a.write(f'{i}\n')
        a.close()
        return file_name
    return write_everything


b = get_advanced_writer('example.txt')
b('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())





