from tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.tennis = TennisPlayer('Ani', 20, 5.5)

    def test_correct_initializing(self):
        self.assertEqual('Ani', self.tennis.name)
        self.assertEqual(20, self.tennis.age)
        self.assertEqual(5.5, self.tennis.points)
        self.assertEqual([], self.tennis.wins)

    def test_name_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis.name = 'A'
        self.assertEqual('Name should be more than 2 symbols!', str(ve.exception))

    def test_name_setter_raise_value_error_two_simbyl(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis.name = 'An'
        self.assertEqual('Name should be more than 2 symbols!', str(ve.exception))

    def test_age_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis.age = 10
        self.assertEqual('Players must be at least 18 years of age!', str(ve.exception))

    def test_add_new_win_if_not_in_list(self):
        self.tennis.add_new_win('abc')
        self.assertEqual(['abc'], self.tennis.wins)

    def test_add_new_win_in_list(self):
        self.tennis.add_new_win('abc')
        self.assertEqual(f"abc has been already added to the list of wins!", self.tennis.add_new_win('abc'))

    def test_lt_incorrect(self):
        self.tennis1 = TennisPlayer('Kati', 22, 4.5)
        self.assertEqual('Ani is a top seeded player and he/she is better than Kati', self.tennis1.__lt__(self.tennis))

    def test_lt_correct(self):
        self.tennis1 = TennisPlayer('Kati', 22, 4.5)
        self.assertEqual('Ani is a better player than Kati', self.tennis.__lt__(self.tennis1))

    def test__str__(self):
        self.tennis.add_new_win('abc')
        self.assertEqual("Tennis Player: Ani\n"
                         "Age: 20\n"
                         "Points: 5.5\n" 
                         "Tournaments won: abc", self.tennis.__str__())

    def test__repr__(self):
        self.tennis.add_new_win('abc')
        self.tennis.add_new_win('abcd')
        self.assertEqual("Tennis Player: Ani\n"
                         "Age: 20\n"
                         "Points: 5.5\n" 
                         "Tournaments won: abc, abcd", self.tennis.__str__())


if __name__ == '__main__':
    main()
