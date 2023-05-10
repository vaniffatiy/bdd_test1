from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:mypassword@localhost:5432/mydatabase2')

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age})>"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

user = User(name='John', age=30)
session.add(user)
session.commit()

# получение списка пользователей
users = session.query(User).all()
print(users)

# изменение возраста пользователя
user = session.query(User).filter_by(name='John').first()
user.age = 31
session.commit()

session.delete(user)
session.commit()

session.close()



