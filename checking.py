import unittest
import nefne
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        a = nefne.Runner('')
        for _ in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    def test_run(self):
        b = nefne.Runner('')
        for _ in range(10):
            b.run()
        self.assertEqual(b.distance, 100)

    def test_challenge(self):
        c1 = nefne.Runner('')
        c2 = nefne.Runner('')
        for _ in range(10):
            c1.walk()
            c2.run()
        self.assertNotEqual(c1.distance, c2.distance)



if __name__ == '__main__':
    unittest.main()




