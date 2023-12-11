import database as db
import streamlit as st
import admin as ad
import pandas as pd



#read data barang inv, masuk, keluar
def readbarang():
    sql = "SELECT * FROM barang"
    db.cursor.execute(sql)
    data = db.cursor.fetchall()
    return data

def readbarangmasuk():
    sql = "SELECT * FROM barang_masuk"
    db.cursor.execute(sql)
    data = db.cursor.fetchall()
    return data

def readbarangkeluar():
    sql = "SELECT * FROM barang_keluar"
    db.cursor.execute(sql)
    data = db.cursor.fetchall()
    return data

#memilih data
def inputbarang():
    with st.form("Masukan Data"):
        tipe = st.selectbox("",["Barang Masuk","Barang Keluar"])
        tgl = st.date_input("Tanggal")
        kodbm = st.text_input("Kode Transaksi")
        kodbar = st.text_input("Masukan Kode Barang")
        if st.form_submit_button("Periksa") :
            results = ad.searchbarang(kodbar)
            # Display results
            if not results:
                st.info("No results found.")
            else:
                st.table(results)
        koded = st.text_input("Masukan Kode Admin")
        if st.form_submit_button("Cek") :
            results = ad.search_data(koded)
            # Display results
            if not results:
                st.info("No results found.")
            else:
                st.info("Admin Ditemukan")
        jmlh = st.number_input("Masukan Jumlah",min_value=0)
        if st.form_submit_button("Input"):
            if tipe == "Barang Masuk" :
                # Check if KODE_BM already exists
                db.cursor.execute("SELECT COUNT(*) FROM barang_masuk WHERE KODE_BM = %s", (kodbm,))
                if db.cursor.fetchone()[0] > 0:
                    st.error("KODE_BM already exists. Please use a different KODE_BM.")
                else:
                    # If KODE_BM does not exist, insert the new record
                    sql = "INSERT INTO barang_masuk (KODE_BM, KODE_ADMIN, TANGGAL, JUMLAH) VALUES (%s, %s, %s, %s)"
                    val = (kodbm, koded, tgl, jmlh)
                    db.cursor.execute(sql, val)
                    db.cursor.execute("UPDATE barang SET stok = stok + %s WHERE KODE_BARANG = %s", (jmlh,kodbar,))
                    db.mydb.commit()
                    print(db.cursor.rowcount, "Data berhasil ditambahkan")
                    st.success("Data Masuk")
            elif tipe == "Barang Keluar":
                # Check if KODE_BM already exists
                db.cursor.execute("SELECT COUNT(*) FROM barang_keluar WHERE KODE_BK = %s", (kodbm,))
                if db.cursor.fetchone()[0] > 0:
                    st.error("KODE_BK already exists. Please use a different KODE_BK.")
                else:
                    # If KODE_BK does not exist, insert the new record
                    sql = "INSERT INTO barang_keluar (KODE_BK, KODE_ADMIN, TANGGAL, JUMLAH) VALUES (%s, %s, %s, %s)"
                    val = (kodbm, koded, tgl, jmlh)
                    db.cursor.execute(sql, val)
                    db.cursor.execute("UPDATE barang SET stok = stok -%s WHERE KODE_BARANG = %s", (jmlh,kodbar,))
                    db.mydb.commit()
                    print(db.cursor.rowcount, "Data berhasil ditambahkan")
                    st.success("Data Masuk")

#Inventori
def invenbaru():
    with st.form("Masukan Data Inventori Baru"):
        Kodebar = st.text_input("Masukan Kode Barang")
        df = pd.read_sql_query("SELECT KATEGORI FROM kategori_barang", db.mydb)
        katbar = st.selectbox("Kategori Barang", df["KATEGORI"])
        namabar = st.text_input("Masukan Nama Barang")
        stk = st.number_input("Stok Barang",min_value=0)
        kondisi = st.selectbox("Kondisi Barang",["Baik","Cacat"])
        if st.form_submit_button("Tambah") :
            sql = "INSERT INTO barang (KODE_BARANG, KATEGORI, NAMA_BARANG, STOK, KONDISI) VALUES (%s, %s, %s, %s, %s)"
            val = (Kodebar, katbar, namabar, stk, kondisi)
            db.cursor.execute(sql, val)
            db.mydb.commit()
            print(db.cursor.rowcount, "Data berhasil ditambahkan")
            st.success("Data Masuk")

def hapusinven():
    with st.form("Hapus Barang"):
        kodebar = st.text_input("Masukan Kode Barang")
        if st.form_submit_button("Hapus"):
            sql = "DELETE FROM barang where KODE_BARANG =%s"
            val = (kodebar,)
            db.cursor.execute(sql, val)
            db.mydb.commit()
            st.success("Terhapus")
            st.stop()

def katbar():
    with st.form("Kategori Baru"):
        katbar = st.text_input("Masukan Kategori Baru")
        if st.form_submit_button("Input"):
            sql = "INSERT INTO kategori_barang (KATEGORI) VALUES (%s)"
            val = (katbar)
            db.cursor.execute(sql, val)
            db.mydb.commit()