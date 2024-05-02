import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from st_pages import Page, Section, show_pages, add_page_title,hide_pages
from pymongo import MongoClient
__login__obj = __login__(auth_token = "dk_prod_D8ZQ8GGX75M35KMST4HRTSX97QED",company_name = "Carbon Footprint Calculator",width = 200, height = 250,logout_button_name = 'Logout', hide_menu_bool = False,hide_footer_bool = False,lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')
LOGGED_IN= __login__obj.build_login_ui()
username= __login__obj.get_username()
show_pages(
    [
        Page("Calculator.py","Home"),
        Page("UserInfo.py","My Info"),
        Page("2_history.py", "Stats"),
        Page("Quiz.py","Quiz"),
        Page("Rewards.py","Rewards"),
        Page("1_About.py", "About"),
    ]
)
if LOGGED_IN==False:
   hide_pages(["Stats","Home","About","Quiz","Rewards","My Info"])
if LOGGED_IN == True:
    show_pages(
    [
        Page("Calculator.py","Home"),
        Page("UserInfo.py","My Info"),
        Page("2_history.py", "Stats"),
        Page("Quiz.py","Quiz"),
        Page("Rewards.py","Rewards"),
        Page("1_About.py", "About"),
    ]
    )
    def disable():
        st.session_state.disabled = True
    
    st.toast("Fill this form only once")    
    st.title("Personal Information")
    st.write("Enter the following information for ease to calculate your carbon emission")

    members = st.selectbox("Number of members in house?",['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    locality = st.selectbox("Region",['Urban','Rural'])
    meal = st.selectbox("Meal Preference",['Veg','Non-Veg'])
    appliances = st.number_input("Enter the No. of Electronic Appliances used in your home",value=None,step=1)
    renew = st.toggle("Any type of Renewable Energy Generated")
    if renew:
        renew_energy = st.number_input("Amount of Energy Renewed(KWh)",step=1,value=0,min_value=0,max_value=1000)
    else:
        renew_energy=0
    submit = st.button("Submit",on_click=disable)
    if submit:
        client = MongoClient('mongodb+srv://carboncalculator2024:zipzcwaQu1UnYTT5@carbonfootprint.febn7uz.mongodb.net/?retryWrites=true&w=majority&appName=carbonfootprint')
        db = client['carbon_footprint']
        collection = db['User_info']
        document = {'Username':username,'Family':members,'Locality':locality,'Meal':meal,'Appliance_no':appliances,'Renewable_produced':renew_energy,'Points':300}
        collection.insert_one(document)


