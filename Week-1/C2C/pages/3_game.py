import streamlit as st
import random
import time

st.set_page_config(
    page_title="Game",
    page_icon="🎰", 
)

# --------------------------------------------0
def set_shade_only():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: linear-gradient(
                rgba(56, 234, 140, 1),
                rgba(255, 255, 255, 0.75)
            );
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_shade_only()

# --------------------------------------------1
col1, col2, col3 = st.columns([3, 10, 1]) 
with col2:
    st.title(":rainbow[Guess The Number!] :sunglasses:" )

# --------------------------------------------2
number = st.number_input("Enter a number from 1 to 15", min_value=1, max_value=15)

# --------------------------------------------3
# Initialize session state variables
if "counter" not in st.session_state:
    st.session_state.counter = 3
if "rn" not in st.session_state:
    st.session_state.rn = random.randint(1, 15)
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Reset function
def reset_game():
    st.session_state.counter = 3
    st.session_state.rn = random.randint(1, 15)
    st.session_state.game_over = False

# When "Guess" button is clicked (only if game is not over)
if st.button("Guess", type="primary") and not st.session_state.game_over:
    st.session_state.counter -= 1

    if number == st.session_state.rn:
        st.success("## 🎉 Congratulations! You guessed the right number!")
        st.balloons()
        st.session_state.game_over = True
    else:
        if number < st.session_state.rn:
            hint = "🔼 The secret number is greater!"
        else:
            hint = "🔽 The secret number is smaller!"

        if st.session_state.counter > 0:
            st.warning(f"### ❌ Wrong guess! {hint}")
        else:
            st.error(f"## 💀 You lost! The correct number was :blue-background[{st.session_state.rn}].")
            st.session_state.game_over = True

# --------------------------------------------4
def reset_done():
    st.toast('Game Reset, You can play again!')
    time.sleep(1)
    
if st.session_state.game_over:
    if st.button("Play Again 🔄"):
        reset_game()
        reset_done()
else:
    st.write(f"Tries left: {st.session_state.counter}")


# -----------------------------------------------------------------------------------------------------Version 1
# import streamlit as st
# import random
# import time

# st.set_page_config(
#     page_title="Game",
#     page_icon="🎰", 
# )

# # --------------------------------------------0
# def set_shade_only():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-image: linear-gradient(
#                 rgba(255, 255, 255, 0.75),
#                 rgba(255, 255, 255, 0.55),
#                 rgba(56, 234, 140, 1)
#             );
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#             background-position: center;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# set_shade_only()


# # --------------------------------------------1
# col1, col2, col3 = st.columns([3, 10, 1]) 
# with col1:
#     pass

# with col2:
#     st.title(":rainbow[Guess The Number!] :sunglasses:" )

# with col3:
#     pass

# # --------------------------------------------2
# number = st.number_input("Enter a number from 1 to 15", min_value=1 , max_value=15)

# # --------------------------------------------3
# def wrong():
#     st.toast('Try Again', icon = "😥")
#     time.sleep(.5)

# def right():
#     st.toast('Congrats', icon = "🎉")
#     time.sleep(1)

# def guess_number(number):
#     rn = random.randint(1, 15)
#     if( number == rn ):
#         st.success("## Congratulations You Guessed The Right Number!!")
#         st.balloons()
#         right()
#     else: 
#         st.warning("### ❌ You,ve Guessed the wrong number, Try again!")
#         st.markdown(f"#### The number was: :blue-background[{rn}]")
#         wrong()
        

# if st.button("Guess", type = "primary"):
#     if number:
#         guess_number(number)
