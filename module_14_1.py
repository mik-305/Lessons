import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(10):           # цикл из 10 повторов
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i + 1}', f'example{i + 1}@gmail.com', f'{(i + 1) * 10}', '1000'))

for i in range(10):
    if (i+1)%2 != 0:
        cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i + 1}'))

for i in range(10):
    if i%3 == 0:
        cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i + 1}',))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (f'{60}',))
rows = cursor.fetchall()
for result in rows:
    print(f'Имя: {result[0]} |'+f' Почта: {result[1]} | '+f' Возраст: {result[2]} | '+f' баланс>: {result[3]} ')
connection.commit()
connection.close()