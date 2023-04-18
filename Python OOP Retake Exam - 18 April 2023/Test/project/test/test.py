from project152127.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):

    def setUp(self) -> None:
        self.robot = Robot('23', 'Military', 18, 200.9)

    def test_in_it(self):
        self.assertEqual('23', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(18, self.robot.available_capacity)
        self.assertEqual(200.9, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'top'
        self.assertEqual(f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ve.exception))

    def test_price_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -10
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_if_hardware_component_in_self_hardware_upgrades(self):
        self.robot.hardware_upgrades.append('new app')
        self.assertEqual(f"Robot 23 was not upgraded.", self.robot.upgrade('new app', 19.9))

    def test_upgrade_if_hardware_component_not_in__self_hardware_upgrades(self):
        self.assertEqual(f'Robot 23 was upgraded with new app.', self.robot.upgrade('new app', 10.0))
        self.assertEqual(215.9, self.robot.price)
        self.assertEqual(['new app'], self.robot.hardware_upgrades)

    def test_update_version_was_not_updated(self):
        result = self.robot.update(0.5, 20)
        self.assertEqual(result, "Robot 23 was not updated.")
        self.assertEqual(self.robot.available_capacity, 18)

    def test_update_version_correct(self):
        result = self.robot.update(1.0, 10)
        self.assertEqual(result, "Robot 23 was updated to version 1.0.")
        self.assertEqual(self.robot.available_capacity, 8)

    def test_update_version_was_not_updated_twice(self):
        self.robot.update(2.0, 5)
        result = self.robot.update(1.5, 5)
        self.assertEqual(result, "Robot 23 was not updated.")

    def test_gt_operator(self):
        other_robot = Robot('24', 'Education', 16, 250.00)
        result = self.robot > other_robot
        self.assertEqual(result, "Robot with ID 23 is cheaper than Robot with ID 24.")

    def test_gt_operator_num_two(self):
        other_robot = Robot('24', 'Education', 16, 200.90)
        result = self.robot > other_robot
        self.assertEqual(result, "Robot with ID 23 costs equal to Robot with ID 24.")

    def test_gt_operator_num_tree(self):
        other_robot = Robot('24', 'Education', 16, 150.00)
        result = self.robot > other_robot
        self.assertEqual(result, "Robot with ID 23 is more expensive than Robot with ID 24.")


if __name__ == '__main__':
    main()
