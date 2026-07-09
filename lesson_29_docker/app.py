import psycopg2
import os


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "testdb"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres")
    )


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()


def insert_user(name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", (name, email))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id


def update_user(user_id, name=None, email=None):
    conn = get_connection()
    cur = conn.cursor()
    if name:
        cur.execute("UPDATE users SET name = %s WHERE id = %s", (name, user_id))
    if email:
        cur.execute("UPDATE users SET email = %s WHERE id = %s", (email, user_id))
    conn.commit()
    cur.close()
    conn.close()


def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def get_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


if __name__ == "__main__":
    create_table()
    new_id = insert_user("Yurii Davydiak", "yurii@example.com")
    print(f"Створено користувача з id={new_id}")
    print(get_all_users())