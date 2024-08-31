a = {}
def custom_write(file_name, strings):
    fed = open(file_name, 'a', encoding='utf-8')
    fed1 = open(file_name, 'r', encoding='utf-8')
    b = 1
    for i in strings:
        a[(fed.tell(), b)] = i
        b += 1
        fed.write(f'{i}\n')
    fed.close()
    fed1.close()
    for h in a:
        print(h, a[h])



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


custom_write('test.txt', info)

















