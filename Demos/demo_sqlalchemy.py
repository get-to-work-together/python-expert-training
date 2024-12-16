from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=True)

Base.metadata.create_all(engine)


from sqlalchemy.orm import Session

with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants"
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
    )
    patrick = User(name="patrick", fullname="Patrick Star")

    session.add_all([spongebob, sandy, patrick])
    session.commit()
