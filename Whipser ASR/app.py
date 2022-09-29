import whisper
from pytube import YouTube
import gradio as gr
import os

def yt_audio(video_url):
  	yt = YouTube(str(video_url))
  	video = yt.streams.filter(only_audio=True).first()
  	destination = 'Files/'
  	audio_file = video.download(output_path=destination)
  	base, ext = os.path.splitext(audio_file)
  	file_path = base + '.mp3'
  	os.rename(audio_file, file_path)
  	
  	return str(file_path)                                      # Returns the path of the downloaded audio file
  	


model = whisper.load_model('base')


def transcribe(video_url):
    # generate a file path
    file_path = yt_audio(video_url)

    # Transcribe audio file
    trascription_dict = model.transcribe(file_path)
    text = trascription_dict['text']
    language = trascription_dict['language']

    return text
    
demo = gr.Interface(
    title = "Youtube Video Transcription",
    description = "Youtube video transcription using OpenAI's Whisper 'Small' model \n\n 1. Pick a youtube video, \n 2. Left click on the video and copy Video URL, \n 3. Paste URL in the video_url input box and click the 'Submit' button",
    fn = transcribe,
    inputs=gr.Textbox(lines=1, placeholder="Youtube Video URL"),
    outputs=gr.Textbox(placeholder="Transcription.", interactive=True),
)


demo.launch(inline = False)