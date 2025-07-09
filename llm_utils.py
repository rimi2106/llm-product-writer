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
