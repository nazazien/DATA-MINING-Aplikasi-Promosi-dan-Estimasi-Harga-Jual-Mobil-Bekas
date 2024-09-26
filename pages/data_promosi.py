from keperluan_modul import *

pemanis.ucapan()

st.header(':rainbow[PROMOTION DATA]', divider='rainbow')
st.subheader('Data of used Car Sellers who use our webapp promotional service!')

def tampil_data():        
    df = pd.read_csv('Documents/data/data_promosi.csv')
    pilih_kolom = ["Tanggal Jual","Nama","Alamat","No. Telp","E-Mail","Model","Tahun","Price","Transmission","Mileage","FuelType","Tax","MPG","EngineSize","Status"]

    def hapus_koma(n):
        return str(n).replace(",","")
    
    def tambah_0(x):
        return f"0{x}"    
        
    df["No. Telp"] = df["No. Telp"].apply(hapus_koma)
    df["No. Telp"] = df["No. Telp"].apply(tambah_0)
    df["Tahun"] = df["Tahun"].apply(hapus_koma)    
    
    tampilkan_kolom = df[pilih_kolom]

    thead_style = '''
        <style>
            th{
                background-color: #696969;            
            }
        </style>
    '''

    st.markdown(thead_style, unsafe_allow_html=True)
    st.table(tampilkan_kolom)
tampil_data()