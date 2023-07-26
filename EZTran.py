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

in_lang = st.selectbox(
    "第一步：选择翻译内容源语言",
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
    "第二步：选择目标翻译语言",
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

tips_text = "请在上方输入框中输入需要翻译的内容"

#text = st.text_input(label="输入需要翻译的内容", value="易翻译EasyTransation", placeholder='在此输入Enter here')

translator = Translator()
placeholder = st.empty()

text = placeholder.text_input(label="输入需要翻译的内容（请务必先输入要翻译的内容再查看翻译或播放语音）", value="", placeholder='在此输入Enter here', key=1)

display_output_text = st.checkbox("语音播放翻译结果")

click_clear = st.button('清空输入框', key=3)

def text_to_speech(input_language, output_language, text):
    try:
        translator = Translator()
        translation = translator.translate(text, src=input_language, dest=output_language)
        trans_text = translation.text
        tts = gTTS(trans_text, lang=output_language, slow=False)
        tts.save("translationresult.mp3")
        return trans_text
    except Exception as e:
        # Handle the error, e.g., print an error message or return a default text
        print(f"Translation error: {e}")
        return "要翻译内容为空"
        st.stop()

if text is None:
    st.stop()
else: 
    if text is not None:
        st.write("翻译结果")
        output_text = text_to_speech(input_language, output_language, text)
        st.write(f" {output_text}")
    else:
        st.write("请在上方输入框中输入需要翻译的内容")
        st.stop()
    if click_clear:
        text = placeholder.text_input(label="输入需要翻译的内容（请务必先输入要翻译的内容再查看翻译或播放语音）", value="", placeholder='在此输入Enter here', key=2)
        st.stop()

    if display_output_text:
        try:
            output_text = text_to_speech(input_language, output_language, text)
            audio_file = open("translationresult.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio("translationresult.mp3")
        except Exception as e:
            # Handle the error, e.g., print an error message or return a default text
            print(f"Translation error: {e}")            
            st.stop()
