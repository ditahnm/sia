import streamlit as st
import plotly.graph_objects as go


import calendar
from datetime import datetime

from streamlit_option_menu import option_menu
import plotly.graph_objects as go

# -------------- SETTINGS --------------
incomes = ["Pemesanan Kamar Kos", "Pemasukkan Lainnya"]
expenses = ["Air", "Listrik", "Wi-Fi", "Gas" ]
currency = "Rp."
page_title = "SILOKOS (_SISTEM PENGELOLAAN KOS_)"
page_icon = ":money_with_wings:"  
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])


with st.sidebar:
        selected = option_menu(
        menu_title=None, 
        options=["Home", "Income and Expense", "Income and Expense Tracker"],
        icons=["house-door", "cash-stack", "file-bar-graph"]  
    )

if selected == "Home":
    from PIL import Image
    image = Image.open('logofixx.png')
    st.image(image, caption='SILOKOS (SISTEM PENGELOLAAN KOS)') 

    st.write('SILOKOS (_SISTEM PENGELOLAAN KOS_) merupakan suatu sistem informasi yang menyediakan fitur mengenai keluar masuknya pendanaan dari kos yang dapat membantu anda untuk mengelola keuangan dari hasil pendapatan kos. Pada sistem ini terdapat Income, Expense, Income Expense Tracker sehingga anda dengan mudah memasukkan data keuangan dari hasil pendapatan kos. Dengan adanya sistem ini tidak ada lagi kesulitan dalam mengelola keuangan.')


elif selected == "Income and Expense":
    st.header(f" Enter your {selected} here!")
    with st.form("income and expense form", clear_on_submit=True):
        col1, col2 = st.columns (2)
        col1.selectbox( "Select Month:", months, key ="month")
        col2.selectbox( "Select Years:", years, key ="year")
        "---"
        with st.expander("Calculate your income"):
                name = st.text_input("Nama Pemesan: ")
                hp = st.text_input("Nomor HP Pemesan: ")
                address = st.text_input("Alamat Pemesan: ")
                date = st.date_input("Tanggal Pemesanan: ")
                st.write ("             PEMILIHAN KAMAR KOS                              ")
                st.write (" Kode Kamar ; Nama Kama Kamar ;            Fasilitas Kamar           ;       Harga      ")
                st.write ("     1      ;    VIP Room     ;      AC, TV, Water Heater, Carport   ;      1650000     ")
                st.write ("     2      ;    Deluxe Room  ;                  AC, TV              ;      1450000     ")
                st.write ("     3      ;    Suite Room   ;                   AC                 ;      1250000     ")

                kodekamar = st.text_input ("Masukkan Kode Kamar")
                jml = st.number_input ("Masukkan Jumlah Pesanan Kamar",0)
                total = st.form_submit_button ("Pemasukkan yang diperoleh")
                if total :
                    total = kodekamar*jml
                if kodekamar == "1":
                    total = 16500000*jml
                    st.write("Pemasukkan yang diperoleh:", total)
                if kodekamar == "2":
                    total = 14500000*jml
                    st.write("Pemasukkan yang diperoleh:", total)
                if kodekamar == "3":
                    total = 12500000*jml
                    st.write("Pemasukkan yang diperoleh:", total)
                    st.write(f"Nama Pemesan : {name} ")
                    st.write (f"Nomor HP Pemesan: {hp}")
                    st.write(f"Alamat Pemesan : {address} ")
                    st.write (f"Nomor HP Pemesan: {hp}")
                    st.write(f"Tanggal Pemesanan : {date} ")
                    st.write (f"Total Pemasukkan yang diperoleh: {total}")


        with st.expander("Incomes"):
            for income in incomes:
                st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
        with st.expander("Expenses"):
            for expense in expenses:
                st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
    
        "---"
        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            incomes = {income: st.session_state[income] for income in incomes}
            expenses = {expense: st.session_state[expense] for expense in expenses}
            st.write(f"incomes : {incomes}")
            st.write (f"expenses: {expenses}")
            st.success("Data saved!")


else :
    st.header("Income and Expense Tracker")
    with st.form("saved_periods"):
        period = st.selectbox("Select Period:", ["2022_November"])
        submitted = st.form_submit_button("Plot Period")
        if submitted:
            incomes = {'Pemesanan Kamar Kos': 14500000, 'Pemasukkan Lainnya':80000}
            expenses ={'Air': 30000, 'Listrik':1000000, 'Wi-Fi':200000, 'Gas':70000} 
    
        # Create metrics
            total_income = sum(incomes.values())
            total_expense = sum(expenses.values())
            remaining_budget = total_income - total_expense
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Income", f"{currency} {total_income} ")
            col2.metric("Total Expense", f" {currency} {total_expense}")
            col3.metric("Remaining Budget", f"{currency} {remaining_budget} ")






