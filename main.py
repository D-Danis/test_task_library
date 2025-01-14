import json
import os



class Book:
    """
    Класс, представляющий книгу в библиотеке.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Статус книги ("в наличии", "выдана").

    Методы:
        to_dict() -> dict: Преобразует объект книги в словарь для сохранения.
    """
    
    def __init__(self, id, title, author, year, status='в наличии'):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

class LibraryManagementSystem:
    """
    Класс, представляющий библиотеку.

    Атрибуты:
        filename (str): Имя файла для хранения данных.
        books (list): Список книг в библиотеке.

    Методы:
        load_books() -> list: Загружает книги из JSON-файла.
        save_books(): Сохраняет книги в JSON-файл.
        add_book(title: str, author: str, year: int): Добавляет новую книгу в библиотеку.
        remove_book(book_id: int): Удаляет книгу по идентификатору.
        search_books(query: str) -> list: Находит книги по названию, автору или году.
        display_books(): Выводит список всех книг в библиотеке.
        change_status(book_id: int, new_status: str): Изменяет статус книги.
    """
    
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            return [Book(**book) for book in json.load(open(self.filename))]
        return []

    def save_books(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        id = len(self.books) + 1
        new_book = Book(id, title, author, year)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                self.save_books()
                return
        raise ValueError(f'Книга с ID {id} не найдена.')

    def search_books(self, query):
        results = [book for book in self.books if query.lower() in book.title.lower() or
                   query.lower() in book.author.lower() or
                   query.lower() in str(book.year)]
        return results

    def display_books(self):
        for book in self.books:
            print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}')

    def change_status(self, id, new_status):
        for book in self.books:
            if book.id == id:
                if new_status in ['в наличии', 'выдана']:
                    book.status = new_status
                    self.save_books()
                    return
                else:
                    print('Статус должен быть "в наличии" или "выдана".')
                    return
        raise ValueError(f'Книга с ID {id} не найдена.')

def main():
    library = LibraryManagementSystem()
    while True:
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)
        elif choice == '2':
            id = int(input("Введите ID книги для удаления: "))
            library.remove_book(id)
        elif choice == '3':
            query = input("Введите название, автора или год для поиска: ")
            results = library.search_books(query)
            for book in results:
                print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}')
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.change_status(id, new_status)
        elif choice == '0':
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == '__main__':
    main()