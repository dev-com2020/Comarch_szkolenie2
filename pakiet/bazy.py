from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, REAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///baza.sqlite', echo=True)

base = declarative_base()
base.metadata.create_all(engine)


class Transakcja(base):
    __tablename__ = 'klienci'

    data = Column(String)
    id = Column(Integer, primary_key=True)
    obroty = Column(REAL)

    def __init__(self, data, id, obroty):
        self.data = data
        self.id = id
        self.obroty = obroty


Session = sessionmaker(bind=base.engine)

s = Session()

for i in range(1):
    tr = base.Transakcje('2021-01-20', 3, 123.32)
    s.add(tr)

s.commit()

for i in s.query(base.Transakcje).filter(base.Transakcje.id > 5):
    print(s.tr)

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
