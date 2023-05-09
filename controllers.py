from models import Book

class BookController:
    @staticmethod
    def get_all():
        return [book.to_dict() for book in Book.get_all()]

    @staticmethod
    def get_by_id(book_id):
        book = Book.get_by_id(book_id)
        if book:
            return book.to_dict()
        else:
            return None

    @staticmethod
    def create(data):
        book = Book.create(data)
        return book

    @staticmethod
    def update(book_id, data):
        book = Book.get_by_id(book_id)
        if book:
            book.update(data)
            return book.to_dict()
        else:
            return None
