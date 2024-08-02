import psycopg2
from faker import Faker

conn = psycopg2.connect(
    dbname="task_managment_db", user="igor", password="123", host="localhost", port=5433
)
cursor = conn.cursor()

fake = Faker()

for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email)
    )

statuses = ["new", "in progress", "completed"]
for status in statuses:
    cursor.execute("INSERT INTO status (name) VALUES (%s)", (status,))

# Заповнення таблиці tsks
for _ in range(30):
    title = fake.sentence(nb_words=6)
    description = fake.text()
    status_id = fake.random_int(min=1, max=len(statuses))
    user_id = fake.random_int(min=1, max=10)
    cursor.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, status_id, user_id),
    )

conn.commit()
cursor.close()
conn.close()
