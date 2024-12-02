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
cursor.execute('DELETE FROM Users WHERE id = ?', ('6',))   # Удаление записи с id = 6

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()                         # Всего записей
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()                        # Сумма балансов

print('Средний баланс',all_balances[0]/total_users[0])

connection.commit()
connection.close()