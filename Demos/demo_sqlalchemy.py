from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"



engine = create_engine("sqlite:///example.db", echo=True)

Base.metadata.create_all(engine)




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

    user = User(name="Peter", fullname="Peter Anema")
    session.add(user)
    session.commit()

    retieved = session.query(User).all()
    for user in retieved:
        print(user)


    user = session.get(User, 7)
    print(user)

    retieved = session.query(User).where(User.name == 'Peter')
    for user in retieved:
        print(user)

    retieved = session.query(User).filter(User.name == 'Peter')
    for user in retieved:
        print(user)




