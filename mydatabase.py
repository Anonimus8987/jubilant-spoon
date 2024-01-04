import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Создание таблицы "students"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade TEXT
    )
''')
conn.commit()

# Вставка нескольких записей в таблицу "students"
students_data = [
    ('Alice', 20, 'A'),
    ('Bob', 22, 'B'),
    ('Charlie', 21, 'C'),
    ('David', 19, 'B+')
]

cursor.executemany('''
    INSERT INTO students (name, age, grade) VALUES (?, ?, ?)
''', students_data)
conn.commit()

# Функция для получения информации о студенте по имени
def get_student_by_name(student_name):
    cursor.execute('''
        SELECT name, age, grade FROM students WHERE name = ?
    ''', (student_name,))
    result = cursor.fetchone()
    if result:
        return result
    else:
        return f"Студент с именем '{student_name}' не найден."

# Функция для обновления оценки студента
def update_student_grade(student_name, new_grade):
    cursor.execute('''
        UPDATE students SET grade = ? WHERE name = ?
    ''', (new_grade, student_name))
    conn.commit()
    if cursor.rowcount > 0:
        return f"Оценка студента '{student_name}' успешно обновлена."
    else:
        return f"Студент с именем '{student_name}' не найден."

# Функция для удаления студента
def delete_student(student_name):
    cursor.execute('''
        DELETE FROM students WHERE name = ?
    ''', (student_name,))
    conn.commit()
    if cursor.rowcount > 0:
        return f"Студент '{student_name}' успешно удален."
    else:
        return f"Студент с именем '{student_name}' не найден."

# Пример использования функций
print(get_student_by_name('Alice'))
print(update_student_grade('Bob', 'A-'))
print(delete_student('Charlie'))

# Закрытие соединения с базой данных
conn.close()
