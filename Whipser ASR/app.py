import whisper
from pytube import YouTube
import gradio as gr
import os


tiny_model = whisper.load_model('tiny')
base_model = whisper.load_model('base')
small_model = whisper.load_model('small')
medium_model = whisper.load_model('medium')


def yt_audio(video_url):
	yt = YouTube(str(video_url))
	video = yt.streams.filter(only_audio=True).first()
	destination = 'Files/'
	audio_file = video.download(output_path=destination)
	base, ext = os.path.splitext(audio_file)
	file_path = base + '.mp3'
	os.rename(audio_file, file_path)
	
	return str(file_path)


def transcribe(model_type ,video_url):

    if model_type == 'Tiny':
        model = tiny_model
    elif model_type == 'Base':
        model = base_model
    elif model_type == 'Small':
        model = small_model
    elif model_type == 'Medium':
        model = medium_model
    
    
    file_path = yt_audio(video_url)

    trascription_dict = model.transcribe(file_path)
    text = trascription_dict['text']
    language = trascription_dict['language']

    return text, language


demo_app = gr.Interface(
    title = "Youtube video transcription",
    description = "Youtube video transcription using OpenAI's Whisper models \n\n 1. Select Model, \n 2. Pick a Youtube video, copy the video URL, \n 3. Paste URL in the Youtube Video URL input box and click the 'Submit' button",
    fn = transcribe,
    inputs = [  gr.Dropdown(choices=['Tiny', 'Base' ,'Small', 'Medium'], label="Model", default='Base'),
                gr.Textbox(lines=1, placeholder="Youtube Video URL", label="Video URL"),],

    outputs = [ gr.Textbox(placeholder="Transcription.", interactive=True, label="Transcription"),
                gr.Text(placeholder="Detected Language.", interactive=False, label="Language"),],

    #examples = speech_samples,     # will be added in next update.
    
    allow_flagging = "never",
)

demo_app.launch(share=True, inbrowser=True)