import os

def get_todo_upload_path(instane, filename):
    return os.path.join(
        'product',
        str(instane.todo.id),
        filename
    )