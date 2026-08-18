from utils import get_notes, load_template, save_note, delete_note

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados['id'], title=dados['titulo'], details=dados['detalhes'])
        for dados in get_notes()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    save_note(titulo, detalhes)
    
def delete(id):
    delete_note(id)