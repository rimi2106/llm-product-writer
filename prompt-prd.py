#pip install -r requirements.txt

import streamlit as st
from llm_utils import generate_requirements


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
