import streamlit as st
import pandas as pd

# Define your products and their options
products = {
    "Kidio": {"price": 600, "sizes": ["200g", "250g", "500g", "1000g"]},
    "Gulio": {"price": 500, "sizes": ["200g", "250g", "500g", "1000g"]},
    "Tukdi": {"price": 360, "sizes": ["200g", "250g", "500g", "1000g"]},
    "Banana Chips": {"price": 440, "sizes": ["200g", "250g", "500g", "1000g"]},
    "Nevri": {"price": 15, "units": ["5nos", "10nos", "15nos", "20nos", "25nos"]},
    "Cookie": {"price": 10, "units": ["5nos", "10nos", "15nos", "20nos", "25nos"]},
    "Rice Laddu": {"price": 15, "units": ["5nos", "10nos", "15nos", "20nos", "25nos"]},
    "Rich Plum Cake": {"price": 400, "sizes": ["250g", "500g", "1000g"]}
}

# Create a form
with st.form("order_form"):
    st.write("### Kuswar Order Form")
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")

    orders = {}
    for product, details in products.items():
        options = details.get("sizes", details.get("units", []))
        selected_option = st.selectbox(f"Select package for {product}", [""] + options, key=product)
        if selected_option:
            orders[product] = selected_option

    submitted = st.form_submit_button("Submit Order")
    if submitted and orders:
        st.write("Order submitted successfully!")
        st.write(f"Name: {name}")
        st.write(f"Phone: {phone}")
        st.write(f"Email: {email}")
        for product, option in orders.items():
            st.write(f"{product}: {option}")
        # Save orders to a CSV file
        order_df = pd.DataFrame([{
            "Name": name,
            "Phone": phone,
            "Email": email,
            **orders
        }])
        order_df.to_csv('kuswar_orders.csv', mode='a', header=not pd.read_csv('kuswar_orders.csv').empty, index=False)

# Optionally show saved orders in the app
if st.checkbox("Show all orders"):
    st.write(pd.read_csv('kuswar_orders.csv'))
