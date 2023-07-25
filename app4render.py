import streamlit as st
import os
import time
import glob
import os

from gtts import gTTS
from googletrans import Translator

try:
    os.mkdir("temp")
except:
    pass
    
st.title("易翻译 | Easy Translation")
#st.markdown(f"## 【输入的文本中不可以包括符号【/等文件命名不允许的字符】，因为涉及【f+temp+/+my_file_name.mp3文件命名】")
#text = st.text_input("【输入的文本中不可以包括符号【/等文件命名不允许的字符】，因为涉及【f+temp+/+my_file_name.mp3文件命名】")
translator = Translator()

text = st.text_input("输入需要翻译的内容（注意：文本中请不要包括/等特殊符号）")
in_lang = st.selectbox(
    "请选择待翻译文本的语言",
    ("English", "Hindi", "Bengali", "korean", "Chinese Simplified", "Chinese Traditional", "Japanese"),
)
if in_lang == "English":
    input_language = "en"
elif in_lang == "Chinese Simplified":
    input_language = "zh-cn"
elif in_lang == "Chinese Traditional":
    input_language = "zh-TW"
elif in_lang == "Japanese":
    input_language = "ja"

out_lang = st.selectbox(
    "请选择文本翻译目标语言",
    ("English", "Hindi", "Bengali", "korean", "Chinese Simplified", "Chinese Traditional", "Japanese"),
)
if out_lang == "English":
    output_language = "en"
elif out_lang == "Chinese Simplified":
    output_language = "zh-CN"
elif out_lang == "Chinese Traditional":
    output_language = "zh-TW"
elif out_lang == "Japanese":
    output_language = "ja"

english_accent = st.selectbox(
    "请选择英文风格（当目标语言为英文时）",
    (
        "Default",
        "India",
        "United Kingdom",
        "United States",
        "Canada",
        "Australia",
        "Ireland",
        "South Africa",
    ),
)

if english_accent == "Default":
    tld = "com"
elif english_accent == "India":
    tld = "co.in"
elif english_accent == "United Kingdom":
    tld = "co.uk"
elif english_accent == "United States":
    tld = "com"
elif english_accent == "Canada":
    tld = "ca"
elif english_accent == "Australia":
    tld = "com.au"
elif english_accent == "Ireland":
    tld = "ie"
elif english_accent == "South Africa":
    tld = "co.za"

def text_to_speech(input_language, output_language, text, tld):
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text

if st.button("开始翻译并显示"): 
    st.markdown(f"## 输出的翻译文本（与收听的TTS语音相应）:")
    st.write(f" {output_text}")

#if display_output_text = st.checkbox("显示翻译文本（选择后会在语音播放翻译文本的同时显示翻译后的文本）")    
#    st.markdown(f"## 输出的翻译文本（与收听的TTS语音相应）:")
#    st.write(f" {output_text}")

if st.button("语音播放翻译内容"): 
    result, output_text = text_to_speech(input_language, output_language, text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    text = st.text_input("请点击播放按钮播放翻译内容语音")
#    st.markdown(f"## 请点击下方播放按钮收听TTS语音：")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

remove_files(7)
