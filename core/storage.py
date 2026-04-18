import sqlite3
import os

DB_FILE = "data/expenses.db"


def connect():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_FILE)


def init_storage():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_expense(expense):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (
        expense.amount,
        expense.category,
        expense.description,
        expense.date
    ))

    conn.commit()
    conn.close()


def load_expenses():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, amount, category, description, date
        FROM expenses
        ORDER BY id DESC
    """)

    rows = cur.fetchall()
    conn.close()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "amount": row[1],
            "category": row[2],
            "description": row[3],
            "date": row[4]
        })

    return result


def delete_expense(expense_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    conn.commit()
    conn.close()


def update_expense(expense_id, amount, category, description):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, description = ?
        WHERE id = ?
    """, (amount, category, description, expense_id))

    conn.commit()
    conn.close()