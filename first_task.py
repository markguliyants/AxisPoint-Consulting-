import requests
import json
import sqlalchemy as s
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime


url = 'https://hubofdata.ru/storage/f/2013-08-18T19%3A58%3A51.196Z/greetings-data.json'
resp = requests.get(url)

text_for_db_json = resp.text

text_for_db = json.loads(text_for_db_json)  # декодируем текст файла из json

month_transform = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12,
}


def month_to_int(date):  # данная функция заменит название месяца на его порядковый номер
    for key, value in month_transform.items():
        date = date.replace(key, str(value))

    return date

for greetings in text_for_db['items']:  # пройдемся по всем ключам словаря
    for key, value in greetings.items():
        if key == 'thedate':  # и найдем ключи 'thedate'
            date = greetings['thedate'].replace(' года', '')  # удалим лишнее слово
            date = month_to_int(date)  # используем функцию для замены на номер месяца
            date = datetime.datetime.strptime(date, '%d %m %Y').date()  # class datetime
            greetings['thedate'] = date  # вернем измененную дату в словарь

conn = s.create_engine('sqlite:///greetings_data.db')
Base = declarative_base()


# БД создал с помощью ORM sqlalchemy
# для удобства, я создал еще одно поле id с autoincrement
class Data(Base):
    __tablename__ = 'greetings_data'
    id = s.Column('id', s.Integer, primary_key=True, autoincrement=True, nullable=False)
    category = s.Column('category', s.String, nullable=False)
    from_column = s.Column('from', s.String, nullable=False)
    title = s.Column('title', s.String, nullable=False)
    text = s.Column('text', s.String, nullable=False)
    date = s.Column('date', s.Date, nullable=False)  # поле с датой храним в таблице как Date
    id_column = s.Column('id_column', s.Integer, nullable=False)

Base.metadata.create_all(conn)

Session = sessionmaker(bind=conn)
session = Session()

for greetings in text_for_db['items']:  # проходим по данным и заполняем бд
    data = [
        Data(category=greetings['category'], from_column=greetings['from'],
        title=greetings['title'], text=greetings['text'],
        date=greetings['thedate'], id_column=greetings['id']),
    ]

    session.add_all(data)
    session.commit()
