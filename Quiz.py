import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title,hide_pages
from streamlit_login_auth_ui.widgets import __login__
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
    if "disabled" not in st.session_state:
        st.session_state["disabled"] = False
        
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
    
        
    st.title("Carbon Footprint Quiz")
    st.write("Test your knowledge about carbon footprint!")
    # Define quiz questions and answers
    questions = [
        "Which of the following contributes most to your carbon footprint?",
        "How can you reduce your carbon footprint while commuting?",
        "Which of the following activities has the highest carbon footprint?",
        "What is the most effective way to reduce your carbon footprint at home?",
        "Which type of food has the highest carbon footprint?",
        "What can you do to reduce your carbon footprint when traveling by plane?",
        "What is the largest source of greenhouse gas emissions globally?",
        "What is a carbon offset?",
        "Which of the following is a renewable energy source?",
        "What is the purpose of calculating your carbon footprint?"
    ]
    options = [
        ["Driving a gas-powered car", "Riding a bicycle", "Taking a hot shower", "Eating meat"],
        ["Driving alone in a car", "Taking public transportation", "Carpooling with friends", "All of the above"],
        ["Using a laptop", "Using a dishwasher", "Using a washing machine", "All of the above"],
        ["Reduce, reuse, recycle", "Use energy-efficient appliances", "Eat a plant-based diet", "All of the above"],
        ["Beef", "Chicken", "Vegetables", "Fish"],
        ["Fly less frequently", "Fly nonstop", "Fly economy class", "All of the above"],
        ["Electricity production", "Agriculture", "Transportation", "All of the above"],
        ["A way to reduce carbon emissions", "A measurement of carbon footprint", "A type of renewable energy", "None of the above"],
        ["Coal", "Natural Gas", "Solar", "All of the above"],
        ["To understand your impact on the environment", "To win a prize", "To compare with others", "To increase your carbon footprint"]
    ]
    answers = [3, 3, 3, 3, 1, 3, 3, 1, 3, 1]

        # Function to display quiz questions and collect user answers
    score = 0
    for i in range(10):
        st.write(f"**Question {i+1}:** {questions[i]}")
        selected_option = st.radio("", options[i], index=None)
        if selected_option == options[i][answers[i]-1]:
            score += 1
    submit = st.button("Submit",disabled=st.session_state.disabled)
    if submit:
        st.write(f"You got {score} out of 10 questions correct!")
        client = MongoClient('mongodb+srv://carboncalculator2024:zipzcwaQu1UnYTT5@carbonfootprint.febn7uz.mongodb.net/?retryWrites=true&w=majority&appName=carbonfootprint')
        db = client['carbon_footprint']
        collection = db['User_info']
        alldoc = collection.find_one({'Username':username}, {'Points':1,'_id':0})
        points=alldoc["Points"]
        collection.update_one({'Username':username},{'$set': {'Points':points+score*3}})
        st.success(f"You now have {points+score*3} points.")
