import streamlit as st
import functions
import os

if os.path.exists("todos.txt") == False:
    with open("todos.txt", "w"):
        pass

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("Your Todos")
st.write("""🚀 Jai's ToDo List: Boost Productivity! Effortless organization, customization, and security. Achieve your goals with us. Get started now!""")

st.text_input(label="Add a todo", placeholder="Add a todo", on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()