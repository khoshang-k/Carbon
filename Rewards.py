import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from st_pages import Page, Section, show_pages, add_page_title,hide_pages
from pymongo import MongoClient
__login__obj = __login__(auth_token = "dk_prod_D8ZQ8GGX75M35KMST4HRTSX97QED",company_name = "Carbon Footprint Calculator",width = 200, height = 250,logout_button_name = 'Logout', hide_menu_bool = False,hide_footer_bool = False,lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')
LOGGED_IN= __login__obj.build_login_ui()
username=__login__obj.get_username()
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
    st.title("Reward Page") 
    client = MongoClient('mongodb+srv://carboncalculator2024:zipzcwaQu1UnYTT5@carbonfootprint.febn7uz.mongodb.net/?retryWrites=true&w=majority&appName=carbonfootprint')
    db = client['carbon_footprint']
    collection = db['User_info']
    alldoc = collection.find_one({'Username':username}, {'Points':1,'_id':0})
    points=alldoc["Points"]
    def pointsUpdate(a,b):
        if a>=b:
            collection.update_one({'Username':username},{'$set': {'Points':a-b}})
        return a-b
    st.header(f"Coins 💰: {points}")
    st.write("Welcome to our Reward Page! Here, you can redeem your earned coins for exciting rewards.")
    st.write("Choose from the following rewards:")
    col1, col2 = st.columns(2)
    with col1:
        with st.form("Coffee"):
            st.header("Eco-Friendly Tote Bag 🛍")
            st.write("Cost: 50 💰")
            submit1 = st.form_submit_button("Redeem")
            
        with st.form("Steel"):
            st.header("Stainless Steel Water Bottle 💧")
            st.write("Cost: 75 💰")
            submit2 = st.form_submit_button("Redeem")
        with st.form("Bamboo"):
            st.header("Bamboo Toothbrush Set 🦷")
            st.write("Cost: 100 💰")
            submit3 = st.form_submit_button("Redeem")
        
    with col2:
        with st.form("Tree"):
            st.header("Tree Planting Certificate 🌳")
            st.write("Cost: 150 💰")
            submit4 = st.form_submit_button("Redeem")
        with st.form("Metal"):
            st.header("Reusable Metal Straw Set 🥤")
            st.write("Cost: 80 💰")
            submit5 = st.form_submit_button("Redeem")
        with st.form("Plant"):
            st.header("Plant-Based Meal Recipe Book 📖")
            st.write("Cost: 120 💰")
            submit6 = st.form_submit_button("Redeem")
    if submit1:
        points=pointsUpdate(points,50)
        if(points<0):
            st.warning("Not Enough Coins")
        else:
            st.success("You redeemed Coupon. Enjoy your Reward")
            st.write("Please refresh page to see changes")
            st.write(f"Reward Points Left: {points}")
    if submit2:
        points=pointsUpdate(points,75)
        if(points<0):
            st.warning("Not Enough Coins")
        else:
            st.success("You redeemed Coupon. Enjoy your Reward")
            st.write("Please refresh page to see changes")
            st.write(f"Reward Points Left: {points}")
    if submit3:
        points=pointsUpdate(points,100)
        if(points<0):
            st.warning("Not Enough Coins")
        else:
            st.success("You redeemed Coupon. Enjoy your Reward")
            st.write("Please refresh page to see changes")
            st.write(f"Reward Points Left: {points}")
    if submit4:
        points=pointsUpdate(points,150)
        if(points<0):
            st.warning("Not Enough Coins")
        else:
            st.success("You redeemed Coupon. Enjoy your Reward")
            st.write("Please refresh page to see changes")
            st.write(f"Reward Points Left: {points}")
    if submit5:
        points=pointsUpdate(points,80)
        if(points<0):
            st.warning("Not Enough Coins")
        else:
            st.success("You redeemed Coupon. Enjoy your Reward")
            st.write("Please refresh page to see changes")
            st.write(f"Reward Points Left: {points}")
    if submit6:
        points=pointsUpdate(points,120)
        if(points<0):
            st.warning("Not Enough Coins")
        else:
            st.success("You redeemed Coupon. Enjoy your Reward")
            st.write("Please refresh page to see changes")
            st.write(f"Reward Points Left: {points}")
