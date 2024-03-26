import os 
import streamlit as st
from openai import OpenAI
from IPython.display import Image
from WhatIf_Method import WhatIfMethod as WhatIfMethod
import random


def main():
    
    st.set_page_config(
    page_title="What If Generator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    theme="dark"  # Choose a colorful theme (e.g., "light" or "dark")
    )

    st.title("🌈 Welcome to the What If Generator App")
    st.markdown("Explore the possibilities with vibrant colors!")
    st.success("Success message: Your creativity knows no bounds!")
    st.error("Error message: Oops! Let's try another scenario.")
    
    with st.sidebar:
        st.title("About App")
        st.write("""The What If Generator is your brainstorming buddy!  This app helps you explore possibilities, overcome creative roadblocks, and  approach challenges from new angles. Simply enter a situation or question  and get a random "what if" scenario to jumpstart your thinking.

Let's see where your imagination takes you!""")
    # Category Selection
    categories = ["Technology", "History", "Society", "Personal"]
    selected_category = st.selectbox("Choose a Category:", categories)

    user_input_msg = st.text_input("Enter a 'What if' scenario:", value=" What if humans could fly? e.g.")

    if st.button("Generate Random Scenario"):
        # Define a list of random scenarios
     random_scenarios = [
        "What if robots ruled the world?",
        "What if time travel was possible?",
        "What if dinosaurs still existed?",
        "What if humans could breathe underwater?",
        "What if teleportation became a reality?",
        # Add more scenarios here
    ]
    random_scenario = random.choice(random_scenarios)
    st.write("Random Scenario:", random_scenario)

    if st.button("Generate Response"):
        # Set the OpenAI API key
        OpenAI.api_key = st.secrets["OPENAI_API_KEY"]
        # Create an instance of the OpenAI class
        client = OpenAI()
        
        whatif_response = WhatIfMethod.whatif_ai(user_input_msg, client)
        st.write("Generated Text Response:")
        st.write(whatif_response)

        image_url = WhatIfMethod.pic_ai(user_input_msg, client)
        st.write("Generated Image URL:")
        st.write(image_url)

# Add themed illustrations or images
st.image("themed_illustration.jpg", caption="Imagination knows no bounds")

# Display themed emojis
st.write("Let your creativity soar! ✨🎨🚀")

# Themed background color
st.markdown(
    """
    <style>
    body {
        background-color: #f2f2f2;  /* dark */
    }
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()



    