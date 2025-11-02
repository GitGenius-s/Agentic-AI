# from youtube_transcript_api import YouTubeTranscriptApi
# ytt_api = YouTubeTranscriptApi()
# video_id = "EO8QoyRSVaw"
# print(video_id)

# fetched_transcript = ytt_api.fetch(video_id,languages=['en'],preserve_formatting=True)
# # for snippet in fetched_transcript:
#     # print(snippet.text)
# full_text = " ".join([item.text for item in fetched_transcript])
# print(full_text)

# last_snippet = fetched_transcript[-1]
# snippet_count = len(fetched_transcript)
# print(f"Total snippets: {snippet_count}")
# print(f"Last snippet: {last_snippet}")
# print(ytt_api.list(video_id))
# print(transcript_list)
# ytt_api = YouTubeTranscriptApi()
# transcript_list = ytt_api.list(video_id)
# transcript = transcript_list.find_transcript(['en'])
# translated_transcript = transcript.translate('ko')
# print(translated_transcript.fetch())

import gradio_task as gr
print(gr.__version__)
