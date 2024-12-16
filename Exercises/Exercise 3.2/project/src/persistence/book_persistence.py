from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete


from ..models.books import Book


engine = create_engine('sqlite:///project.db', echo=True)


class Base(DeclarativeBase):
    pass


class BookDB(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    author: Mapped[str] = mapped_column(String(150))
    year: Mapped[Optional[str]]


book_attributes = ['id', 'title', 'author', 'year']


def from_book(book: Book) -> BookDB:
    d = {attr: getattr(book, attr) for attr in book_attributes}
    return BookDB(**d)


def to_book(bookdb: BookDB) -> Book:
    d = {attr: getattr(bookdb, attr) for attr in book_attributes}
    return Book(**d)


def create_database_and_tables(force = False):
    if force:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def insert_book(book: Book):
    bookDB = from_book(book)
    with Session(engine) as session:
        session.add(bookDB)
        session.commit()


def select_books():
    with Session(engine) as session:
        stmt = select(BookDB)
        return [to_book(bookdb) for bookdb in session.scalars(stmt)]


def select_book_by_id(id_: int):
    with Session(engine) as session:
        stmt = select(BookDB).where(BookDB.id == id_)
        return to_book(session.scalar(stmt))


def select_book_by_title(title: str):
    with Session(engine) as session:
        stmt = select(BookDB).where(BookDB.title == title)
        return to_book(session.scalar(stmt))


def select_book_by_author(author: str):
    with Session(engine) as session:
        stmt = select(BookDB).where(BookDB.author == author)
        return to_book(session.scalar(stmt))


def delete_book_by_id(id_: str):
    with engine.begin() as conn:
        stmt = (delete(BookDB)
                .where(BookDB.id == id_))
        result = conn.execute(stmt)


def update_book(book: Book):
    d = {attr: getattr(book, attr) for attr in book_attributes if attr not in [id]}
    title = book.title
    with engine.begin() as conn:
        stmt = (update(BookDB)
                .where(BookDB.title == title)
                .values(title = book.title,
                        author = book.author,
                        year = book.year))
        result = conn.execute(stmt)


def seed():
    books = [
        {'title': 'Max Havelaar',
         'author': 'Multatuli (Eduard Douwes Dekker)',
         'year': 1860},
        {'title': 'De Avonden',
         'author': 'Gerard Reve',
         'year': 1947},
        {'title': 'Het Diner',
         'author': 'Herman Koch',
         'year': 2009},
        {'title': 'De ontdekking van de hemel',
         'author': 'Harry Mulisch',
         'year': 1992},
        {'title': 'De Aanslag',
         'author': 'Harry Mulisch',
         'year': 1982},
        {'title': 'Kruistocht in spijkerbroek',
         'author': 'Thea Beckman',
         'year': 1973},
        {'title': 'Pluk van de Petteflet',
         'author': 'Annie M.G. Schmidt',
         'year': 1971},
        {'title': 'Brief voor de Koning',
         'author': 'Tonke Dragt',
         'year': 1962},
        {'title': 'Jip en Janneke',
         'author': 'Annie M.G. Schmidt',
         'year': 1952},
        {'title': 'De kleine Johannes',
         'author': 'Frederik van Eeden',
         'year': 1887},
        {'title': 'Pogingen iets van het leven te maken',
         'author': 'Hendrik Groen',
         'year': 2014},
        {'title': 'Oorlogswinter',
         'author': 'Jan Terlouw',
         'year': 1972},
        {'title': 'Zomerhuis met zwembad',
         'author': 'Herman Koch',
         'year': 2011},
        {'title': 'De helaasheid der dingen',
         'author': 'Dimitri Verhulst',
         'year': 2006},
        {'title': 'Het gouden ei',
         'author': 'Tim Krabbé',
         'year': 1984},
        {'title': 'Turks Fruit',
         'author': 'Jan Wolkers',
         'year': 1969},
        {'title': 'Harry Potter en de Steen der Wijzen',
         'author': 'J.K. Rowling',
         'year': 1997},
        {'title': 'Harry Potter en de Geheime Kamer',
         'author': 'J.K. Rowling',
         'year': 1998},
        {'title': 'Harry Potter en de Gevangene van Azkaban',
         'author': 'J.K. Rowling',
         'year': 1999},
        {'title': 'Harry Potter en de Vuurbeker',
         'author': 'J.K. Rowling',
         'year': 2000},
        {'title': 'Harry Potter en de Orde van de Feniks',
         'author': 'J.K. Rowling',
         'year': 2003},
        {'title': 'Harry Potter en de Halfbloed Prins',
         'author': 'J.K. Rowling',
         'year': 2005},
        {'title': 'Harry Potter en de Relieken van de Dood',
         'author': 'J.K. Rowling',
         'year': 2007},
        {'title': 'Harry Potter en het Vervloekte Kind',
         'author': 'J.K. Rowling',
         'year': 2016}
    ]

    for d in books:
        book = Book(**d)
        insert_book(book)
