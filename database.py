# database.py
import sqlite3
from datetime import datetime

def migrate_db():
    """Migrate existing database to add unique constraint if needed"""
    conn = sqlite3.connect("horoscope.db")
    c = conn.cursor()
    
    # Check if the unique constraint exists
    c.execute("PRAGMA table_info(horoscope)")
    columns = c.fetchall()
    
    # Check if we need to recreate the table with unique constraint
    c.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='horoscope'")
    result = c.fetchone()
    
    if result and 'UNIQUE(rashi_id, date)' not in result[0]:
        # Backup existing data
        c.execute("SELECT * FROM horoscope")
        backup_data = c.fetchall()
        
        # Drop old table
        c.execute("DROP TABLE IF EXISTS horoscope")
        
        # Create new table with unique constraint
        c.execute('''
            CREATE TABLE horoscope (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rashi_id INTEGER,
                date TEXT,
                prediction TEXT,
                UNIQUE(rashi_id, date)
            )
        ''')
        
        # Restore data, handling duplicates
        for row in backup_data:
            try:
                c.execute('''
                    INSERT OR REPLACE INTO horoscope (id, rashi_id, date, prediction)
                    VALUES (?, ?, ?, ?)
                ''', row)
            except sqlite3.Error:
                # Skip duplicate entries
                continue
    
    conn.commit()
    conn.close()

def init_db():
    conn = sqlite3.connect("horoscope.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS horoscope (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rashi_id INTEGER,
            date TEXT,
            prediction TEXT,
            UNIQUE(rashi_id, date)
        )
    ''')
    conn.commit()
    conn.close()
    
    # Run migration for existing databases
    migrate_db()

def save_prediction(rashi_id, prediction):
    today = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect("horoscope.db")
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO horoscope (rashi_id, date, prediction)
            VALUES (?, ?, ?)
            ON CONFLICT(rashi_id, date) DO UPDATE SET prediction = excluded.prediction
        ''', (rashi_id, today, prediction))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()
    finally:
        conn.close()

def get_predictions(rashi_id):
    conn = sqlite3.connect("horoscope.db")
    c = conn.cursor()
    try:
        c.execute('SELECT date, prediction FROM horoscope WHERE rashi_id=? ORDER BY date DESC LIMIT 30', (rashi_id,))
        rows = c.fetchall()
        return {row[0]: row[1] for row in rows}
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return {}
    finally:
        conn.close()