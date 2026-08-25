from utils import get_notes, load_template, save_note, delete_note, get_note, update_note, favoritar

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados['id'], title=dados['title'], details=dados['content'], favorite_class='fas' if dados['favorite'] else 'far')
        for dados in get_notes()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    save_note(titulo, detalhes)
    
def delete(id):
    delete_note(id)
    
def edit(id):
    note = get_note(id)
    if note:
        template = load_template('edit_note.html')
        return template.replace('{note_id}', str(note['id'])) \
                       .replace('{titulo}', note['title']) \
                       .replace('{detalhes}', note['content'])
    return 'Nota não encontrada', 404

def update(id, titulo, detalhes):
    update_note(id, titulo, detalhes)
    
def favorite(id):
    favoritar(id)