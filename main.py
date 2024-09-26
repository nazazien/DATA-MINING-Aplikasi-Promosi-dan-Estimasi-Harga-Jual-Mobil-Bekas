from keperluan_modul import *

show_pages(
    [
        Page("pages/Homepage.py", "🏠 Home"),
        Page("main.py", "🔥🎉 HOT PROMOTION"),        
        Page("pages/Price_Estimation.py", "📊 Price Estimation"),        
        Page("pages/Promote_Cars.py", "🚗 Promote Cars"),        
        Page("pages/Appointment.py", "📅 Appointment"),        
        Page("pages/data_promosi.py", "📄 Promotion Data"),
        Page("pages/data_janji.py", "📑 Appointment Data"),        
        Page("pages/about_us.py", "👥 About Us"),        
    ]
)

class Pengajuan:
    def __init__(self):
        try:
            self.data_promosi = pd.read_csv("Documents/data/data_promosi.csv")
        except FileNotFoundError:
            self.data_promosi = pd.DataFrame(columns=["Tanggal Jual","Nama","Alamat","No. Telp","E-Mail","Model","Tahun","Price","Transmission","Mileage","FuelType","Tax","MPG","EngineSize","Status","Bagian Depan","Bagian Samping Kanan","Bagian Samping Kiri","Bagian Belakang"])    
    
st.balloons()
st.header(':rainbow[WELCOME TO OUR APP!]', divider='rainbow')
st.title('🔥🎉 !! HOT PROMOTION !! 🎉🔥')
st.markdown('<marquee style="color:#FF7F50"> 🔥 SUPER PROMOTION 🔥 SUPER PROMOTION 🔥 SUPER PROMOTION 🔥 SUPER PROMOTION 🔥 SUPER PROMOTION 🔥 </marquee>', unsafe_allow_html=True)
st.title('')

fungsi = Pengajuan()

df = pd.read_csv("Documents/data/data_promosi.csv")
pilih_kolom = ["Price"]
tampilkan_kolom = df[pilih_kolom]
st.line_chart(tampilkan_kolom)
st.write(":grey[Used car selling price graph on the Technokiawan.com WebApp]")

st.header('💸 SPEND YOUR MONEY HERE 💸')

video_file = open('Documents/video/profil.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

try:            
    pemanis.menyapa_user()

    mobil_yang_tersedia = fungsi.data_promosi[fungsi.data_promosi["Status"] == "DIJUAL"]
    pilih_mobil = st.selectbox("View Promoted Cars:", mobil_yang_tersedia["Model"].unique(), index=0)        
    detail = mobil_yang_tersedia[mobil_yang_tersedia["Model"] == pilih_mobil].iloc[0]        

    col1,col2=st.columns([2,2])
    with col1:        
        st.image(detail["Bagian Depan"], caption="Front view")        
    with col2:        
        st.image(detail["Bagian Samping Kanan"], caption="Right-side view")        

    col4,col5=st.columns([2,2])
    with col4:        
        st.image(detail["Bagian Belakang"], caption="Back view")        
    with col5:        
        st.image(detail["Bagian Samping Kiri"], caption="Left-side view")        

    st.subheader('', divider='rainbow')
    st.subheader(":rainbow[MAKE AN APPOINTMENT WITH THE SELLER AND GET THE]")    
    
    left,center,right = st.columns([3,2,3])
    with center: 
        st.link_button("CAR NOW!", "http://localhost:8501/%F0%9F%93%85%20Appointment") 
    st.subheader('', divider='rainbow')

except IndexError:
    st.title(":rainbow[UPS! Used cars are sold out!!]")
    st.image(Image.open('Documents/image/so.png'))