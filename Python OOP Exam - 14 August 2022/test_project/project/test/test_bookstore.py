from project.bookstore import Bookstore

from unittest import TestCase, main


class TestBookstore(TestCase):

    def setUp(self) -> None:
        self.book = Bookstore(10)

    def test_correct_initializing(self):
        self.assertEqual(10, self.book.books_limit)
        self.assertEqual({}, self.book.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book.total_sold_books)

    def test_books_limit_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.book.books_limit = 0
        self.assertEqual('Books limit of 0 is not valid', str(ve.exception))

    def test_len_count_books_in_bookstore(self):
        self.book.receive_book('abc', 2)
        self.assertEqual(2, len(self.book))

    def test_receive_book_not_enough_space_in_the_bookstore(self):
       with self.assertRaises(Exception) as ex:
           self.book.books_limit = 1
           self.book.receive_book('abc', 3)
           self.book.__len__()
       self.assertEqual('Books limit is reached. Cannot receive more books!', str(ex.exception))

    def test_receive_book_enough_space_in_the_bookstore(self):
        self.book.receive_book('abc', 3)
        self.assertEqual({'abc': 3}, self.book.availability_in_store_by_book_titles)

    def test_receive_book_new_availability_return(self):
        self.assertEqual("3 copies of abc are available in the bookstore.", self.book.receive_book('abc', 3))

    def test_receive_book_new_availability_return_in_bookstore(self):
        self.book.receive_book('abc', 1)
        self.assertEqual("4 copies of abc are available in the bookstore.", self.book.receive_book('abc', 3))

    def test_sell_book_not_available_in_the_bookstore(self):
        with self.assertRaises(Exception) as ex:
            self.book.sell_book('abc', 3)
        self.assertEqual("Book abc doesn't exist!", str(ex.exception))

    def test_sell_book_not_enough_copies_book_sell(self):
        self.book.receive_book('abc', 3)
        with self.assertRaises(Exception) as ex:
            self.book.sell_book('abc', 4)
        self.assertEqual("abc has not enough copies to sell. Left: 3", str(ex.exception))

    def test_sell_book_if_can_sell_successfully(self):
        self.book.receive_book('abc', 3)
        self.assertEqual("Sold 3 copies of abc", self.book.sell_book('abc', 3))

    def test_str_result(self):
        self.book.receive_book('abc', 2)
        self.book.sell_book('abc', 2)
        self.assertEqual('Total sold books: 2\n'
                         'Current availability: 0\n'
                         ' - abc: 0 copies', self.book.__str__())


if __name__ == '__main__':
    main()
