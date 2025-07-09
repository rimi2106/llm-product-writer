import streamlit as st
from llm_utils import generate_requirements

st.set_page_config(page_title="AI Product Requirements Generator")
st.title("🧠 LLM-Powered Product Requirements Generator")

st.markdown("Upload customer feedback or type in raw user insights, and get structured product requirements (user stories, PRDs, etc.)!")

user_input = st.text_area("Paste customer feedback or interview notes:", height=250)

if st.button("Generate Requirements"):
    if user_input.strip():
        with st.spinner("Generating product requirements..."):
            output = generate_requirements(user_input)
            st.subheader("Generated Output")
            st.markdown(output)
            st.download_button("Download PRD", output, file_name="requirements.md")
    else:
        st.warning("Please paste some input to proceed.")
