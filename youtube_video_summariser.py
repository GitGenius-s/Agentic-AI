import os
import re
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI
from web_scrap import Website
from youtube_transcript_api import YouTubeTranscriptApi
load_dotenv(override=True)
from rich.markdown import Markdown
from rich.console import Console

api_key = os.getenv('OPENAI_API_KEY')

class YouTubeWebLink:
    def __init__(self, url):
        self.url = url
        self.video_id = self.get_video_id(url)
        self.set_openai_client()
        self.set_system_prompt()

    def get_video_id(self, url):
        """ extract youtube video id from url with regular expression """
        regex = r"(?:v=|be/)([a-zA-Z0-9_-]{11})"
        match = re.search(regex, url)
        if match:
            return match.group(1)
        else:
            raise ValueError("Probably not a YouTube URL")
        
    def set_openai_client(self):    
        self.openai = OpenAI()
        
    def set_system_prompt(self, system_prompt=None):
        """ set system prompt from youtube video """
        self.system_prompt = """
        You are a skilled explainer and storyteller who specializes in summarizing YouTube video transcripts in a way that's both engaging and informative. 
        Your task is to:
        - Capture key points and main ideas of the video
        - Structure your summary with in clear sections
        - Include important details, facts, and figures mentioned
        - Never end your summary with a "Conclusion" section
        - Keep the summary short and easy to understand
        - Always format your response in markdown for better readability
        """ if system_prompt is None else system_prompt

    def get_transcript(self):
        try:
            ytt_api = YouTubeTranscriptApi()
            video_id = "EO8QoyRSVaw"

            fetched_transcript = ytt_api.fetch(video_id,languages=['en'],preserve_formatting=True)
            # for snippet in fetched_transcript:
                # print(snippet.text)
            full_text = " ".join([item.text for item in fetched_transcript])
            return full_text

        except Exception as fallback_error:
            print(f"Still failed: {fallback_error}")
            return None
        
    def get_summary_from_transcript(self, transcript):
        """ summarize text using openai """
        try:
            print('Summarizing video...')
            response = self.openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"Summarize the following YouTube video transcript:\n\n{transcript}"}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error summarizing text: {e}")
            return None

    def display_summary(self):
        """ summarize youtube video """
        transcript = self.get_transcript()
        # print(transcript)
        summary = self.get_summary_from_transcript(transcript)
        console = Console()
        console.print(Markdown(summary))

# test_url_1 = "https://www.youtube.com/watch?v=nYy-umCNKPQ&list=PLWHe-9GP9SMMdl6SLaovUQF2abiLGbMjs"
# test_url_2 = "https://youtu.be/nYy-umCNKPQ?si=ILVrQlKT0W71G5pU"

test_url_1 = "https://www.youtube.com/watch?v=EO8QoyRSVaw"
video1 = YouTubeWebLink(test_url_1)
print(video1.video_id), 
# print(video2.video_id)

video1.display_summary()
# video2.display_summary()