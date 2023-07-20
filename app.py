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
st.title("文字/文本转语音App-Streamlit")
st.markdown(f"## 【输入的文本中不可以包括符号【/】，因为涉及【f+temp+/+my_file_name.mp3文件命名】")
translator = Translator()

text = st.text_input("输入需要翻译的内容")
in_lang = st.selectbox(
    "请选择输入语言",
    ("English", "Hindi", "Bengali", "korean", "Chinese", "Japanese"),
)
if in_lang == "English":
    input_language = "en"
elif in_lang == "Chinese":
    input_language = "zh-cn"
elif in_lang == "Japanese":
    input_language = "ja"

out_lang = st.selectbox(
    "请选择输出语言",
    ("English", "Hindi", "Bengali", "korean", "Chinese", "Japanese"),
)
if out_lang == "English":
    output_language = "en"
elif out_lang == "Chinese":
    output_language = "zh-cn"
elif out_lang == "Japanese":
    output_language = "ja"

english_accent = st.selectbox(
    "请选择英文风格",
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

display_output_text = st.checkbox("显示翻译文本")

if st.button("翻译文本转语音"):
    result, output_text = text_to_speech(input_language, output_language, text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## 请点击下方播放按钮收听TTS语音：")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    if display_output_text:
        st.markdown(f"## 输出的翻译文本（与收听的TTS语音相应）:")
        st.write(f" {output_text}")

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)

remove_files(7)
