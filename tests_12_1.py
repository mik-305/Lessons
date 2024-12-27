import unittest

class Runner:  # Проверяемый класс Runner
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def walk(self):
        self.distance += 5

    def run(self):
        self.distance += 10


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r1 = Runner('Сигизмунд')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50, f'{r1.name} должен пройти 50, а прошел {r1.distance}')

    def test_run(self):
        r2 = Runner('Сидор')
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100, f'{r2.name} должен пробежать 100, а пробежал {r2.distance}')

    def test_challenge(self):
        r1 = Runner('Сигизмунд')
        r2 = Runner('Сидор')
        for _ in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance, f'Дистанции не совпадают: {r1.distance} и {r2.distance}')

if __name__ == "__main__":
    unittest.main()






