import sqlite3


con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS estimation(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS type(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    manager TEXT NOT NULL,
    count_employees INTEGER NOT NULL
);



CREATE TABLE IF NOT EXISTS job(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    birthday TEXT NOT NULL,
    post TEXT NOT NULL,
    level TEXT NOT NULL,
    salary INTEGER NOT NULL,
    rights INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    estimation_id INTEGER NOT NULL,
    FOREIGN KEY(type_id) REFERENCES type(id),
    FOREIGN KEY(estimation_id) REFERENCES estimation(id)
);
''')

con.commit()

job = [
    (1, 'Николев НН', '01.01.1999', 'инженер', 'jun', 20000, 0, 1, 3),
    (2, 'Иванов ИИ', '05.11.1990', 'инженер', 'middle', 30000, 1, 2, 4),
    (3, 'Бут АВ', '11.12.1979', 'инженер', 'middle', 50000, 1, 2, 1),
    (4, 'Сюр ВВ', '08.03.1994', 'инженер', 'middle', 40000, 1, 1, 1),
    (5, 'Послед ЕН', '01.04.1997', 'водитель', 'middle', 30000, 1, 2, 5)
]

type = [
    (1, 'Info', 'Сюр ВВ', 3),
    (2, 'IT', 'Бут АВ', 2)
]

estimation = [
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'D'),
    (5, 'E')
]
cur.executemany('INSERT INTO type VALUES(?, ?, ?, ?);', type)
cur.executemany('INSERT INTO estimation VALUES(?, ?);', estimation)
cur.executemany('INSERT INTO job VALUES(?, ?, ?,?, ?, ?,?, ?, ?);', job)

con.commit()


con.close()
