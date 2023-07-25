import streamlit as st
import os
import time
import glob
import os

from gtts import gTTS
from googletrans import Translator

#try:
#    os.mkdir("temp")
#except:
#    pass

# Set the title, favicon, page icon, and layout of the webpage or app
st.set_page_config(
    page_title="易翻译·EZTranslation - 你的随身翻译助手",
    page_icon=":rocket:",  # You can use Emoji as the page icon
    layout="centered",  # You can set the layout to "wide" or "centered"
)

# Set the title and other configurations
st.title("易翻译 | Easy Translation")

st.write("---")

translator = Translator()

in_lang = st.selectbox(
    "请选择待翻译文本的语言",
    ("Chinese", "English", "German", "French", "Japanese", "Korean"),
)
if in_lang == "Chinese":
     input_language = "zh-CN"
#elif in_lang == "Chinese Traditional":
#    input_language = "zh-TW"
elif in_lang == "English":
    input_language = "en"
elif in_lang == "German":
    input_language = "de"
elif in_lang == "French":
    input_language = "fr"
elif in_lang == "Japanese":
    input_language = "ja"
elif in_lang == "Korean":
    input_language = "kr"

st.write("---")
out_lang = st.selectbox(
    "请选择文本翻译目标语言",
    ("English", "Chinese", "German", "French", "Japanese", "Korean"),
)
if out_lang == "English":
    output_language = "en"
elif out_lang == "Chinese":
    output_language = "zh-CN"
#elif out_lang == "Chinese Traditional":
#    output_language = "zh-TW"
elif out_lang == "German":
    output_language = "de"
elif out_lang == "French":
    output_language = "fr"
elif out_lang == "Japanese":
    output_language = "ja"
elif out_lang == "Korean":
    output_language = "kr"

st.write("---")

# Pre-filled text for the text_input widget
pre_filled_text = "Hi"

# Create the text_input widget with pre-filled text
text = st.text_input("输入需要翻译的内容", value=pre_filled_text)
tips_text = "请在上方输入框中输入需要翻译的内容"

def text_to_speech(input_language, output_language, text):
    if text is None:
        trans_text = tips_text
        return trans_text
    else:
        translation = translator.translate(text, src=input_language, dest=output_language)
        trans_text = translation.text
        tts = gTTS(trans_text, lang=output_language, slow=False)
        tts.save("translationresult.mp3")
        return trans_text

if text is not None:
    st.write("翻译结果")
    output_text = text_to_speech(input_language, output_language, text)
    st.write(f" {output_text}")
else:
    st.write("请在上方输入框中输入需要翻译的内容")
    st.stop()

display_output_text = st.checkbox("语音播放翻译结果")
if display_output_text:
    output_text = text_to_speech(input_language, output_language, text)
    audio_file = open("translationresult.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio("translationresult.mp3")
#    st.write(f" {output_text}")
#if text is None:
#    st.write("请在上方输入框中输入需要翻译的内容")
#    st.stop()
 
#    在手机端，下面这行代码会导致错误（手机上无法播放）
#    st.audio(audio_bytes, format="audio/mp3", start_time=0)

#os.remove(f"translationaudio.mp3")

#def remove_files(n):
#    mp3_files = glob.glob("temp/*mp3")
#    if len(mp3_files) != 0:
#        now = time.time()
#        n_days = n * 86400
#        for f in mp3_files:
#            if os.stat(f).st_mtime < now - n_days:
#                os.remove(f)
#                print("Deleted ", f)

#remove_files(7)
