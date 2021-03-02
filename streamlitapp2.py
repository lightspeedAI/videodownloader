from pytube import YouTube
import streamlit as st
import io
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import time
import base64
option=[]
global downloadop
global success
dicti={}



#Setting the background image of the app
main_bg = "ha.png"
main_bg_ext = "png"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   
    </style>
    """,
    unsafe_allow_html=True
)



#App title
st.markdown("<h1 style='color: white;'>App to check tags used by a Youtube Video</h1>",unsafe_allow_html=True)
st.markdown("<p style='color: white;'>Enter Youtube Video Link Here</p>",unsafe_allow_html=True)


#Input field to enter Youtube Link
videolink = st.text_input('', '')



#Function to find the tags used by the video
def main():
    global videolink
    global option
    
    #checks if link is a youtube link
    if("youtube" in videolink):
        #checks if https:// is used in link
        if("https://" not in videolink):
            videolink="https://"+videolink
        st.markdown("<p style='color: white;'>Loading page, searching for tags</p>",unsafe_allow_html=True)
        #st.write("Loading page, searching for tags")  
        try:
            #loads page
            page = requests.get(videolink)
            #checks if page loaded successfully
            if(int(page.status_code)>=200 and int(page.status_code)<300):
                soup = BeautifulSoup(page.content, 'html5lib')
                tags1 =soup.find_all(attrs={"name": "keywords"})[0]
                attribute = tags1['content']    
                li = list(attribute.split(","))    
                htmlthing=""
                #adding tags into button for better readability
                for l in li:
                    htmlthing=htmlthing+"<a href='https://duckduckgo.com/?q="+l+"&ia=web' target='_blank' class='ptag' style='background-color: #0000FF;  border: none;  color: white;  padding: 15px 32px;  text-align: center;  text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;cursor: pointer;'>"+l+"</a>"
                #prints the tags using html+css
                st.markdown(htmlthing,unsafe_allow_html=True)               
                
            else:
                #in case of proper link, but issue in loading page
                st.markdown("<p style='color: white;'>Page did not load due to an error. Error code"+str(page.status_code)+"</p>",unsafe_allow_html=True)
                
        except:
            #in case link provided doesnt work at all
            st.markdown("<p style='color: white;'>The youtube video link entered either does not exist ,has been removed, or there is a problem with your internet connection.</p>",unsafe_allow_html=True)
            
    else:
        #in case non youtube link was provided
        st.markdown("<p style='color: white;'>Please enter a valid youtube video link</p>",unsafe_allow_html=True)
        




if(videolink!=''):
    #using pytube to load the video     
    yt = YouTube(videolink)
    thumbnail=str(yt.thumbnail_url)
    #thumbnail.replace("default","maxresdefault")
    #putting the video thumbnail as the app background
    htmlelement="<img src='"+thumbnail+"' width=400 height=200 align='center'>"
    st.markdown(htmlelement,unsafe_allow_html=True)
    #background-image: url("paper.gif");
    
    try:
        #creating dictionary to make the drop down list of video qualities more readable
        for stre in list(yt.streams.all()):
            if("144p" in str(stre)):
                if('progressive="False"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="144P 30fps Video Only(No sound)"
                    elif("60fps" in str(stre)):
                        dicti[stre]="144P 60fps Video Only(No sound)"
                elif('progressive="True"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="144P 30fps Video with sound"
                    elif("60fps" in str(stre)):
                        dicti[stre]="144P 60fps Video with sound"
            elif("240p" in str(stre)):
                if('progressive="False"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="240P 30fps Video Only(No sound)"
                    elif("60fps" in str(stre)):
                        dicti[stre]="240P 60fps Video Only(No sound)"
                elif('progressive="True"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="240P 30fps Video with sound"
                    elif("60fps" in str(stre)):
                        dicti[stre]="240P 60fps Video with sound"
            elif("360p" in str(stre)):
                if('progressive="False"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="360P 30fps Video Only(No sound)"
                    elif("60fps" in str(stre)):
                        dicti[stre]="360P 60fps Video Only(No sound)"
                elif('progressive="True"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="360P 30fps Video with sound"
                    elif("60fps" in str(stre)):
                        dicti[stre]="360P 60fps Video with sound"
            elif("480p" in str(stre)):
                if('progressive="False"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="480P 30fps Video Only(No sound)"
                    elif("60fps" in str(stre)):
                        dicti[stre]="480P 60fps Video Only(No sound)"
                elif('progressive="True"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="480P 30fps Video with sound"
                    elif("60fps" in str(stre)):
                        dicti[stre]="480P 60fps Video with sound"
            elif("720p" in str(stre)):
                if('progressive="False"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="720P 30fps Video Only(No sound)"
                    elif("60fps" in str(stre)):
                        dicti[stre]="720P 60fps Video Only(No sound)"
                elif('progressive="True"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="720P 30fps Video with sound"
                    elif("60fps" in str(stre)):
                        dicti[stre]="720P 60fps Video with sound"
            elif("1080p" in str(stre)):
                if('progressive="False"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="1080P 30fps Video Only(No sound)"
                    elif("60fps" in str(stre)):
                        dicti[stre]="1080P 60fps Video Only(No sound)"
                elif('progressive="True"' in str(stre)):
                    if("30fps" in str(stre)):
                        dicti[stre]="1080P 30fps Video with sound"
                    elif("60fps" in str(stre)):
                        dicti[stre]="1080P 60fps Video with sound"
            elif("50kbps" in str(stre)):
                dicti[stre]="50kbps Audio only"
            elif("70kbps" in str(stre)):
                dicti[stre]="70kbps Audio only"
            elif("128kbps" in str(stre)):
                dicti[stre]="128kbps Audio only"
            elif("160kbps" in str(stre)):
                dicti[stre]="160kbps Audio only"
        #Creating the Drop Down List of different video qualities available
        st.markdown("<p style='color: white;'>Select Video Download Quality</p>",unsafe_allow_html=True)
        option=st.selectbox("",(list(dicti.values())), index=0)
        #Storing the Keys and values of the dictionary into two lists(to be used for referencing when downloading video)
        keys=list(dicti.keys())
        values=list(dicti.values())

    except:
        #st.write("The video could not be found. Possible Causes:")
        #st.write("1)Invalid Youtube Video Link")
        #st.write("2)Internet Connection Problem")
        #st.write("3)Video has been removed/does not exist")
        st.markdown("<p style='color: white;'>The video could not be found. Possible Causes:</p>",unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>1)Invalid Youtube Video Link</p>",unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>2)Internet Connection Problem</p>",unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>3)Video has been removed/does not exist</p>",unsafe_allow_html=True)
    #st.write(str(yt.streams.all()))










    #Button to find Tags of selected youtube video
    if st.button('Find Tags'):
        main()






    #Button to download the youtube video in the selected video quality given
    if st.button("Download Video"):
        try:
            keys[values.index(option)].download()
        except:
            st.markdown("<p style='color: white;'>Invalid youtube link, or internet connection problem</p>",unsafe_allow_html=True)
            #st.write("Invalid youtube link, or internet connection problem")


