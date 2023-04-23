import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("Eden Capital - a 6 products store")
st.write("my first page as a student, hope u will enjoy the info the and website!")
st.subheader("Our Team")


col_1,emp_col,col_2,emp_col_1,col_3 = st.columns([1.5,0.5,1.5,0.5,1.5])
df = pandas.read_csv("data_comp.csv")

with col_1:
    for index,row in df[:4].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images_comp/" + row["image"])


with col_2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images_comp/" + row["image"])

with col_3:
    for index, row in df[8:13].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images_comp/" + row["image"])
