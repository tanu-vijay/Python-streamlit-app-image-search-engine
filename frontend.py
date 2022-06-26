import streamlit as st
from PIL import Image
import requests

st.markdown("<h1 style='text-align: center; color: lightblue;'>The Maple Project</h1>", unsafe_allow_html=True)
st.text('')
st.markdown("<h2 style='text-align: center; color: lightblue;'>Welcome to Our Search Engine :-)</h2>", unsafe_allow_html=True)
st.text('')

image = Image.open('image3.jpg')
st.image(image)

# video_file = open('Video/myvideo.mp4', 'rb')
# video_bytes = video_file.read()
# st.video(video_bytes)

download = st.text_input('Enter Anything to Search')

val=st.button("Submit")

if val:
    site = 'https://www.google.com/search?tbm=isch&q='+download
    getURL = requests.get(site, headers={"User-Agent":"Mozilla/5.0"})
    print(getURL.status_code)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(getURL.text, 'html.parser')
    images = soup.find_all('img')
    imageSources = []
    for image in images:
        imageSources.append(image.get('src'))
    imgList=[]
    for _ in imageSources:
        if 'https' in _:
            imgList.append(_)
    im=[]
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3) 
    with col1:
        im=Image.open(requests.get(imgList[0], stream=True).raw)
        st.image(im, width=200)
    with col2:
        im=Image.open(requests.get(imgList[1], stream=True).raw)
        st.image(im, width=200)
    with col3:
        im=Image.open(requests.get(imgList[2], stream=True).raw)
        st.image(im, width=200)
    with col4:
        im=Image.open(requests.get(imgList[3], stream=True).raw)
        st.image(im, width=200)
    with col5:
        im=Image.open(requests.get(imgList[4], stream=True).raw)
        st.image(im, width=200)
    with col6:
        im=Image.open(requests.get(imgList[5], stream=True).raw)
        st.image(im, width=200)
