import os
import streamlit as st
from openai import OpenAI
# Remove IPython.display since it's not needed for Streamlit
# from IPython.display import Image
from WhatIf_Method import WhatIfMethod as WhatIfMethod
import random

def main():
    st.sidebar.title("About App")
    # ... (similar to your code)

    st.title(" What If Generator with OpenAI")

    user_input_msg = st.text_input("Enter a 'What if' scenario:", value=" What if humans could fly? e.g.")

    num_possibilities = st.slider("Number of Possibilities to Generate", min_value=1, max_value=5, value=1)

    if st.button("Generate Scenarios"):
        OpenAI.api_key = st.secrets["OPENAI_KEY"]
        client = OpenAI()

        # Generate multiple possibilities using a loop
        possibilities = []
        for _ in range(num_possibilities):
            whatif_response = WhatIfMethod.whatif_ai(user_input_msg, client)
            possibilities.append(whatif_response)

        # Display generated possibilities with markdown
        st.write(f"Generated {num_possibilities} Possibilities:")
        for i, possibility in enumerate(possibilities):
            st.subheader(f"Possibility {i+1}")
            st.markdown(possibility)  # Use markdown for each possibility

if __name__ == "__main__":
    main()
