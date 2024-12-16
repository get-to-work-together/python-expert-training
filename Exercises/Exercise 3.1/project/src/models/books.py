from dataclasses import dataclass

class Book:

    fields = ['id', 'title', 'author', 'year']

    def __init__(self, id: int = None, title: str = None, author: str = None, year: int = None):
        self.id: int = id
        self.title: str = title
        self.author: str = author
        self.year: int = year

    def __repr__(self):
        return f'Book("{self.title}")'

    def to_dict(self, fields = None):
        if fields is None:
            fields = Book.fields
        return {field: getattr(self, field) for field in fields}
