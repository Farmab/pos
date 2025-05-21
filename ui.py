import streamlit as st
import auth
import tables
import delivery
import takeout
import report

def run_app():
    st.set_page_config(page_title="Restaurant POS System", layout="wide")
    st.title("🍽️ Restaurant POS System")

    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        with st.form("login"):
            st.subheader("🔐 Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                if auth.login(username, password):
                    st.session_state.authenticated = True
                    st.success("Logged in successfully!")
                else:
                    st.error("Invalid credentials")
        return

    # Sidebar menu
    menu = st.sidebar.radio("📋 Menu", ["Tables", "Delivery", "Takeout", "Reports"])

    if menu == "Tables":
        st.header("🍽️ Dine-In Orders")
        table_id = st.text_input("Table Number")
        order = st.text_area("Enter Order")
        if st.button("Submit Table Order"):
            tables.handle_table_order(table_id, order)
            st.success("Order sent!")

    elif menu == "Delivery":
        st.header("🚚 Delivery Orders")
        company = st.selectbox("Select Delivery Company", ["FastExpress", "HungerNow", "DeliverIt"])
        order = st.text_area("Enter Order")
        if st.button("Submit Delivery Order"):
            delivery.handle_delivery(company, order)
            st.success("Order sent to company!")

    elif menu == "Takeout":
        st.header("🥡 Takeout Orders")
        order = st.text_area("Enter Takeout Order")
        if st.button("Submit Takeout"):
            takeout.handle_takeout(order)
            st.success("Takeout order registered!")

    elif menu == "Reports":
        st.header("📊 Reports & Revenue")
        report_data = report.generate_report()
        st.write(report_data)
