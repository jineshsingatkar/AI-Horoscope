# database.py
import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("horoscope.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS horoscope (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rashi_id INTEGER,
            date TEXT,
            prediction TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_prediction(rashi_id, prediction):
    today = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect("horoscope.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO horoscope (rashi_id, date, prediction)
        VALUES (?, ?, ?)
        ON CONFLICT(date) DO UPDATE SET prediction = excluded.prediction
    ''', (rashi_id, today, prediction))
    conn.commit()
    conn.close()

def get_predictions(rashi_id):
    conn = sqlite3.connect("horoscope.db")
    c = conn.cursor()
    c.execute('SELECT date, prediction FROM horoscope WHERE rashi_id=? ORDER BY date DESC LIMIT 30', (rashi_id,))
    rows = c.fetchall()
    conn.close()
    return {row[0]: row[1] for row in rows}