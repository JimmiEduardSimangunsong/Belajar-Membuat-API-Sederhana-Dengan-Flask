class Book:
    BOOKS = [
        {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925},
        {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
        {'id': 3, 'title': '1984', 'author': 'George Orwell', 'year': 1949},
        {'id': 4, 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year': 1813},
        {'id': 5, 'title': 'One Hundred Years of Solitude', 'author': 'Gabriel Garcia Marquez', 'year': 1967}
    ]

    @classmethod
    def get_all(cls):
        return [cls(**book) for book in cls.BOOKS]

    @classmethod
    def get_by_id(cls, book_id):
        for book in cls.BOOKS:
            if book['id'] == book_id:
                return cls(**book)
        return None

    @classmethod
    def create(cls, data):
        book = {'id': cls.get_next_id(), **data}
        cls.BOOKS.append(book)
        return cls(**book)

    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def update(self, data):
        self.title = data.get('title', self.title)
        self.author = data.get('author', self.author)
        self.year = data.get('year', self.year)

    def delete(self):
        Book.BOOKS.remove(self)

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author, 'year': self.year}

    @classmethod
    def get_next_id(cls):
        return max(book['id'] for book in cls.BOOKS) + 1
