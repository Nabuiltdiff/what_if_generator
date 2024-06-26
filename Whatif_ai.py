import os
import streamlit as st
from openai import OpenAI
# Remove IPython.display since it's not needed for Streamlit
# from IPython.display import Image
from WhatIf_Method import WhatIfMethod as WhatIfMethod
import random

def main():
    st.sidebar.title("About App")
    st.sidebar.write("""**The What If Generator** is your brainstorming buddy! 

Explore possibilities, overcome creative roadblocks, and approach challenges from new angles. Simply enter a situation or question and get a random "what if" scenario to jumpstart your thinking.

Let's see where your imagination takes you! """)

    st.title("🤖 What If Generator with OpenAI")

    user_input_msg = st.text_input("Enter a 'What if' scenario:", value=" What if humans could fly? e.g.")

    num_possibilities = st.slider("Number of Possibilities to Generate", min_value=1, max_value=5, value=1)

    if st.button("Generate Scenarios"):
        OpenAI.api_key = st.secrets["OPENAI_API_KEY"]
        client = OpenAI()

        # Generate multiple possibilities using a loop
        possibilities = []
        images = []  # List to store image URLs
        for _ in range(num_possibilities):
            whatif_response = WhatIfMethod.whatif_ai(user_input_msg, client)
            image_url = WhatIfMethod.pic_ai(user_input_msg, client)
            possibilities.append(whatif_response)
            images.append(image_url)

        # Display generated possibilities with markdown and images
        st.write(f"Generated {num_possibilities} Possibilities:")
        for i, (possibility, image_url) in enumerate(zip(possibilities, images)):
            st.subheader(f"Possibility {i+1}")
            st.markdown(possibility)
            if image_url:  # Check if image URL exists
                st.image(image_url, caption=f"Visual representation of Possibility {i+1}")

if __name__ == "__main__":
    main()
