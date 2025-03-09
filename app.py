#streamlit 
import streamlit as st

st.set_page_config(page_title="Growth_Mindset_Program", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("♥♥ Welcome to your Growth journey!")
st.write("Embrace challenges,learn from mistakes,and unlock your full potential.This AI-powered app will help you build a growth mindset with reflection,challenges,and achievements.")

#quote section
st.header("🌹 Today's Growth Mindset Quote")
st.write('"The only limit to the height of your achievements is the reach of your dreams and your willingness to work for them." - Michelle Obama')


st.header("🏹 what's your challenge today?")
user_input = st.text_input("describe a challenge you're facing")

#condition
if user_input:
  st.success(f"💪 you're facing: {user_input} keep pushing forward towards your goals!")
else:
    st.warning("Tell us about your challenge to get started!")

 #reflexing
st.header("🌱reflect on your learing")
reflection = st.text_area("write your reflection here:")
if reflection:
    st.success(f" ✨great insights! keep reflecting and growing: {reflection}")
else:
    st.info("Reflection on past experiences can help you grow! share your  difficulties")

 #achievements
st.header("🏆celebrate your wins!")
achievements = st.text_input("share something you have recently accomplished")
if achievements:
    st.success(f"🎉Amazing! You achieved: {achievements}")
else:
    st.info("big or small, every achievement counts! share one now ✌")

#footer
st.write("- - -")
st.write("keep believing in yourself,Growth is a journey, not a destination. 😐")
st.write(" ** created by umair khan **")
