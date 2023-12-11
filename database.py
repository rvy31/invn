import mysql.connector
import streamlit as st

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="invn"
    )
    cursor = mydb.cursor()
    mydb.commit()
    print("Database connected successfully")
except Exception as e:
    print(e)
