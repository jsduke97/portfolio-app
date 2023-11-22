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
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:5%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<p style="color:white;font-size:18px;line-height:normal;margin-top:30px;">{content2}</p></h1>', 
                unsafe_allow_html = True)
    
def education(school, degrees, grad_date):
    st.markdown("##### " + school)
    st.markdown("🗓️ " + grad_date)
    for d in degrees:
        st.markdown("🎓 " + d)

def skills(skills):
    for text, col in zip(skills, st.columns(len(skills))):
        col.button(text, use_container_width = True)


gradient("#5c4fed", "#341979", "white", "Hi, I'm " + info["Name"], info["About"])

st.divider()

st.markdown("### Projects")

def project(title, link, areas, description, image):
    st.markdown("<h5><a href = \"" + link + "\" target = \"_self\">" + title + "</a></h5>", unsafe_allow_html = True)
    skills(areas)
    st.image(image)
    st.markdown(f'<div id=\"project_description\">{description}</div>', 
                unsafe_allow_html = True)

with st.container():
    c1, c2, c3 = st.columns(3)

with c1:
    title = "ESG Certification Recommender"
    link = "./ESG_Recommendation"
    description = """Built a Python application to recommend sustainability certifications for IT products. The application takes in product data and enriches the dataset with feature definitions from LLaMA and Cohere LLMs. Each product is then assessed by GPT-3.5 and Cohere on compliance with various environmental, social, and governance (ESG) certifications."""
    image = Image.open("./assets/ESG.png")
    project(title, link, ["LLM Generation", "NLP Transformers"], description, image)

with c2:
    title = "Predicting the 2022 FIFA World Cup"
    link = "./FIFA_Predictions"
    description = """Scraped 15,000+ player ratings and 860 national team soccer match statistics from 2015 – 2022 to train five ML classification models up to 70% test accuracy aiming to predict the 2022 FIFA World Cup matches."""
    image = Image.open("./assets/FIFA.png")
    project(title, link, ["ML Classification", "Data Scraping"], description, image)

with c3:
    title = "Meta Ad Impact on 2020 Elections"
    link = "./Meta_Ad_Impact"
    description = """Leveraged the Meta Ad Library API to fit multiple linear regression models, aiming to determine if a 2020 presidential candidate’s Meta ad spend led to an increase in votes."""
    image = Image.open("./assets/META.png")
    project(title, link, ["Multiple Linear Regression"], description, image)

st.divider()

with st.container():
    col1,col2 = st.columns(2)

with col1:
    st.markdown("### Education")
    education("Georgia Institute of Technology", ["Online Master's of Science in Analytics"], "December 2023")
    education("University of North Carolina at Chapel Hill", ["BS Computer Science", "BA Chinese"], "August 2019")

with col2:
    st.markdown("### Technical Skills")
    st.markdown("##### Languages")
    skills(["Python", "SQL", "R"])
    st.markdown("##### Competencies")
    skills(["Natural Language Processing", "Recommender Systems"])
    skills(["ETLs", "Regression", "Machine Learning"])
    skills(["Data Visualization", "Large Language Models"])
