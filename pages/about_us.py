from keperluan_modul import *

pemanis.profil()

st.header(':rainbow[ABOUT US]', divider='rainbow')
st.subheader('We are behind the scenes of Technokiawan!')
st.subheader("")

deskripsi, poto = st.columns([2,2])
with deskripsi:
    st.markdown('''The "Technokiawan" team consists of three students from the Data Science Undergraduate Study Program class 2023E, Faculty of Mathematics and Natural Sciences, Surabaya State University.\n\nFormed with the aim of fulfilling the final project assignment for first semester in the Basic Programming course under the guidance of the lecturer, namely Mrs. Fadhilah Qalbi Annisa, S.T., M.Sc.''')

with poto:
    st.image(Image.open('Documents/image/logo.png'), width=250)
st.markdown('''\n\nThe project carried out by this team is the "Data Mining Used Car Price Estimation" application which also includes promotional services and scheduling used car purchases.\n\nThe "Technokiawan" team hopes to make a positive contribution in fulfilling the final semester assignment and improving understanding and skills in basic programming and data science.''')
st.subheader("",divider='grey')
st.subheader(":rainbow[Our Team]", divider='grey')

col1,col2,col3 = st.columns([2,2,2])
with col1:
    st.image(Image.open('Documents/image/naza.jpg'), width=150)
    st.markdown('''Naza Sulthoniyah Wahda
                23031554026
                naza.23026@gmail.com''')

with col2:
    st.image(Image.open('Documents/image/mamad1.jpg'), width=150)
    st.markdown('''Ahmad Marannuang Tajibu
                23031554040
                ahmadmarannuang.23040@mhs.unesa.ac.id''')

with col3:
    st.image(Image.open('Documents/image/salsa.jpg'), width=150)
    st.markdown('''Salsabilla Indah Rahmawati
                23031554193
                salsabilla.23193@mhs.unesa.ac.id''')