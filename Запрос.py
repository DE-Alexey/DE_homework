import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
SELECT id,
       name,
       birthday
FROM job;
''')

for result in cur:
    print(result)
print('-----')
con.commit()

cur.execute('''
SELECT id,
       name,
       birthday
FROM job
LIMIT 3;
''')

for result in cur:
    print(result)
print('-----')
con.commit()

cur.execute('''
SELECT id
FROM job
WHERE post = 'водитель';
''')

for result in cur:
    print(result)
print('-----')
con.commit()

cur.execute('''
SELECT job.id,
       estimation.name
FROM job
LEFT JOIN estimation ON job.estimation_id = estimation.id
WHERE estimation.name = 'D'
      OR estimation.name = 'E';
''')

for result in cur:
    print(result)
print('-----')
con.commit()

cur.execute('''
SELECT MAX(salary)
FROM job
''')

for result in cur:
    print(result)
print('-----')
con.commit()

con.close()
