import database as db
import streamlit as st


def search_data(keyword):
    query = "SELECT * FROM admin WHERE KODE_ADMIN = %s"
    db.cursor.execute(query, (keyword,))
    result = db.cursor.fetchall()
    return result

def masukan():
    with st.form("Masukan Data"):
        Kodead = st.text_input("Masukan Kode")
        namaad = st.text_input("Masukan Nama Admin")
        nomorad = st.text_input("Masukan Nomor Admin")
        alamatad = st.text_input("masukan Alamat")
        if st.form_submit_button("Tambah"):
            sql = "INSERT INTO admin (KODE_ADMIN, NAMA_ADMIN, NOMOR_HP, ALAMAT) VALUES (%s, %s, %s, %s)"
            val = (Kodead, namaad, nomorad, alamatad,)
            db.cursor.execute(sql, val)
            db.mydb.commit()
            print(db.cursor.rowcount, "Data berhasil ditambahkan")
            st.success("Data Masuk")

def editdataadmin():
    with st.form("Edit Data"):
        Kodead = st.text_input("Masukan Kode")
        namaad = st.text_input("Masukan Nama Admin")
        nomorad = st.text_input("Masukan Nomor Admin")
        alamatad = st.text_input("masukan Alamat")
        if st.form_submit_button("UPDATE"):
            sql = "UPDATE admin set NAMA_ADMIN=%s, NOMOR_HP=%s, ALAMAT=%s where KODE_ADMIN =%s"
            val = (namaad, nomorad, alamatad, Kodead,)
            db.cursor.execute(sql, val)
            db.mydb.commit()
            st.success("Sukses")

def hapusdataadmin():
    with st.form("Hapus Data Admin"):
        kodead = st.text_input("Masukan Kode")
        if st.form_submit_button("Hapus"):
            sql = "DELETE FROM admin where KODE_ADMIN =%s"
            val = (kodead,)
            db.cursor.execute(sql, val)
            db.mydb.commit()
            st.success("Terhapus")
            st.stop()

#Data barang
def searchbarang(keyword):
    query = "SELECT * FROM barang WHERE KODE_BARANG = %s"
    db.cursor.execute(query, (keyword,))
    result = db.cursor.fetchall()
    return result
