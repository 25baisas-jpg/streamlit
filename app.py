import streamlit as st
import os

FILE = "students.txt"

# Function to load data
def load_students():
    if not os.path.exists(FILE):
        return []
    
    with open(FILE, "r") as f:
        return f.readlines()

# Function to save student
def add_student(name, marks):
    with open(FILE, "a") as f:
        f.write(f"{name},{marks}\n")

# Function to delete student
def delete_student(name):
    students = load_students()
    with open(FILE, "w") as f:
        for student in students:
            if not student.lower().startswith(name.lower()):
                f.write(student)

# UI
st.title("🎓 Student Management System")

menu = st.sidebar.selectbox("Menu", ["Add Student", "View Students", "Delete Student"])

# Add Student
if menu == "Add Student":
    st.subheader("Add Student")
    name = st.text_input("Enter Name")
    marks = st.text_input("Enter Marks")

    if st.button("Add"):
        add_student(name, marks)
        st.success("Student Added!")

# View Students
elif menu == "View Students":
    st.subheader("Student List")
    students = load_students()

    if students:
        for s in students:
            name, marks = s.strip().split(",")
            st.write(f"Name: {name} | Marks: {marks}")
    else:
        st.warning("No data found")

# Delete Student
elif menu == "Delete Student":
    st.subheader("Delete Student")
    name = st.text_input("Enter Name to Delete")

    if st.button("Delete"):
        delete_student(name)
        st.success("Student Deleted!")
