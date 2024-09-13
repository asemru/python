import logging
import unittest
import hihi
class RunnerTest:
    is_frozen = False


    def test_walk(self):
        try:
            a = hihi.Runner('', -5)

            for _ in range(10):
                a.walk()

            logging.info('test walk выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)



    def test_run(self):
        try:
            b = hihi.Runner('', 5, 1243154)
            for _ in range(10):
                b.run()

            logging.info('test_run выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge(self):
        c1 = hihi.Runner('')
        c2 = hihi.Runner('')
        for _ in range(10):
            c1.walk()
            c2.run()




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='runner_tests21.log', encoding='utf-8', filemode='w', format='''%(asctime)s
                                            | %(levelname)s | %(message)s''')
    op = RunnerTest()
    op.test_walk()
    op.test_run()

