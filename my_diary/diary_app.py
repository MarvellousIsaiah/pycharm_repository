from my_diary.my_diary_test import Diary


class IncorrectPasswordException:
    def __init__(self, message):
        super().__init__(message)


class EntryIdNotFoundException:
    def __init__(self, message):
        super().__init__(message)


class NoSuchDiaryException:
    def __init__(self, message):
        super().__init__(message)


class TestDiaryInMain:
    diary = Diary("Marvy", "1234")

    def main_app(self):
        while True:
            try:
                self.print("oops diary is locked >>>>>>")
                pin = input("enter your pin")
                self.diary.unlock(pin)
                self.print("welcome to Marvy Diary")
                self.display_menu()
                self.print("please kindly enter your options")
                option = int(input())
                self.options(option)
                self.lock_diary()
            except (ValueError, IncorrectPasswordException, EntryIdNotFoundException, NoSuchDiaryException) as e:
                self.print(
                    f"there was an exception of type {e} know what you are doing, all protocols is duly observed oga")
                self.main_app()

    def main_app_while_locked(self):
        self.print("do you want to unlock your diary")
        reply = input()
        if reply.lower() == "yes":
            self.unlock_diary()
            self.main_app()
        self.display_menu()
        self.print("please kindly enter your options")
        option = int(input())
        self.options(option)

    def lock_diary(self):
        self.print("do you want to lock your diary")
        reply = input()
        if reply.lower() == "yes":
            self.diary.lock_diary()
        self.display_menu()
        option = int(input())
        self.options(option)

    @staticmethod
    def print(message):
        print(message)

    @staticmethod
    def display_menu():
        print("""
        enter 1 to create an entry
        enter 2 to find an entry
        enter 3 to update an entry
        enter 4 to delete an entry
        enter 5 to unlock diary
        """)

    def options(self, option):
        try:
            if self.is_valid(option) and not self.diary.is_locked():
                if option == 1:
                    self.create_entry()
                elif option == 2:
                    self.find_entry()
                elif option == 3:
                    self.update_entry()
                elif option == 4:
                    self.delete_entry()
                elif option == 5:
                    self.unlock_diary()
        except (ValueError, IncorrectPasswordException, EntryIdNotFoundException, NoSuchDiaryException) as e:
            self.print("know what you are doing all protocols is duly observed oga")
            self.main_app()

    @staticmethod
    def is_valid(option):
        if option < 0 or option > 5:
            raise ValueError("oga enter a valid option")
        else:
            return True

    def create_entry(self):
        self.print("enter the title of your entry")
        entry_title = input()
        self.print("enter the body of your entry")
        entry_body = input()
        self.diary.create_entry(entry_title, entry_body)
        self.print("your entry is successfully created")

    def find_entry(self):
        self.print("enter the id of the entry you will like to search")
        entry_to_find = int(input())
        entry = self.diary.find_entry(entry_to_find)
        self.print(str(entry))

    def update_entry(self):
        self.print("enter the id of the entry you will like to update")
        entry_to_be_updated = int(input())
        self.print("enter the new title")
        new_title = input()
        self.print("enter the new body")
        new_body = input()
        self.diary.update_entry(entry_to_be_updated, new_title, new_body)
        self.print("your diary has been updated successfully")
        self.print(str(self.diary.find_entry(entry_to_be_updated)))

    def delete_entry(self):
        self.print("enter the id of the entry you will like to be deleted")
        entry_to_be_deleted = int(input())
        self.diary.delete_entry(entry_to_be_deleted)
        self.print("your entry has been successfully deleted")

    def unlock_diary(self):
        self.print("enter your pin")
        pin = input()
        self.diary.unlock(pin)
        if self.diary.is_locked():
            self.main_app()


test_my_diary = TestDiaryInMain()
test_my_diary.main_app()
