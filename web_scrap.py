from bs4 import BeautifulSoup
import requests
class Website:
    """
    A class that represent a website that we have scrapped
    """
    url: str
    title: str
    text: str

    def __init__(self,url):
        """
         Create this website object from given url using beatiful soup  library
        """
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else 'No Title'
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""
        self.content_preview = (self.title + "\n\n" + self.text)[:2000]
        # return (self.title + "\n\n" + self.text)[:2000]

# sel = Website("https://edwarddonner.com")
# print(sel.title)
# print(sel.text)

"""
open source model
1.Llama from meta
2.Mistral from mistral
3.Qwen from alibaba cloud
4.Gemma from google
5.phi from microsoft
6.Deepseek from DeepSeek Ai
7.GPT-OSS from openai
Inferance (Running the model)
"""