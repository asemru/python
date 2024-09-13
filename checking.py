import unittest
import nefne
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        a = nefne.Runner('')
        for _ in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        b = nefne.Runner('')
        for _ in range(10):
            b.run()
        self.assertEqual(b.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        c1 = nefne.Runner('')
        c2 = nefne.Runner('')
        for _ in range(10):
            c1.walk()
            c2.run()
        self.assertNotEqual(c1.distance, c2.distance)



if __name__ == '__main__':
    unittest.main()


