import gradio as gr
import assemblyai as aai
from translate import Translator
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import uuid
from pathlib import Path

def voice_to_voice(audio_file):

    #transcribe audio
    transcription_response = audio_transcription(audio_file)

    if transcription_response.status == aai.TranscriptStatus.error:
        raise gr.Error(transcription_response.error)
    else:
        text = transcription_response.text

    es_translation, gu_translation, ja_translation = text_translation(text)

    es_audi_path = text_to_speech(es_translation)
    gu_audi_path = text_to_speech(gu_translation)
    ja_audi_path = text_to_speech(ja_translation)
    
    es_path = Path(es_audi_path)
    gu_path = Path(gu_audi_path)
    ja_path = Path(ja_audi_path)

    return es_path, gu_path, ja_path
    
def audio_transcription(audio_file):

    aai.settings.api_key = "3bfb568efbf8400a85570d553664375e"

    transcriber = aai.Transcriber()
    transcription=transcriber.transcribe(audio_file)

    return transcription

def text_translation(text):
    translator_es = Translator(from_lang="en", to_lang="es")
    es_text = translator_es.translate(text)

    translator_gu = Translator(from_lang="en", to_lang="gu")
    gu_text=translator_gu.translate(text)

    translator_ja = Translator(from_lang="en", to_lang="ja")
    ja_text = translator_ja.translate(text)

    
    return es_text, gu_text, ja_text


def text_to_speech(text):
    elevenlabs = ElevenLabs(
        api_key="sk_f75a6d10dd1c9d79c8be1dc73b70bdc30645e846f0e750c5",
    )

    # Calling the text_to_speech conversion API with detailed parameters
    response = elevenlabs.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2", # use the turbo model for low latency
        # Optional voice settings that allow you to customize the output
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.5,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )
    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"
    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    print(f"{save_file_path}: A new audio file was saved successfully!")
    # Return the path of the saved audio file
    return save_file_path

audio_input=gr.Audio(
    sources=["microphone"],
    type="filepath"
)    

demo=gr.Interface(
    fn=voice_to_voice,
    inputs=audio_input,
    outputs=[gr.Audio(label="Spanish"), gr.Audio(label="Gujrati"), gr.Audio(label="Japanese")]


)




if __name__ == "__main__":
    demo.launch()
