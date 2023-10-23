import streamlit as st
import functions
import os

if os.path.exists("todos.txt") == False:
    with open("todos.txt", "w"):
        pass

todos = functions.get_todos()

st.title("Your Todos")
st.write("""🚀 Jai's ToDo List: Boost Productivity! Effortless organization, customization, and security. Achieve your goals with us. Get started now!""")

st.text_input(label="", placeholder="Add a todo")

for todo in todos:
    st.checkbox(todo)