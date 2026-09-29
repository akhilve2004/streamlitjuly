import streamlit as st
from datetime import date


n=st.text_input("Name")
a=st.number_input("Age",min_value=0)
d=st.date_input("DOB",
                min_value=date(1990,1,1),
                max_value=date.today(),
                value=date(2006,1,1))
e=st.text_input("Email")

g=st.radio( "Gender",['male','female'])
c=st.selectbox("Courses",['python','dotnet','java'])

b=st.button("Register")

if b:
    st.write("Name",n)
    st.write("Age",a)
    st.write("DateOfBirth",d)
    st.write("Email",e)
    st.write("Gender",g)
    st.write("Course",c)
