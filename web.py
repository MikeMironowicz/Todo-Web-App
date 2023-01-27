import streamlit
import streamlit as sl
import app_functions

def add_todo():
    todo = sl.session_state["new_todo"]
    todos.append(todo + "\n")
    app_functions.save_todos(todos)

todos = app_functions.get_todos()

sl.title("Lista Zadań by Michał Mironowicz")
sl.subheader("Który jest bardzo atrakcyjny")
sl.write("i zabawny")

for index, item in enumerate(todos):
    checkbox = sl.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        app_functions.save_todos(todos)
        del sl.session_state[item]
        streamlit.experimental_rerun()

sl.text_input(label="",placeholder="Enter your todo here, or don't."
                                   " Your lazy ass is not my problem.",
              key="new_todo", on_change=add_todo)
