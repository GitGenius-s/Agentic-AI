import os
import json
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI
from web_scrap import Website
from openai import OpenAI
from rich.markdown import Markdown
from rich.console import Console

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-5-nano'
openai = OpenAI()

website = Website("https://qoruz.com")
# # print(website.content_preview)
# link = (website.fetch_website_link("https://flexable.work/"))
# for l in link:
#     print(l)

link_system_prompt = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company,
such as links to an About page, or a Company page.
You should respond in JSON as in this example:

{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
    ]
}
"""

def get_links_user_prompt(url):
    user_prompt = f"""
Here is the list of links on the website {url} -
Please decide which of these are relevant web links for a brochure about the company, 
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.
"""
    links = website.fetch_website_link(url)
    user_prompt += "\n".join(links)
    return user_prompt

# print(get_links_user_prompt("https://qoruz.com/"))


def select_relevant_links(url):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(url)}
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    links = json.loads(result)
    print(f"Found {len(links['links'])} relevant links")
    return links

# print(select_relevant_links("https://qoruz.com/"))

def fetch_page_and_all_relevant_links(url):
    website = Website(url)
    relevant_links = select_relevant_links(url)
    result = f"## Landing Page:\n\n{website.content_preview}\n## Relevant Links:\n"
    for link in relevant_links['links']:
        result += f"\n\n### Link: {link['type']}\n"
        website = Website(link["url"])
        result += website.content_preview + "\n"
    return result

# print(fetch_page_and_all_relevant_links("https://qoruz.com/"))

brochure_system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors and recruits.
Respond in markdown without code blocks.
Include details of company culture, customers if you have the information.
"""

def get_brochure_user_prompt(company_name, url):
    user_prompt = f"""
You are looking at a company called: {company_name}
Here are the contents of its landing page and other relevant pages;
use this information to build a short brochure of the company in markdown without code blocks.\n\n
"""
    user_prompt += fetch_page_and_all_relevant_links(url)
    user_prompt = user_prompt[:5_000] # Truncate if more than 5,000 characters
    return user_prompt


def create_brochure(company_name, url):
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": brochure_system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ],
    )
    result = response.choices[0].message.content
    console = Console()
    md = Markdown(result)
    console.print(md)

create_brochure("qoruz", "https://qoruz.com/")