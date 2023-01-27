import streamlit
import streamlit as sl
import app_functions

def add_todo():
    todo = sl.session_state["new_todo"]
    todos.append(todo + "\n")
    app_functions.save_todos(todos)

todos = app_functions.get_todos()

sl.set_page_config(layout="wide")

sl.title("Lista Zadań by Michał Mironowicz")
sl.subheader("Totalnie umiem programowac")
sl.write("Kaja obczaj temat")

sl.text_input(label="",placeholder="Napisz cos, jak chcesz lol nic na sile dobra elo",
              key="new_todo", on_change=add_todo)

for index, item in enumerate(todos):
    checkbox = sl.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        app_functions.save_todos(todos)
        del sl.session_state[item]
        streamlit.experimental_rerun()

