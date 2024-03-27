import streamlit as st
from openai import OpenAI
import random
from WhatIf_Method import WhatIfMethod as WhatIfMethod

def main():
    st.sidebar.title("About App")
    # ... (similar to your code)

    st.title(" What If Generator with OpenAI")

    user_input_msg = st.text_input("Enter a 'What if' scenario:", value="What if humans could fly? e.g.")
    selected_format = st.selectbox("Choose Response Format:", ["Text", "Poem", "Script"])

    if st.button("Generate Scenario"):
        OpenAI.api_key = st.secrets["OPENAI_API_KEY"]
        client = OpenAI()

        # Adjust instructions based on selected format
        instructions = {
            "Text": "",
            "Poem": "Write a poem about the scenario",
            "Script": "Write a short script scene depicting the scenario"
        }[selected_format]

        whatif_response = WhatIfMethod.whatif_ai(f"{instructions}\n{user_input_msg}", client)
        st.write(f"Generated {selected_format} Response:")
        st.markdown(whatif_response)

        image_url = WhatIfMethod.pic_ai(user_input_msg, client)
        st.image(image_url, caption="A visual representation of the scenario")

        # Example twist input
        twist_prompt = st.text_input("Add an unexpected twist (optional):")
        if twist_prompt:
            st.subheader("Scenario with a Twist:")
            st.write(WhatIfMethod.whatif_ai(f"{whatif_response}\n{twist_prompt}", client))

if __name__ == "__main__":
    main()
