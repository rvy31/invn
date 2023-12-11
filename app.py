import streamlit as st
import pandas as pd
import database as db
from streamlit_option_menu import option_menu
import admin as ad
import barang as br

with st.sidebar :
    menu = option_menu("Main Menu", [
                        "Admin","Data Barang","Input Barang"],menu_icon = "list",icons=["person-fill","boxes","pencil"])
    
if menu == "Admin":
    admin = st.selectbox("",["Data Admin","Daftar","Edit Data Admin","Hapus Admin"])
    if admin == "Data Admin" :
        st.subheader("Admin")
        keyword = st.text_input("Enter a keyword:")
        
        if not keyword:
            st.warning("Please enter a keyword.")
            st.stop()

        # Perform search
        results = ad.search_data(keyword)
        data = pd.DataFrame(results)

            # Display results
        st.write(f"Search results for '{keyword}':")
        if not results:
            st.info("No results found.")
        else:
            st.table(data)

    elif admin == "Daftar" :
        ad.masukan()

    elif admin == "Edit Data Admin":
        ad.editdataadmin()

    elif admin == "Hapus Admin" :
        ad.hapusdataadmin()


elif menu == "Data Barang" :
    tab1, tab2, tab3 = st.tabs(["Data Inventori", "Barang Masuk", "Barang Keluar"])
    with tab1:
        menu1 = st.selectbox("",["Data Inventori","Inventori Baru","Hapus Inventori","Kategori Baru"])  
        if menu1 == "Data Inventori":
            st.header("Data Inventori")
            data = br.readbarang()
            df = pd.DataFrame(data)
            st.table(df)
        
        elif menu1 == "Inventori Baru":
            st.header("Inventori Baru")
            br.invenbaru()
        
        elif menu1 == "Hapus Inventori":
            br.hapusinven()


        elif menu1 == "Kategori Baru":
            br.katbar()

    with tab2 :
        st.header("Data Barang Masuk")
        data = br.readbarangmasuk()
        df = pd.DataFrame(data)
        st.table(df)
    with tab3 :
        st.header("Data Barang Masuk")
        data = br.readbarangkeluar()
        df = pd.DataFrame(data)
        st.table(df)

#input barang masuk keluar
elif menu == "Input Barang":
    st.header("Masukan Barang")
    br.inputbarang()

