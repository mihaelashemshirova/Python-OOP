from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):

    def setUp(self):
        self.market = ShoppingCart('City', 20.5)
        self.supermarket = ShoppingCart('Billa', 30.5)

    def test_correct_initialization(self):
        self.assertEqual("City", self.market.shop_name)
        self.assertEqual(20.5, self.market.budget)

    def test_shop_name_for_value_error_props(self):
        with self.assertRaises(ValueError) as ve:
            self.market.shop_name = '211'
        assert ve.exception.args[0] == 'Shop must contain only letters and must start with capital letter!'

    def test_add_to_cart_with_valid_data(self):
        shop = ShoppingCart('Test', 200)
        shop.add_to_cart('product_name1', 99)
        self.assertEqual('product_name2 product was successfully added to the cart!', shop.add_to_cart('product_name2', 98))
        self.assertEqual({'product_name1': 99, 'product_name2': 98}, shop.products)

    def test_add_to_cart_product_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.market.add_to_cart('milk', 100.0)
        assert ve.exception.args[0] == 'Product milk cost too much!'

    def test_remove_from_cart_with_valid_data(self):
        shop = ShoppingCart('Test', 200)
        shop.add_to_cart('product_name1', 99)
        shop.add_to_cart('product_name2', 98)
        actual = shop.remove_from_cart('product_name1')
        expected = 'Product product_name1 was successfully removed from the cart!'
        self.assertEqual(expected, actual)
        self.assertEqual({'product_name2': 98}, shop.products)

    def test_add_to_cart_products(self):
        self.market.add_to_cart('milk', 10.0)
        self.assertEqual(10.0, self.market.products['milk'])
        self.assertEqual('milk product was successfully added to the cart!', self.market.add_to_cart('milk', 10))

    def test_remove_from_cart_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.market.remove_from_cart('banana')
        assert ve.exception.args[0] == 'No product with name banana in the cart!'

    def test_remove_from_cart(self):
        self.market.add_to_cart('milk', 10.0)
        #self.market.remove_from_cart('milk')
        self.assertEqual('Product milk was successfully removed from the cart!', self.market.remove_from_cart('milk'))

    def test_buy_product_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.market.products['milk'] = 25.5
            self.market.buy_products()
        assert ve.exception.args[0] == 'Not enough money to buy the products! Over budget with 5.00lv!'

    def test_buy_product(self):
        self.market.products['milk'] = 10.5
        #self.market.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 10.50lv.', self.market.buy_products())

    def test_add_(self):
        cart3 = self.market + self.supermarket
        self.assertEqual(cart3.shop_name, "CityBilla")
        self.assertEqual(cart3.budget, 51.0)
        self.assertDictEqual(cart3.products, {})
        self.market.products = {'item1': 5}
        self.supermarket.products = {'item2': 10}
        cart4 = self.market + self.supermarket
        self.assertEqual(cart4.shop_name, "CityBilla")
        self.assertEqual(cart4.budget, 51.0)
        self.assertDictEqual(cart4.products, {'item1': 5, 'item2': 10})


if __name__ == "__main__":
    main()
