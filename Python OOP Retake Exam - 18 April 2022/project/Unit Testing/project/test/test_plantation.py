from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plan = Plantation(2)

    def test_correct_initialization(self):
        self.assertEqual(2, self.plan.size)
        self.assertEqual({}, self.plan.plants)
        self.assertEqual([], self.plan.workers)

    def test_size_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plan.size = -1
        self.assertEqual('Size must be positive number!', str(ve.exception))

    def test_hire_worker_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plan.workers.append('abc')
            self.plan.hire_worker('abc')
        self.assertEqual('Worker already hired!', str(ve.exception))

    def test_hire_worker_new_worker(self):
        self.assertEqual('abc successfully hired.', self.plan.hire_worker('abc'))
        self.assertEqual(['abc'], self.plan.workers)

    def test_plantation_len(self):
        self.plan.plants = {'a': 'a'}
        self.assertEqual(1, len(self.plan))

    def test_plantation_len_wrong(self):
        self.plan.size = 1
        self.plan.hire_worker('a')
        self.plan.hire_worker('m')
        self.plan.plants['a'] = ['t']
        self.plan.plants['m'] = ['p']
        self.assertEqual(2, self.plan.__len__())

    def test_planting_worker_not_in_workers_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plan.planting('a', 'b')
        self.assertEqual('Worker with name a is not hired!', str(ve.exception))

    def test_planting_len_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plan.plants = {'ab': 'ab'}
            self.plan.workers = 'a'
            self.plan.planting('a', 'ab')
        self.assertEqual('The plantation is full!', str(ve.exception))

    def test_planting_worker_in_plans_keys(self):
        self.plan.size = 3
        self.plan.hire_worker('a')
        self.assertEqual("a planted it's first b.", self.plan.planting('a', 'b'))
        self.assertEqual({'a': ['b']}, self.plan.plants)

    def test_planting_planted_it_is_first(self):
        self.plan.size = 3
        self.plan.hire_worker('a')
        self.plan.planting('a', 'b')
        self.assertEqual('a planted c.', self.plan.planting('a', 'c'))
        self.assertEqual({'a': ['b', 'c']}, self.plan.plants)

    def test_plantation__str__(self):
        self.plan.workers = ['abv']
        self.plan.plants = {'abv': 'a'}
        self.assertEqual('Plantation size: 2\n'
                         'abv\n'
                         'abv planted: a', self.plan.__str__())

    def test_plantation__repr__(self):
        self.plan.workers = ['abv', 'bsg']
        self.assertEqual('Size: 2\nWorkers: abv, bsg', self.plan.__repr__())


if __name__ == "__main__":
    main()
