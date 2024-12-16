from src.persistence import user_persistence
from src.persistence import book_persistence


if __name__ == '__main__':

    user_persistence.create_database_and_tables()
    book_persistence.create_database_and_tables()

    user_persistence.seed()
    book_persistence.seed()
