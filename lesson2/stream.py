import streamlit as st

# Начальное состояние задач (можно сделать сессией)
if "tasks" not in st.session_state:
    st.session_state.tasks = ["Go to gym"]

st.title("📝 Ülesannete nimekiri")

# --- Lisa uus ülesanne ---
new_task = st.text_input("Sisesta uus ülesanne")
if st.button("➕ Lisa ülesanne") and new_task:
    st.session_state.tasks.append(new_task)
    st.experimental_rerun()

# --- Kuva olemasolevad ülesanded ---
st.subheader("📋 Ülesanded")
for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([6, 1, 1])
    with col1:
        st.write(f"{i+1}. {task}")
    with col2:
        if st.button("❌", key=f"del{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
    with col3:
        if st.button("✏️", key=f"edit{i}"):
            edited = st.text_input("Muuda ülesanne:", value=task, key=f"edit_input_{i}")
            if st.button("Salvesta", key=f"save{i}"):
                st.session_state.tasks[i] = edited
                st.experimental_rerun()
