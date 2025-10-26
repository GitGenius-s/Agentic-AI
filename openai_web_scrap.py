import os
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI
# import web_scrap
from web_scrap import Website

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

website = Website("https://cnn.com/")
# print(website.content_preview)
openai = OpenAI()
system_prompt = """
You are a snarkyassistant that analyzes the contents of a website,
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
response = openai.chat.completions.create(
    model='gpt-5-nano',
    messages=messages
)
print(response.choices[0].message.content)