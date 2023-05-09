import streamlit as st

st.title('menghitung jumlah mmol dari suatu logam mulia')

tab1, tab2, tab3=st.tabs(['informasi tentang Logam Mulia','informasi nilai Ar Logam Mulia','kalkulator menghitung mmol'])

with tab1:
    st.header('Informasi Tentang Logam Mulia')
    st.write('Logam mulia atau logam adi adalah logam yang tahan terhadap korosi maupun oksidasi. Beberapa contoh logam yang mulia secara kimia (unsur-unsur yang disetujui hampir seluruh kimiawan) diantaranya rutenium (Ru), rodium (Rh), paladium (Pd), perak (Ag), osmium (Os), iridium (Ir), platina (Pt), dan emas (Au)')
    
with tab2:
    st.header('Nilai Ar suatu logam Mulia')
    st.write('Ru =101,07')
    st.write('Rh =102,905')
    st.write('Pd =106,4')
    st.write('Ag =107,870')
    st.write('Os =190,2')
    st.write('Ir =192,2')
    st.write('Pt =195,09')
    st.write('Au =196,967')
    
with tab3:
    st.header('kalkulator menghitung mmol')
    options=st.multiselect(
        'nama logam mulia',
        ['Ru','Rh ','Pd','Ag ','Os','Ir ','Pt ','Au'])
    y = st.number_input('Masukkan massa padatan dari unsur logam yang telah dipilih dalam satuan mg:')
    z = st.number_input('Masukkan massa atom relatif logam (Ar) mulia yang telah dipih dalan satuan mg/mmol:')


    tombol = st.button('Hitung jumlah mmol dari suatu logam mulia')

    if tombol:
        jumlah_mmol = y/z
        st.success(f'jumlah mmol adalah {options} {jumlah_mmol}')
    
    