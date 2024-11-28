import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load credentials and create a client
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_service_account.json', scope)
client = gspread.authorize(creds)

# Open the spreadsheet
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1fjIgUcN7BY89O1UZW-csBgOHR-31QD_gifYKJNQTMyQ/edit?usp=sharing').sheet1

# Streamlit form for data entry
with st.form("order_form"):
    st.write("### Kuswar Order Form")
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Submit Order")
    if submitted:
        # Update Google Sheet
        sheet.append_row([name, phone, email])
        st.success("Order submitted successfully!")

# Optionally view the data submitted
if st.button('Show Orders'):
    data = sheet.get_all_records()
    st.write(data)
