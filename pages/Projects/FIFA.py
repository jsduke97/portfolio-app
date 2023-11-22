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
project = fifa_project
project_title = project["Title"]
project_description = project["Description"]
project_image = Image.open(project["image"])
project_image_caption = project["image_caption"]

st.markdown("### " + project_title)

left_co, cent_co,last_co = st.columns([1,10,1])
with cent_co:
    st.image(project_image, caption = project_image_caption, width = 750)

with st.container():
    col1, col2 = st.columns([8,4])

with col1:
    st.markdown(f"<div style=\"text-align: justify;\">{project_description}</div>", unsafe_allow_html = True)

with col2:
    st.link_button("Read the Report", "https://github.com/jsduke97/2022-World-Cup-Prediction/blob/main/2022_World_Cup_Prediction_REPORT.pdf", use_container_width = True)
    st.link_button("View the Poster", "https://github.com/jsduke97/2022-World-Cup-Prediction/blob/main/2022_World_Cup_Prediction_POSTER.pdf", use_container_width = True)
    st.link_button("View the Project Code", "https://github.com/jsduke97/2022-World-Cup-Prediction/blob/main/2022_World_Cup_Prediction_CODE.ipynb", use_container_width = True)