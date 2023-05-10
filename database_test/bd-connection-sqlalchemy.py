from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData


engine = create_engine('postgresql://postgres:mypassword@localhost:4532/mydatabase2')
metadata = MetaData()
mytable = Table('Fruit', metadata,
                Column('id', Integer, primary_key=True),
                Column('Yellow', String),
                Column('Red', String))
conn = engine.connect()
session = conn.begin()
conn.execute(mytable.insert(), [{'Yellow': 'banana', 'Red': 'apple'}])
session.commit()
conn.close()
