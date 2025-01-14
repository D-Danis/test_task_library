import unittest
import json
import os
from main import Book, LibraryManagementSystem  

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book(1, "Гарри Поттер", "J.K. Rowling", 1997)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Гарри Поттер")
        self.assertEqual(book.author, "J.K. Rowling")
        self.assertEqual(book.year, 1997)
        self.assertEqual(book.status, "в наличии")

    def test_to_dict(self):
        book = Book(1, "Гарри Поттер", "J.K. Rowling", 1997)
        self.assertEqual(book.to_dict(), {
            "id": 1,
            "title": "Гарри Поттер",
            "author": "J.K. Rowling",
            "year": 1997,
            "status": "в наличии"
        })


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создаем временный файл для тестирования"""
        self.library = LibraryManagementSystem("test_library.json")
        self.library.books = []  # 

    def tearDown(self):
        """Удаляем временный файл после тестов"""
        if os.path.exists("test_library.json"):
            os.remove("test_library.json")

    def test_add_book(self):
        self.library.add_book("Гарри Поттер", "J.K. Rowling", 1997)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Гарри Поттер")

    def test_remove_book(self):
        self.library.add_book("Гарри Поттер", "J.K. Rowling", 1997)
        self.assertEqual(len(self.library.books), 1)
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_remove_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library.remove_book(99)

    def test_search_books(self):
        self.library.add_book("Гарри Поттер", "J.K. Rowling", 1997)
        results = self.library.search_books("Гарри Поттер")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Гарри Поттер")

    def test_display_books(self):
        self.library.add_book("Гарри Поттер", "J.K. Rowling", 1997)
        try:
            self.library.display_books()
        except Exception:
            self.fail("display_books raised an exception unexpectedly!")

    def test_change_status(self):
        self.library.add_book("Гарри Поттер", "J.K. Rowling", 1997)
        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")
        
    def test_change_status_nonexistent(self):
        with self.assertRaises(ValueError): 
            self.library.change_status(99, "выдана")
    


if __name__ == "__main__":
    unittest.main()
    # python3 -m unittest test_main.py