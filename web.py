import streamlit as st
import functions

todos = functions.getTodos()

def add_todo():
  todo = st.session_state['new_todo'] + '\n'
  todos.append(todo)
  functions.postTodos(todos)
  st.session_state['new_todo'] = ''

st.title('My Todo App')

for index, todo in enumerate(todos):
  checkbox = st.checkbox(todo, key=todo)
  if checkbox:
    todos.pop(index)
    functions.postTodos(todos)
    del st.session_state[todo]
    st.rerun()
  
st.text_input(label='Enter new todo:', placeholder='Add new todo...', on_change=add_todo, key='new_todo')
