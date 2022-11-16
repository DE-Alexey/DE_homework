import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
SELECT name
FROM job
ORDER BY salary DESC
LIMIT 1;
''')

for result in cur:
    print(result)
print('-----')
con.commit()

cur.execute('''
SELECT name
FROM job
ORDER BY name;
''')

for result in cur:
    print(result)
print('-----')
con.commit()

cur.execute('''
SELECT j.name,
       t.name
FROM job AS j
LEFT JOIN type AS t ON j.type_id = t.id;
''')

for result in cur:
    print(result)
print('-----')
con.commit()

cur.execute('''
SELECT j.name,
       t.name,
       MAX(j.salary)
FROM job AS j
LEFT JOIN type AS t ON j.type_id = t.id
GROUP BY t.name;
''')

for result in cur:
    print(result)
print('-----')
con.commit()

con.close()
