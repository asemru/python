import hihi
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        self.all_results = dict()

    def setUp(self):
        self.a = hihi.Runner('Усейн', 10)
        self.b = hihi.Runner('Андрей', 9)
        self.c = hihi.Runner('Ник', 3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_hihi_1(self):
        f1 = hihi.Tournament(90, self.a, self.c)
        self.all_results = f1.start()
        self.assertEqual(self.all_results[len(self.all_results)], 'Ник')
        self.all_results.update(self.all_results)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_hihi_2(self):
        f2 = hihi.Tournament(90, self.b, self.c)
        self.all_results = f2.start()
        self.assertEqual(self.all_results[len(self.all_results)], 'Ник')
        self.all_results.update(self.all_results)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_hihi_3(self):
        f3 = hihi.Tournament(90, self.a, self.b, self.c)
        self.all_results = f3.start()
        self.assertEqual(self.all_results[len(self.all_results)], 'Ник')
        self.all_results.update(self.all_results)

    def tearDown(self):
        print(self.all_results)

if __name__ == '__main__':
    unittest.main()

