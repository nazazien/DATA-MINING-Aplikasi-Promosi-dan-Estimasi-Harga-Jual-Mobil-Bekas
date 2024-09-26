from keperluan_modul import *

st.header(':rainbow[USED CAR PRICE ESTIMATED]', divider='rainbow')
st.subheader('Price Estimate Form')
df = pd.read_csv('Documents/data/toyota.csv')

st.title('')

col1, col2 = st.columns([2,2])
with col1:
    model = pickle.load(open('estimasi_mobil.sav', 'rb'))
    year = st.number_input('Enter Car Year        : ')
    mileage = st.number_input('Enter mileage (km)  : ')
    pajak = st.number_input('Enter Car Tax        : ')
    tax = pajak/14000
    mpg = st.number_input('Enter Car Fuel Consumption : ')
    engineSize = st.number_input('Enter Engine Size       : ')


with col2:
    st.write("What is the physical condition of your car?")  
    servis = st.radio(
       "Car periodic service period",
        ["Once every 1 month", "Once every 3 months", "Once every 6 months", "More than 6 months"],
        index=None,
    )
    
    lecet = st.checkbox('Scratches')
    if lecet:
        lecet = st.radio(
        "Select damage level",
        ["Mild", "Moderate", "Severe"],
        index=None,
        )

    turun_mesin = st.checkbox('Never down the machine')

    mogok = st.checkbox('Strike')
    if mogok:
        mogok = st.radio(
        "Select damage level",
        ["Sometimes", "Quite often", "Frequently"],
        index=None,
        )

    banjir = st.checkbox('Through the flood')
    if banjir:
        banjir = st.radio(
        "Select level",
        ["1-5 times", "6-10 times", "more than 10 times"],
        index=None,
        )

    predict = 0
    convert_ke_rupiah = 0

if st.button('Estimated Price'):        
    pemanis.sukses()

    predict += model.predict([[year, mileage, tax, mpg, engineSize]])[0]    
    convert_ke_rupiah += predict * 14000

    if servis == "Once every 3 months":         
        convert_ke_rupiah = convert_ke_rupiah-385000
    elif servis == "Once every 6 months":         
        convert_ke_rupiah = convert_ke_rupiah-635000
    elif servis == "More than 6 months":        
        convert_ke_rupiah = convert_ke_rupiah-1070000
    
    if lecet == "Light":
        convert_ke_rupiah = convert_ke_rupiah - 461000
    elif lecet == "Currently":
        convert_ke_rupiah = convert_ke_rupiah - 700100
    elif lecet == "Critical":
        convert_ke_rupiah = convert_ke_rupiah - 930000

    if turun_mesin:
        convert_ke_rupiah = convert_ke_rupiah - 12050000

    if mogok == "Sometimes":
        convert_ke_rupiah = convert_ke_rupiah - 470000
    elif mogok == "Often enough":
        convert_ke_rupiah = convert_ke_rupiah - 830000
    elif mogok == "Often":
        convert_ke_rupiah = convert_ke_rupiah - 1735000
    
    if banjir == "1-5 times":
        convert_ke_rupiah = convert_ke_rupiah - 567000
    elif banjir == "6-10 times":
        convert_ke_rupiah = convert_ke_rupiah - 1093000
    elif banjir == "more than 10 times":
        convert_ke_rupiah = convert_ke_rupiah - 2605000
    
    st.subheader('', divider='rainbow')
    gambar, hasil = st.columns([2,2])
    with gambar:
        st.image(Image.open('Documents/image/da.png'), width=300, caption='Source: https://storyset.com/')
    with hasil:
        st.subheader(':rainbow[Estimated price of your used cars in IDR (Million) : ]')
        st.header('')    

        bulatkan = f'{convert_ke_rupiah:,.0f}'
        cek_hasil = bulatkan.find('-')

        if cek_hasil == 0:
            st.title(f'Rp. {convert_ke_rupiah:,.0f}')  
            st.error("Your car estimation results may not be accurate. Please enter the correct specifications and condition of the car!")          
        else:
            st.title(f'Rp. {convert_ke_rupiah:,.0f}')                        
    
    st.subheader('', divider='rainbow')
    st.subheader(":rainbow[Are you interested for promoting your used car here?]")
    link = "http://localhost:8501/%F0%9F%9A%97%20Promote%20Cars"
    
    left,center,right = st.columns([3,2,3])
    with center: 
        st.link_button("TRY NOW!", link) 
    st.subheader('', divider='rainbow')