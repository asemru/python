class WordsFinder:
    tim = []
    kim = {}
    def __init__(self, *fid):
        for i in fid:
            self.tim.append(i)
            print(self.tim)

    def get_all_words(self):
        for i in self.tim:
            with open(i, 'r', encoding='utf-8') as op:
                ope = []
                a = op.read().split()
                for p in a:
                    ope.append(p.lower().replace(',', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '').replace('.', '').replace('=', '').replace(' - ', ''))


                self.kim[i] = ope

        return self.kim

    def find(self, tim1):
        k = 1
        for i, v in self.kim.items():
            for u in v:
                if u == tim1.lower():
                    return {i: k}
                    break
                else:
                    k += 1

    def count(self, tim2):
        k = 0
        for i, v in self.kim.items():
            for u in v:
                if u == tim2.lower():
                    k += 1
            return {i: k}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего








