
import unittest
from exercises.PhoneBook import PhoneBook

class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.phone_book = PhoneBook()
        self.phone_book.add_contact("Marvellous", "1234567890")
        self.phone_book.add_contact("Boby", "9876543210")

    def test_add_contact(self):
        self.phone_book.add_contact("Charlie", "5555555555")
        self.assertIn("Charlie", self.phone_book.contacts)
        self.assertEqual(self.phone_book.contacts["Charlie"], "5555555555")

    def test_edit_contact(self):
        self.phone_book.edit_contact("Marvellous", "0000000000")
        self.assertEqual(self.phone_book.contacts["Marvellous"], "0000000000")

    def test_search_contact(self):
        self.assertEqual(self.phone_book.search_contact("Boby"), "Name: Boby, Phone Number: 9876543210")

    def test_delete_contact(self):
        self.phone_book.delete_contact("Boby")
        self.assertNotIn("Boby", self.phone_book.contacts)
