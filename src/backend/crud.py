import sqlite3
from pathlib import Path
from model import User

DB_PATH = Path("./database/app.db")

def init_user():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id              INTEGER PRIMARY KEY,
            email           TEXT NOT NULL UNIQUE,
            password_hash   TEXT NOT NULL,
            name            TEXT NOT NULL,
            student_id      TEXT UNIQUE,
            department      TEXT,
            created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def init_carpool():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE carpool (
            id              SERIAL PRIMARY KEY,
            poster_id       INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            origin          VARCHAR(100) NOT NULL,
            destination     VARCHAR(100) NOT NULL,
            departure_time  TIMESTAMP NOT NULL,
            seats_total     SMALLINT NOT NULL CHECK (seats_total > 0),
            seats_left      SMALLINT NOT NULL CHECK (seats_left >= 0),
            cost            INTEGER DEFAULT 0,
            note            TEXT,
            status          VARCHAR(10) NOT NULL DEFAULT 'open'
                            CHECK (status IN ('open', 'full', 'closed', 'cancelled')),
            created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
            updated_at      TIMESTAMP NOT NULL DEFAULT NOW(),
            CHECK (seats_left <= seats_total)
        );
    """)
    conn.commit()
    conn.close()

def email_exist(email: str):
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            f"SELECT EXISTS(SELECT 1 FROM user WHERE email = ?)",
            (email,)
        )
        return bool(cur.fetchone()[0])
    finally:
        conn.close()

def create_user(user: User):
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.execute(
            """
            INSERT INTO user (email, password_hash, name, student_id, department)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user.email, user.password_hash, user.name, user.student_id, user.department),
        )
        conn.commit()
        user.id = cursor.lastrowid   # 取得資料庫產生的 id 並寫回物件
        return user
    finally:
        conn.close()

