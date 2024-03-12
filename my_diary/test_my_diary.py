from my_diary_test import *
from unittest import TestCase


class DiaryTest(TestCase):
    def test_delete_entry(self):
        diary = Diary("marvy", "mangolong")
        self.assertFalse(diary.is_locked())
        diary.create_entry("a", "b")
        diary.delete_entry(1)
        self.assertEqual(diary.get_number_of_entry(), 0)

    def test_find_entry(self):
        diary = Diary('marvy', '1234')
        diary.create_entry("a", "b")
        entry_to_find = diary.create_entry("b", "c")
        self.assertEqual(entry_to_find, diary.find_entry(2))

    def test_that_we_can_create_entry_in_diary(self):
        diary = Diary("marvy", "1234")
        diary.create_entry("a", "b")
        diary.create_entry("b", "c")
        self.assertEqual(2, diary.get_number_of_entry())

    def test_that_we_can_update_diary(self):
        diary = Diary("marvy", "1234")
        diary.create_entry("a", "b")
        diary.create_entry("b", "c")
        diary.update_entry(2, "new", "new")
        self.assertEqual(diary.find_entry(2).get_body(), "new")

    def test_that_diary_can_be_locked(self):
        diary = Diary("marvy", "1234")
        self.assertFalse(diary.is_locked())
        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def test_that_diary_can_be_unlocked(self):
        diary = Diary("marvy", "1234")
        self.assertFalse(diary.is_locked())
        diary.lock_diary()
        self.assertTrue(diary.is_locked())
        diary.unlock("1234")
        self.assertFalse(diary.is_locked())
