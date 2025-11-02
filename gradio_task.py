import os
from dotenv import load_dotenv
from openai import OpenAI

import gradio as gr # oh yeah!
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

openai = OpenAI()

system_prompt = "You are a helpful assistance"

def msg_prompt(prompt):
    message = [{"role" : "system","content": system_prompt},{"role" : "user","content": prompt}]
    response = openai.chat.completions.create(model='gpt-4.1-mini',messages=message)
    return response.choices[0].message.content

print(msg_prompt("what is today's date?"))

def shout(text):
    print(f"Shout is called with input {text}")
    return text.upper()  

shout("hello")

# gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch()
gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch(inbrowser=True,auth=('gradio','gradio@123'))
