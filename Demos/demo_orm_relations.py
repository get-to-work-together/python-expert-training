from typing import List
from sqlalchemy.orm import Mapped, DeclarativeBase
from sqlalchemy.orm import relationship


class User(DeclarativeBase):
    __tablename__ = "user_account"

    # ... mapped_column() mappings

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")


class Address(DeclarativeBase):
    __tablename__ = "address"

    # ... mapped_column() mappings

    user: Mapped["User"] = relationship(back_populates="addresses")