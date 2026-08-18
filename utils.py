import sqlite3
import os

DB_PATH = 'banco.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def load_template(filename):
    with open(os.path.join('static', 'templates', filename), 'r', encoding='utf-8') as file:
        template = file.read()
        
    return template

def save_note(titulo, detalhes):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (titulo, detalhes) VALUES (?, ?)', (titulo, detalhes))
    conn.commit()
    conn.close()
    
def get_notes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT titulo, detalhes FROM notes ORDER BY id ASC')
    notes = cursor.fetchall()
    conn.close()
    return [{'titulo': note['titulo'], 'detalhes': note['detalhes']} for note in notes]