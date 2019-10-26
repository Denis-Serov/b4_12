import datetime
#import uuid

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):
    """
    Описывает структуру таблицы athelete, содержащую данные об атлетах
    """
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """

    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    print("Ввод нового пользователя в  sochi_athletes.sqlite3")
    first_name = input("НЕВАЖНО Введите своё имя: ")
    last_name = input("НЕВАЖНО Фамилию: ")
    gender = input("НЕВАЖНО Пол? (Male, Female) ")
    email = input("НЕВАЖНО Адрес электронной почты: ")
    birthdate = input("ВАЖНО! Дата рождения в формате ГГГГ-ММ-ДД. Например, 2020-01-01: ")
    height = input("ВАЖНО! Рост в метрах? ( для разделения целых чисел и долей нужна ТОЧКА)")
    #user_id = str(uuid.uuid4())
    user = User(
    	#id = user_id,
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user

def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Ваши данные сохранены. Ваш id: {}, запомните его для ввода в find_athelete.py Спасибо!".format(user.id))


if __name__ == "__main__":
    main()