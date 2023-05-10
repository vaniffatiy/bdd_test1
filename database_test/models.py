from peewee import *

db = PostgresqlDatabase('my_database2', user='postgres', password='mypassword',
                        host='localhost', port=5432)


class User(Model):
    username = CharField()
    email = CharField()

    class Meta:
        database = db
