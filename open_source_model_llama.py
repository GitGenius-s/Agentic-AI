import os
from dotenv import load_dotenv
from openai import OpenAI
from web_scrap import Website

OLLAMA_BASE_URL = "http://localhost:11434/v1"
website = Website("https://cnn.com/")

ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')
system_prompt = """
You are a assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""
user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
"""
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt_prefix+website.content_preview}
]
response = ollama.chat.completions.create(
    model="llama3.2", 
    messages = messages
)

print(response.choices[0].message.content)