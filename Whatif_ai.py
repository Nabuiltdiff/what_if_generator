import os 
import streamlit as st
from openai import OpenAI
from IPython.display import Image
from WhatIf_Method import WhatIfMethod as WhatIfMethod
import random


def main():
    
    with st.sidebar:
        st.title("About App")
        st.write("""The What If Generator is your brainstorming buddy!  This app helps you explore possibilities, overcome creative roadblocks, and  approach challenges from new angles. Simply enter a situation or question  and get a random "what if" scenario to jumpstart your thinking.

Let's see where your imagination takes you!""")
        
    # Category Selection
        st.title("🤖 What If Generator with OpenAI")
    categories = ["general, Technology", "History", "Society", "Personal"]
    selected_category = st.selectbox("Choose a Category:", categories)

    user_input_msg = st.text_input("Enter a 'What if' scenario:", value=" What if humans could fly? e.g.")

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

if __name__ == "__main__":
    main()



    