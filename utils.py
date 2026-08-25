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
    cursor.execute('INSERT INTO note (title, content) VALUES (?, ?)', (titulo, detalhes))
    conn.commit()
    conn.close()
    
def get_notes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content, favorite FROM note ORDER BY favorite DESC, id ASC')
    notes = cursor.fetchall()
    conn.close()
    return [{'id': note['id'], 'title': note['title'], 'content': note['content'], 'favorite': note['favorite']} for note in notes]

def delete_note(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM note WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def get_note(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content FROM note WHERE id = ?', (id,))
    note = cursor.fetchone()
    conn.close()
    if note:
        return {'id': note['id'], 'title': note['title'], 'content': note['content']}
    return None

def update_note(id, new_title, new_detalhes):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE note SET title = ?, content = ? WHERE id = ?', (new_title, new_detalhes, id))
    conn.commit()
    conn.close()
    
def favoritar(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT favorite FROM note WHERE id = ?', (id,))
    row = cursor.fetchone()
    if row:
        novo_valor = 0 if row['favorite'] else 1
        cursor.execute('UPDATE note SET favorite = ? WHERE id = ?', (novo_valor, id))
        conn.commit()
    conn.close()