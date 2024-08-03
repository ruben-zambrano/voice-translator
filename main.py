import gradio as gr
import whisper
from translate import Translator
from dotenv import dotenv_values
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

config= dotenv_values(".env")

ELEVENLABS_API_KEY = config["ELEVENLABS_API_KEY"]

def text_to_speech(text: str, language: str) -> str:
    try:
        eleven_labs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        response = eleven_labs_client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",  # Adam pre-made voice
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        save_file_path = f"audios/{language}.mp3"

        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

        return save_file_path
    
    except Exception as e:
        raise gr.Error(
            f"Error converting text to speech: {str(e)}"
        )

def translator(audio_file):
  
  try:
    model = whisper.load_model("base")
    result = model.transcribe(audio_file, language="Spanish", fp16=False)
    transcription = result["text"]
  except Exception as e:
    raise gr.Error(
        f"Error transcribing audio: {str(e)}"
    )
  
  try:
    en_translation = Translator(from_lang="es",to_lang="en").translate(transcription)
    it_translation = Translator(from_lang="es",to_lang="it").translate(transcription)
    fr_translation = Translator(from_lang="es",to_lang="fr").translate(transcription)
    de_translation = Translator(from_lang="es",to_lang="de").translate(transcription)

  except Exception as e:
    raise gr.Error(
        f"Error translating text: {str(e)}"
    )
  
  try:
    en_save_file_path = text_to_speech(en_translation, "en")
    it_save_file_path = text_to_speech(it_translation, "it")
    fr_save_file_path = text_to_speech(fr_translation, "fr")
    de_save_file_path = text_to_speech(de_translation, "de")

    return en_save_file_path, it_save_file_path, fr_save_file_path, de_save_file_path
    
  except Exception as e:
    raise gr.Error(
        f"Error translating text and saving audio: {str(e)}"
    )

web = gr.Interface(
fn=translator,
inputs=gr.Audio(
  sources=["microphone"],
  type="filepath",
  label="Spanish"
),
outputs=[
    gr.Audio(label="English"),
    gr.Audio(label="Italian"),
    gr.Audio(label="French"),
    gr.Audio(label="German"),
],
title="Voice translator",
description="Translate your voice to any language with AI"
)

web.launch()