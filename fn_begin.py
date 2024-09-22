FILEPATH = 'task.txt'


def do_todos(filepath= FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='task.txt'):
    with open(filepath, 'w') as file_loc:
        file_loc.writelines(todos_arg)