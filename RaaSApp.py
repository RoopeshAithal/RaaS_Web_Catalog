
import streamlit as app
import snowflake.connector

app.title('RaaS Web Catalog')

my_cnx = snowflake.connector.connect(**app.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
app.text("Hello from Snowflake:")
app.text(my_data_row)
