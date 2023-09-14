import streamlit as st
import os
import time
import glob
import sys
from gtts import gTTS
from googletrans import Translator

#try:
#    os.mkdir("temp")
#except:
#    pass

# Set the title, favicon, page icon, and layout of the webpage or app and other configurations
st.set_page_config(
    page_title="易翻译·EZTranslation - 你的随身翻译助手",
    page_icon=":rocket:",  # You can use Emoji as the page icon
    layout="wide",  # You can set the layout to "wide" or "centered"
)
st.title("易翻译 | Easy Translation")
st.write("---")
#st.markdown(f"## 【输入的文本中不可以包括符号【/等文件命名不允许的字符】，因为涉及【f+temp+/+my_file_name.mp3文件命名】")
#text = st.text_input("【输入的文本中不可以包括符号【/等文件命名不允许的字符】，因为涉及【f+temp+/+my_file_name.mp3文件命名】")
st.subheader("易翻译 | Easy Translation")

css_file = "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
# Add custom CSS style to center the title
st.markdown(
    """
    <style>
    /* Center the title */
    .title-wrapper {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
elif out_lang == "Korea":
    output_language = "kr"

st.write("---")

# Pre-filled text for the text_input widget
pre_filled_text = "Hi"

# Create the text_input widget with pre-filled text
text = st.text_input("输入需要翻译的内容", value=pre_filled_text)
#text = st.text_input("输入需要翻译的内容（注意：文本中请不要包括/等特殊符号）")

def text_to_speech(input_language, output_language, text):
    if text is None:
#        st.stop()
        print("Input empty.")        
    else:
        translation = translator.translate(text, src=input_language, dest=output_language)
        trans_text = translation.text
        tts = gTTS(trans_text, lang=output_language, slow=False)
        tts.save("translationresult.mp3")
        return trans_text

#def text_to_speech(input_language, output_language, text):
#    translation = translator.translate(text, src=input_language, dest=output_language)
#    trans_text = translation.text
#    tts = gTTS(trans_text, lang=output_language, slow=False)
#    try:
#        my_file_name = text[0:20]
#    except:
#        my_file_name = "audio"
#    tts.save("translationresult.mp3")
#    return trans_text

#if display_output_text = st.checkbox("显示翻译文本（选择后会在语音播放翻译文本的同时显示翻译后的文本）")    
#    st.markdown(f"## 输出的翻译文本（与收听的TTS语音相应）:")
#    st.write(f" {output_text}")

#if st.button("查看翻译结果"):
#    output_text = text_to_speech(input_language, output_language, text)
#    st.write(f" {output_text}")
#    st.write("---")

if text =="" or text.strip().isspace() or text == "" or text.strip() == ""  or text.isspace():
#    st.write("请在上方输入框中输入需要翻译的内容")
#    st.stop()
    print("Input empty.")
else:
    st.write("翻译结果")
    output_text = text_to_speech(input_language, output_language, text)
    st.write(f" {output_text}")

display_output_text = st.checkbox("语音播放翻译结果")    
if display_output_text:
    if text =="" or text.strip().isspace() or text == "" or text.strip() == ""  or text.isspace():
#        st.write("请在上方输入框中输入需要翻译的内容")
#        st.stop()
         print("Input empty.")
    else:
        output_text = text_to_speech(input_language, output_language, text)
        audio_file = open("translationresult.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
#        st.write(f" {output_text}")
 
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
