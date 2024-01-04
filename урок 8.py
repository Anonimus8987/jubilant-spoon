import sqlite3
import hashlib

# Создание подключения к базе данных
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Создание таблицы клиентов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        phone_number TEXT UNIQUE,
        password TEXT,
        balance REAL DEFAULT 0
    )
''')
conn.commit()

# Функция для регистрации нового клиента
def register():
    full_name = input('Введите ваше полное имя: ')
    phone_number = input('Введите номер телефона: ')
    password = hashlib.sha256(input('Введите пароль: ').encode()).hexdigest()

    cursor.execute('''
        INSERT INTO clients (full_name, phone_number, password) 
        VALUES (?, ?, ?)
    ''', (full_name, phone_number, password))
    conn.commit()
    print('Регистрация успешна!')

# Пример использования функции регистрации
register()

# Закрытие соединения с базой данных
conn.close()
