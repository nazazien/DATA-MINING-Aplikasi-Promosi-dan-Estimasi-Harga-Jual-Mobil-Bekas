from keperluan_modul import *

pemanis.ucapan()


st.header(':rainbow[APPOINTMENT DATA]', divider='rainbow')
st.subheader('User data of our webapp appointment service!')

def tampil_data():        
    df = pd.read_csv('Documents/data/data_janji.csv')

    def hapus_koma(phone):
        return str(phone).replace(",","")

    df["Tahun"] = df["Tahun"].apply(hapus_koma)

    pilih_kolom = ['Tanggal Pengajuan','Nama Penjual','Nama Pembeli','Model','Tahun']
    tampilkan_kolom = df[pilih_kolom]

    thead_style = '''
        <style>
            th{
                background-color: #696969;
            }
        </style>
    '''

    st.markdown(thead_style, unsafe_allow_html=True) #unsafe_follow_html fungsinya agar TML/CSS dapat dijalankan
    #st.markdown gunanya untuk menambahkan elemen-elemen. kek menampilkan teks dengan format-format seng udah diatur
    #contoh e coba kode ndek bawah iki komen e ilangin dan lihat hasilnya.
    # st.markdown("Ini adalah *teks miring* dan **teks tebal**.")
    # st.markdown("1. ini adalan item daftar \n2. Ini adlah item daftar kedua")
    st.table(tampilkan_kolom)

tampil_data()