pip install -r requirements.txt

import streamlit as st
from llm_utils import generate_requirements

import os
os.environ["OPENAI_API_KEY"] = "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"
%%writefile app.py
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
%%writefile llm_utils.py
import os
from openai import OpenAI

# Use OpenAI's new client-based interface
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_requirements(user_text):
    prompt = f"""
You are an expert Product Manager and Technical Writer.
Based on the following user feedback, generate structured product requirements including:
- A summary of the problem
- One or more user stories (in the format: As a [user], I want [action], so that [benefit])
- Feature suggestions
- Acceptance criteria

Customer Feedback:
\"\"\"
{user_text}
\"\"\"

Output in Markdown format.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes product requirements."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=1000
    )

    return response.choices[0].message.content

import subprocess
import time
from pyngrok import ngrok

# Kill previous ngrok if needed
!pkill -f streamlit

# Start Streamlit app in background
process = subprocess.Popen(["streamlit", "run", "app.py"])

# Wait for Streamlit to initialize
time.sleep(5)

# Connect via ngrok to port 8501
public_url = ngrok.connect(8501)
print(f"🚀 Streamlit app is live at: {public_url}")
