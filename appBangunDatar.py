import streamlit as st

# halaman utama 
st.title('aplikasi perhitungan luas bangung datar')
st.header('ini buatan anak SI') 

menu = st.sidebar.selectbox ('Pilih aplikasi', ['luas persegi', 'luas segitiga', 'luas lingkaran'])

if menu == 'luas persegi':
    st.write ('ini halaman untuk menghitung luas persegi')
    st.markdown('luas persegi panjang')
    st.image('https://imgix3.ruangguru.com/assets/miscellaneous/png_mslu6k_7468.png', caption='gambar persegi')
    sisi = st.number_input('silahkan masukan angka sisi', min_value=0)
    if st.button('hitung'):
       luas = sisi * sisi
       st.write(f'Luas persegi adalah {luas}')

elif menu == 'luas segitiga':
    st.write ('ini halaman untuk menghitung luas segitiga')
    st.markdown('Luas segitiga')
    st.image('https://i.pinimg.com/736x/0e/d0/29/0ed0298f948ba076e1e7ee5501f56ffc.jpg', caption='gambar luas segitiga')