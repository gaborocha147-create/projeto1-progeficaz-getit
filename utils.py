import json
import os

def load_data(filename):
    with open(os.path.join('static', 'data', filename), 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data

def load_template(filename):
    with open(os.path.join('static', 'templates', filename), 'r', encoding='utf-8') as file:
        template = file.read()
        
    return template

def save_note(titulo, detalhes):
    data = load_data('notes.json')
    data.append({'titulo': titulo, 'detalhes': detalhes})
        
    with open(os.path.join('static', 'data', 'notes.json'), 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)