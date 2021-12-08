from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///baza.sqlite', echo=True)

base = declarative_base()





# import sqlite3
#
# conn = sqlite3.connect('baza.sqlite')
#
# c = conn.cursor()

# c.execute("CREATE TABLE klienci(data TEXT,id INTEGER,obroty REAL)")
#
# c.execute("INSERT INTO klienci VALUES('2021-12-08',1,258.52)")
# c.execute("INSERT INTO klienci VALUES('2021-12-07',2,4458.52)")
# c.execute("INSERT INTO klienci VALUES('2021-12-06',3,58.52)")
#
# conn.commit()

# for row in c.execute('SELECT * FROM klienci ORDER BY obroty'):
#     print(row)
#
# conn.close()
