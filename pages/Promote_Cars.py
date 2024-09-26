from keperluan_modul import *

try:
    class Promosi:
        def __init__(self):
            try:
                self.data_promosi = pd.read_csv("Documents/data/data_promosi.csv")
            except FileNotFoundError:
                self.data_promosi = pd.DataFrame(columns=["Tanggal Jual","Nama","Alamat","No. Telp","E-Mail","Model","Tahun","Price","Transmission","Mileage","FuelType","Tax","MPG","EngineSize","Status","Bagian Depan","Bagian Samping Kanan","Bagian Samping Kiri","Bagian Belakang"])

        def jual_mobil(self, tanggal_jual, nama, alamat, no_telp, email, model, year, price, transmission, mileage, fuel_type, tax, mpg, engine_size, depan, kanan, kiri, belakang):
            status = "DIJUAL"    
            self.data_promosi.loc[len(self.data_promosi)] = [tanggal_jual, nama, alamat, int(no_telp), email, model, int(year), int(price), transmission, int(mileage), fuel_type, tax, int(mpg), int(engine_size), status, depan, kanan, kiri, belakang]    
            self.data_promosi.to_csv("Documents/data/data_promosi.csv", index=False)        


    fungsi = Promosi()

    st.header(':rainbow[PROMOTE YOUR USED CAR]', divider='rainbow')
    st.title('')
    st.subheader("Fill in your personal data", divider="grey")
    data,gambar = st.columns([2,2])
    with data:
        nama = st.text_input('Enter Name: ', placeholder="Your Name ...")    
        alamat = st.text_area('Enter Address: ')
        no_telp = st.number_input("Enter Phone Number:")
        email = st.text_input("Enter E-mail:")

    with gambar:
        st.image(Image.open('Documents/image/fo.png'), width=500, caption='Source: https://storyset.com/')


    st.title('')
    st.subheader("Fill in your car's specification data", divider="grey")

    col1,col2=st.columns([2,2])
    with col1:
        model = st.text_input('Enter Model: ',placeholder="ex: Yaris, Auris, Aygo, etc.")
        year = st.number_input('Enter Year: ', min_value=2005, max_value=2023, step=1)
        price = st.number_input('Enter Price: ', placeholder="Your price ...")
        transmission = st.selectbox(
                        'Select transmission type: ',
                        ('Manual', 'Semi-Auto', 'Automatic'))
        mileage = st.number_input('Enter Mileage (km): ', placeholder="Your mileage ...")        

    with col2:
        fuel_type = st.selectbox(
                        'Select Fuel Type: ',
                        ('Petrol', 'Hybrid', 'Diesel', 'Other'))
        tax = st.number_input('Enter TAX: ')
        mpg = st.number_input('Enter MPG: ')
        engine_size = st.number_input('Enter Engine Size: ') 

    st.title('')
    st.subheader("Upload some photos of your car", divider="grey")

    col1,col2=st.columns([2,2])
    with col1:
        depan = st.file_uploader("Front view")
        kanan = st.file_uploader("Right-side view")
    with col2:
        kiri = st.file_uploader("Left-side view")
        belakang = st.file_uploader("Back view")

    st.title('')
    st.subheader("", divider="rainbow")
    st.subheader(":rainbow[CONFIRM YOUR DATA]", divider="rainbow")

    personal_data,specification = st.columns([2,2])
    with personal_data:
        st.write('PERSONAL DATA')
        st.write('Sale Date : ',datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        st.write('Name   \t:', nama)    
        st.write('Address\t:', alamat)
        st.write('Contact Number:', no_telp)
        st.write('E-Mail        :', email)
        st.write(' ')

    with specification:
        st.write('CAR SPECIFICATIONS')
        st.write('Model :', model)
        st.write('Year :', year)
        st.write('Price :', price)
        st.write('You selected:', transmission)

    kol1,kol2 = st.columns([2,2])
    with kol1:
        st.write('Front View:')
        if depan is not None:
            st.image(depan)

    with kol2:
        st.write('Back View:')
        if belakang is not None:
            st.image(belakang)

    kol3,kol4 = st.columns([2,2])
    with kol3:
        st.write('Right-side View:')
        if kanan is not None:
            st.image(kanan)

    with kol4:
        st.write('Left-side View:')
        if kiri is not None:
            st.image(kiri)

    if st.button("Sell Car"):        
        tanggal_jual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
        with open(os.path.join("Documents\dok mobil",depan.name),"wb") as menyimpan:
            menyimpan.write(depan.getbuffer())
        with open(os.path.join("Documents\dok mobil",kanan.name),"wb") as menyimpan:
            menyimpan.write(kanan.getbuffer())
        with open(os.path.join("Documents\dok mobil",kiri.name),"wb") as menyimpan:
            menyimpan.write(kiri.getbuffer())
        with open(os.path.join("Documents\dok mobil",belakang.name),"wb") as menyimpan:
            menyimpan.write(belakang.getbuffer())

        isi_depan = f"Documents\dok mobil\{depan.name}"
        isi_kanan = f"Documents\dok mobil\{kanan.name}"
        isi_kiri = f"Documents\dok mobil\{kiri.name}"
        isi_belakang = f"Documents\dok mobil\{belakang.name}"

        fungsi.jual_mobil(tanggal_jual, nama, alamat, no_telp, email, model, year, price, transmission, mileage, fuel_type, tax, mpg, engine_size, isi_depan, isi_kanan, isi_kiri, isi_belakang)
        st.success("Successfully promote the car!!")
        pemanis.sukses()

        st.subheader('', divider='rainbow')
        st.subheader(":rainbow[Try checking how your used car is promoted]")

        left,center,right = st.columns([3,2,3])
        with center: 
            st.link_button("HERE!", "http://localhost:8501/%F0%9F%94%A5%F0%9F%8E%89%20HOT%20PROMOTION")
        
    st.subheader("", divider="rainbow")

except AttributeError:
    st.warning("FAILED TO SELL! Make sure all photos of the car is uploaded.")