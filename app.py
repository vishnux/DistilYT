from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import gradio as gr
from gradio.mix import Series

def generate_transcript(url):
 
    text = url[url.index("=")+1:]
    transcript = YouTubeTranscriptApi.get_transcript(text)

    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)

    return text_formatted
    
transcriber = gr.Interface(generate_transcript, 'text', 'text')
summarizer = gr.Interface.load("huggingface/facebook/bart-large-cnn")

description =  '''
        This application summarizes a YouTube video based on its transcript. 
        Enter a Youtube video URL and click submit for obtaining a summary. 
        '''

youtube_url_examples = [['https://www.youtube.com/watch?v=MBRqu0YOH14'],
              ['https://www.youtube.com/watch?v=UjtOGPJ0URM']]
              
#Videos taken from Kurzgesagt – In a Nutshell       
     
iface = Series(transcriber, summarizer,
                  inputs = gr.inputs.Textbox(label = "Enter the YouTube URL"),
                  outputs = gr.outputs.Textbox(label = "Transcript Summary"),
                  examples = youtube_url_examples,
                  title = "Distil YouTube",
                  theme = "grass",
                  description = description)

iface.launch()     
