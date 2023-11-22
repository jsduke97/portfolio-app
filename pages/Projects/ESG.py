#######Imports and header########
import streamlit as st
from bio import *
from PIL import Image
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

st.set_page_config(page_title = "Jackson S Duke - Data Scientist", layout = "wide", page_icon = "👨🏻‍💼💻")
#################################

#######Sidebar########
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

show_pages(
    [
        Page("1_Home.py", "Home", icon = ":house:"),
        Page("pages/Projects/ESG.py", "ESG_Recommendation", icon = ":recycle:"),
        Page("pages/Projects/FIFA.py", "FIFA_Predictions", icon = ":soccer:"),
        Page("pages/Projects/META.py", "Meta_Ad_Impact", icon = ":us:"),
    ]
)

st.sidebar.markdown(info["Photo"], unsafe_allow_html = True)

st.sidebar.markdown(info["Sidebar Name"], unsafe_allow_html = True)

st.sidebar.markdown(info["Sidebar About"], unsafe_allow_html = True)

with st.sidebar:
    with open("./assets/Jackson_S_Duke_Resume_2023.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    resume = st.download_button(
        label = "Download Resume",
        data = PDFbyte,
        file_name = "Jackson_S_Duke_Resume_2023.pdf",
        mime = "application/pdf",
        use_container_width = True
    )
######################

########Page Content########
project = esg_project
project_title = project["Title"]
project_description = project["Description"]
project_image = Image.open(project["image"])
project_image_caption = project["image_caption"]

st.markdown("### " + project_title)

left_co, cent_co,last_co = st.columns([2,6,2])
with cent_co:
    st.image(project_image, caption = project_image_caption, width = 500)

with st.container():
    col1, col2 = st.columns([8,4])

with col1:
    st.markdown(f"<div style=\"text-align: justify;\">{project_description}</div>", unsafe_allow_html = True)

with col2:
    st.link_button("Try the Demo", project["demo_link"], use_container_width = True)
    st.link_button("Read the Report", "", use_container_width = True, disabled = True)
    st.link_button("View the Presentation", "", use_container_width = True, disabled = True)

with st.container():
    v1_col1, v1_col2 = st.columns([4, 10])

with v1_col1:
    st.markdown(project["video1_desc"])

with v1_col2:
    st.video(project["video1_link"]) 

with st.container():
    v2_col1, v2_col2 = st.columns([4, 10])

with v2_col1:
    st.markdown(project["video2_desc"])
    
with v2_col2:
    st.video(project["video2_link"]) 