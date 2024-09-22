import streamlit as pr
import fn_begin

todos = fn_begin.do_todos()


def to_add():
    add_new = pr.session_state["new_todo"] + '\n'
    todos.append(add_new)
    fn_begin.write_todos(todos)


pr.title('My Todo App')
pr.subheader('What to do? Write it!')

for index,item in enumerate(todos):
    checkbox = pr.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        fn_begin.write_todos(todos)
        del pr.session_state[item]
        pr.rerun()

pr.text_input(label='', placeholder='Add a todo...', on_change=to_add, key='new_todo')