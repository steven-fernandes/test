import os
import pandas as pd

# File path
file_path = 'kuswar_orders.csv'

# Function to check if the CSV file exists and is not empty
def is_non_empty_csv(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) > 0

# Save orders to a CSV file
def save_order(orders, file_path):
    # Create a DataFrame
    order_df = pd.DataFrame([orders])

    # Check if the CSV file exists and is not empty
    if is_non_empty_csv(file_path):
        # Read CSV to check if we need to write headers
        header = not pd.read_csv(file_path).empty
        order_df.to_csv(file_path, mode='a', header=header, index=False)
    else:
        # If the file doesn't exist or is empty, write with headers
        order_df.to_csv(file_path, mode='w', header=True, index=False)

# Usage in Streamlit
if submitted and orders:
    order_details = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        **orders
    }
    save_order(order_details, file_path)
    st.write("Order submitted successfully!")
    st.write(f"Name: {name}")
    st.write(f"Phone: {phone}")
    st.write(f"Email: {email}")
    for product, option in orders.items():
        st.write(f"{product}: {option}")
