from keperluan_modul import *

try:
    class Pengajuan:
        def __init__(self):
            try:
                self.data_janji = pd.read_csv("Documents/data/data_janji.csv")
            except FileNotFoundError:
                self.data_janji = pd.DataFrame(columns=["Tanggal Jual Mobil","Nama Penjual","Alamat Penjual","No. Telp Penjual","E-Mail Penjual","Model","Tahun","Price","Transmission","Mileage","FuelType","Tax","MPG","EngineSize","Status","Bagian Depan","Bagian Samping Kanan","Bagian Samping Kiri","Bagian Belakang","Tanggal Pengajuan","Jadwal Janji Temu","Nama Pembeli","Alamat Pembeli","No. Telp Pembeli","E-Mail Pembeli"])

            try:
                self.data_promosi = pd.read_csv("Documents/data/data_promosi.csv")
            except FileNotFoundError:
                self.data_promosi = pd.DataFrame(columns=["Tanggal Jual","Nama","Alamat","No. Telp","E-Mail","Model","Tahun","Price","Transmission","Mileage","FuelType","Tax","MPG","EngineSize","Status","Bagian Depan","Bagian Samping Kanan","Bagian Samping Kiri","Bagian Belakang"])

        def beli_mobil(self, index, temu, nama, alamat, no_tlp, email):            
            self.nama = nama
            self.temu = temu
            self.alamat = alamat
            self.no_tlp = no_tlp
            self.email = email
            self.pilih_model = self.data_promosi.loc[index].drop("Status")
            self.tanggal_pengajuan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        
            self.data_janji.loc[len(self.data_janji)] = self.pilih_model.tolist() + [self.tanggal_pengajuan,temu,nama,alamat,int(no_tlp),email]
            
            self.data_promosi.at[index, "Status"] = "Unavailable"
            
            self.data_janji.to_csv("Documents/data/data_janji.csv", index=False)
            self.data_promosi.to_csv("Documents/data/data_promosi.csv", index=False)                        
            
            st.success(f"Successfully booked an appointment with {pilih_mobil}`s Car seller!")            
            st.header(" ", divider="rainbow")
            st.header(":rainbow[APPOINTMENT DETAILS]", divider="rainbow")
            
            col1,col2 = st.columns([2,2])
            with col1:
                st.subheader("Seller Data")
                st.write(f"Name: {self.pilih_model['Nama']}")
                st.write(f"Address: {self.pilih_model['Alamat']}")
                st.write(f"Contact Person: 0{self.pilih_model['No. Telp']}")
                st.write(f"E-Mail: {self.pilih_model['E-Mail']}")            
                st.subheader(" ")                                                            
            
            with col2:
                st.subheader("Buyer Data")            
                st.write(f"Name: {self.nama}")
                st.write(f"Address: {self.alamat}")
                st.write(f"Contact Person: {self.no_tlp}")
                st.write(f"E-Mail: {self.email}")            
                st.write(f"Appointment Schedule: {self.temu}")
                st.subheader(" ")                                
        
            st.subheader("",divider="grey")
            st.subheader("Car Spec Data",divider="grey")
            col3,col4 = st.columns([2,2])
            with col3:                
                st.write(f"Model: {self.pilih_model['Model']}")        
                st.write(f"Year: {self.pilih_model['Tahun']}")        
                st.write(f"Price: {self.pilih_model['Price']}")        
                st.write(f"Transmission: {self.pilih_model['Transmission']}")        
            with col4:
                st.write(f"Mileage: {self.pilih_model['Mileage']}")
                st.write(f"FuelType: {self.pilih_model['FuelType']}")
                st.write(f"Tax: {self.pilih_model['Tax']}")
                st.write(f"MPG: {self.pilih_model['MPG']}")
                st.write(f"EngineSize: {self.pilih_model['EngineSize']}")      

            st.subheader("",divider="grey")
            st.subheader("Car Photos",divider="grey")
            col5,col6,col7,col8 = st.columns([2,2,2,2])
            with col5:                
                st.image(f"{self.pilih_model['Bagian Depan']}")
            with col6:
                st.image(f"{self.pilih_model['Bagian Samping Kanan']}")
            with col7:
                st.image(f"{self.pilih_model['Bagian Samping Kiri']}")
            with col8:
                st.image(f"{self.pilih_model['Bagian Belakang']}")                                      
            
            self.hubungi_penjual()

        def hubungi_penjual(self):
            no_penjual = self.pilih_model['No. Telp']
            nama = self.nama
            mobil = self.pilih_model['Model']
            jadwal = self.temu
            
            copy_pesan = f"Halo, perkenalkan nama saya *{nama}.* Saya adalah pengguna Layanan Website Jual Beli Mobil Bekas oleh *Technokiawan.com.* Saya tertarik dengan mobil *{mobil}* yang Anda jual. Untuk itu bisakah kita melakukan pertemuan pada *{jadwal}* ? Saya harap kita bisa bertemu. Terimakasih atas waktu Anda!"
            link_wa = f"https://wa.me/+62{no_penjual}?text={copy_pesan}"        
            
            st.subheader("", divider="rainbow")            
            st.link_button("Contact the Seller via WhatsApp", link_wa)
            st.subheader("",divider="rainbow")
                                            
    fungsi = Pengajuan()
    
    st.header(':rainbow[SET AN APPOINTMENT SCHEDULE]', divider='rainbow')
    st.subheader('Arrange an appointment with the seller for car purchases')
    st.subheader('')

    st.subheader('Personal data', divider="grey")        
    st.subheader("")

    col1,col2=st.columns([2,2])
    with col1:        
        nama = st.text_input('Enter Name: ', placeholder="Your Name ...")          
        alamat = st.text_area('Enter Address: ')
    with col2:
        no_tlp = st.number_input("Enter Phone Number:", value=None, placeholder="Type a number...")
        email = st.text_input('Enter E-Mail: ', value=None, placeholder="...@gmail.com")        
        
    st.subheader("Set Schedule", divider="grey")        
    st.subheader("")

    foto,data = st.columns([3,2])
    with foto:
        mobil_yang_tersedia = fungsi.data_promosi[fungsi.data_promosi["Status"] == "DIJUAL"]
        pilih_mobil = st.selectbox("Select the car to buy:", mobil_yang_tersedia["Model"].unique(), index=0)    
        detail = mobil_yang_tersedia[mobil_yang_tersedia["Model"] == pilih_mobil].iloc[0]                 
                
        st.image(detail["Bagian Depan"])        
        st.image(detail["Bagian Samping Kanan"])        
        st.image(detail["Bagian Belakang"])                
        st.image(detail["Bagian Samping Kiri"])

    with data:
        temu = st.date_input('Enter Appointment Date: ',value=None)
        
        pilih_kolom = ["Tanggal Jual","Nama","Alamat","No. Telp","E-Mail","Model","Tahun","Price","Transmission","Mileage","FuelType","Tax","MPG","EngineSize"]
        def tambah_0(x):
            return f"0{x}"
        detail["No. Telp"] = tambah_0(detail["No. Telp"])

        tampilkan_kolom = detail[pilih_kolom]        
        st.table(tampilkan_kolom) 
    
    st.subheader("",divider='rainbow')
    if st.button("Make an Appointment"):
        pemanis.sukses()
        pilih_data = mobil_yang_tersedia[mobil_yang_tersedia["Model"] == pilih_mobil]    
        if not pilih_data.empty:
            index = pilih_data.index[0]
            fungsi.beli_mobil(index, temu, nama, alamat, no_tlp, email) 
        else:
            st.warning("Cannot find the selected car.")

except IndexError:
    st.title(":rainbow[UPS! Used cars are sold out!!]")
    st.image(Image.open('Documents/image/so.png'))