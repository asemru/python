import unittest
import hihi2
import checking

a = unittest.TestSuite()
a.addTest(unittest.TestLoader().loadTestsFromTestCase(hihi2.TournamentTest))
a.addTest(unittest.TestLoader().loadTestsFromTestCase(checking.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(a)