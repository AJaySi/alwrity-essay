import time
import os
import json
import streamlit as st

from ai_essay_writer import ai_essay_generator


def main():
    set_page_config()
    custom_css()
    hide_elements()
    sidebar()
    title_and_description()
    input_section()

def set_page_config():
    st.set_page_config(
        page_title="Alwrity",
        layout="wide",
        page_icon="img/logo.png"
    )

def custom_css():
    st.markdown("""
        <style>
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            [class="st-emotion-cache-7ym5gk ef3psqc12"] {
                display: inline-block;
                padding: 5px 20px;
                background-color: #4681f4;
                color: #FBFFFF;
                width: 300px;
                height: 35px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

def hide_elements():
    hide_decoration_bar_style = '<style>header {visibility: hidden;}</style>'
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    hide_streamlit_footer = '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>'
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

def sidebar():
    st.sidebar.image("img/alwrity.jpeg", use_column_width=True)
    st.sidebar.markdown("🧕 :red[Checkout Alwrity], complete **AI writer & Blogging solution**:[Alwrity](https://alwrity.netlify.app)")


def title_and_description():
    st.title("✍️ Alwrity - AI Essay Writer")
    with st.expander("What is **AI Essay writer** & **How to Use**? 📝❗"):
        st.markdown('''
        Choose the inputs carefully and as per your requirements. Below are the options for the inputs.
        ## Essay Types and Education Levels

		### Essay Types
		- **Argumentative**: Forming an opinion via research. Building an evidence-based argument.
		- **Expository**: Knowledge of a topic. Communicating information clearly.
		- **Narrative**: Creative language use. Presenting a compelling narrative.
		- **Descriptive**: Creative language use. Describing sensory details.
		
		### Education Levels
		- **Primary School**
		- **High School**
		- **College**
		- **Graduate School**
		-----------------------------

		## Inputs and Details
		
		### Essay Type
		Choose the type of essay you want to write from the options provided.
		
		### Education Level
		Select your current level of education from the given choices.
		
		### Essay Title
		Enter the title of your essay. The title should accurately reflect the content and focus of your essay.
		
		### Number of Pages
		Select the length of your essay by choosing one or more options:
		- **Short Form (1-2 pages)**
		- **Medium Form (3-5 pages)**
		- **Long Form (6+ pages)**
            ---
        ''')


def input_section():
    with st.expander("**PRO-TIP** - Choose your inputs carefully", expanded=True):
        col1, space, col2 = st.columns([5, 0.1, 5])
        essay_types = [
            ("Argumentative", "Argumentative - Forming an opinion via research. Building an evidence-based argument."),
            ("Expository", "Expository - Knowledge of a topic. Communicating information clearly."),
            ("Narrative", "Narrative - Creative language use. Presenting a compelling narrative."),
            ("Descriptive", "Descriptive - Creative language use. Describing sensory details.")
        ]

        education_levels = [
            ("Primary School", "Primary School"),
            ("High School", "High School"),
            ("College", "College"),
            ("Graduate School", "Graduate School")
        ]
        with col1:
            # Ask the user for type of essay, level of education, and number of pages
            selected_essay_type = st.selectbox("Choose the type of essay you want to write:", options=[option[0] for option in essay_types])
            selected_education_level = st.selectbox("Choose your level of education:", options=[option[0] for option in education_levels])

        with col2:
            # Ask the user for the title of the essay
            essay_title = st.text_input("Enter the title of your essay:")

            # Ask the user for the number of pages
            num_pages_options = ["Short Form (1-2 pages)", "Medium Form (3-5 pages)", "Long Form (6+ pages)"]
            selected_num_pages = st.selectbox("Select the length of your essay (choose one or more):", options=num_pages_options)


        if st.button('AI, Write Essay'):
            if essay_title.strip():
                with st.spinner("Generating Essay...💥💥"):
                    essay_content = ai_essay_generator(essay_title, selected_essay_type, 
                            selected_education_level, selected_num_pages) 
                    if essay_content:
                        st.subheader('**👩🔬👩🔬 Your Awesome Essay:**')
                        st.markdown(essay_content)
                    else:
                        st.error("💥 **Failed to generate Essay. Please try again!**")
            else:
                st.error("Essay Title is needed, it needs to be 3 words long !")

    page_bottom()


def page_bottom():
    """Display the bottom section of the web app."""

    st.markdown('''
    AI Essay Generator, Powered by AI (Gemini Pro).

    Implemented by [Alwrity](https://alwrity.netlify.app).

    ''')

    st.markdown("""
    ### Free & No Signup. Open Source AI Essay Writer.

    """)

if __name__ == "__main__":
    main()

