import streamlit as st
import logging
import pandas as pd
from random import randint

logger = logging.getLogger(__name__)

st.set_page_config(page_title="World Capitals Quiz",
                   page_icon=":mortar_board:")
st.title('World Capitals Quiz \n *for Xenia*')

# color "st.buttons" in main page light blue: #(0, 100, 160)
st.markdown("""
<style>
div.stButton > button:first-child {
     background-color: rgb( 0, 131, 184)
 }
 </style>""", unsafe_allow_html=True)
# hide menu
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

# site-structure and main-widgets:
first = st.container()
second = st.container()
start = st.sidebar.button("Start")
end = st.sidebar.button("Quit")
next = second.button("Next")

# Dictionary of all capitals and capitals in Europe
df = pd.read_csv("./data/capitals.csv", sep=";", header=None)
world = dict(zip(df[1],df[0]))

# initiate necessary session_state-variables #########
if 'capitals' not in st.session_state:
    st.session_state['capitals'] = list(world.keys())
# number of questions asked:
if 'questions' not in st.session_state:
    st.session_state['questions'] = 0
if 'right' not in st.session_state:
    st.session_state['right'] = 0
if 'wrong' not in st.session_state:
    st.session_state['wrong'] = 0
if 'capital' not in st.session_state:
    st.session_state['country'] = ""
if 'last' not in st.session_state:
    st.session_state['last'] = "last"
# 'number' stores the number of capitals remaining:
if 'number' not in st.session_state:
    st.session_state['number'] = len(st.session_state['capitals'])-1
x = randint(0, st.session_state['number'])
# 'capital' stores the capital in the current question:
if 'capital' not in st.session_state:
    st.session_state['capital'] = st.session_state['capitals'][x]

def new():
    try:
        x = randint(0, st.session_state['number'])
    except:
        quit()
    st.session_state['capital'] = st.session_state['capitals'][x]

def grade(perc):
    if perc == 100:
        grade = "fantastic! (??????????????????????)???"
    elif perc > 80:
        grade = "very good! (?? ?????????)??"
    elif perc > 60:
        grade = "pretty good! ( ???? ?? ????)"
    elif perc > 40:
        grade = "ok! (~ ??? ??? ???)~"
    elif perc > 20:
        grade = "pretty bad! (?? ???_???)??"
    else:
        grade = "sad! (?? ?????????)??"
    return grade

def reset():
    # reset values:
    st.session_state['capitals'] = list(world.keys())
    st.session_state['number'] = len(st.session_state['capitals'])-1
    st.session_state['questions'] = 0
    st.session_state['right'] = 0
    st.session_state['wrong'] = 0
    st.session_state['country'] = ""

def main():
    capital = st.session_state['capital']
    first.markdown(f"Which country has **{capital}** as it's capital?")
    country = first.text_input("", "", key=st.session_state['questions'])
    if country != st.session_state['last'] and country != "":
        st.session_state['last'] = country
        st.session_state['questions'] += 1
        st.session_state['country'] = country
        if st.session_state['country'] == world[capital]:
            st.session_state['capitals'].remove(capital)
            st.session_state['right'] += 1
            st.session_state['number'] -= 1
            if st.session_state['number'] == -1:
                perc = st.session_state['right'] * 100 / st.session_state['questions']
                second.write(f"You know all capitals in the world (?? ??0??)?? and answered {st.session_state['right']} of {st.session_state['questions']} questions correctly ({int(round(perc,0))} percent).")
                second.write(f"That's {grade(perc)}")
                reset()
            else:
                second.write("That's correct. (???^???^)")
                second.write(f"{st.session_state['right']} of {st.session_state['questions']} ({str(st.session_state['number']+1)} countries remaining)")

        else:
            st.session_state['wrong'] += 1
            second.write(f"'{country}' is wrong. (?? ?????????)??  **{capital}** is the capital of: **{world[st.session_state['capital']]}**")
            second.write(f"{st.session_state['right']} of {st.session_state['questions']} ({str(st.session_state['number']+1)} countries remaining)")

def quit():
    try:
        perc = st.session_state['right'] * 100 / st.session_state['questions']
    except:
        perc = 0
    second.write(f"You answered {st.session_state['right']} of {st.session_state['questions']} questions correctly ({int(round(perc,0))} precent).")
    second.write(f"That's {grade(perc)}")
    reset()

if end:
    quit()

if start:
    new()

if next:
    new()


#########################################################################
if __name__ == '__main__':
    main()
