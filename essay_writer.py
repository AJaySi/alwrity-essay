import time
import os
import json
import streamlit as st

from ai_essay_writer import ai_essay_generator


def main():
    set_page_config()
    custom_css()
    hide_elements()
    title_and_description()
    input_section()

def set_page_config():
    st.set_page_config(
        page_title="Alwrity",
        layout="wide",
    )

def custom_css():
    st.markdown("""
        <style>
        ::-webkit-scrollbar-track {
        background: #e1ebf9;
        }

        ::-webkit-scrollbar-thumb {
            background-color: #90CAF9;
            border-radius: 10px;
            border: 3px solid #e1ebf9;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #64B5F6;
        }

        ::-webkit-scrollbar {
            width: 16px;
        }
        div.stButton > button:first-child {
            background: #1565C0;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

def hide_elements():
    hide_decoration_bar_style = '<style>header {visibility: hidden;}</style>'
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    hide_streamlit_footer = '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>'
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)


def title_and_description():
    st.title("✍️ Alwrity - AI Essay Writer")


def input_section():
    with st.expander("**💡 PRO-TIP** - Choose your inputs carefully", expanded=True):
        col1, space, col2 = st.columns([5, 0.1, 5])
        
        # Enhanced options with explanations
        essay_types = [
            ("Argumentative", "Forming an opinion via research. Building an evidence-based argument."),
            ("Expository", "Knowledge of a topic. Communicating information clearly."),
            ("Narrative", "Creative language use. Presenting a compelling narrative."),
            ("Descriptive", "Creative language use. Describing sensory details.")
        ]

        education_levels = [
            ("Primary School", "Basic understanding, simple language."),
            ("High School", "Moderate complexity, clear arguments."),
            ("College", "Advanced complexity, detailed analysis."),
            ("Graduate School", "High complexity, critical thinking.")
        ]
        
        with col1:
            # Type of essay with descriptions
            selected_essay_type = st.selectbox(
                "📘 **Choose the type of essay you want to write**", 
                options=[option[0] for option in essay_types],
                format_func=lambda option: f"{option} - {dict(essay_types)[option]}"
            )
            
            # Education level with descriptions
            selected_education_level = st.selectbox(
                "🎓 **Choose your level of education**", 
                options=[option[0] for option in education_levels],
                format_func=lambda option: f"{option} - {dict(education_levels)[option]}"
            )

        with col2:
            # Title of the essay with example
            essay_title = st.text_input(
                "📝 **Enter the title of your essay**", 
                placeholder="e.g., The Impact of Climate Change on Marine Life"
            )

            # Number of pages with descriptions
            num_pages_options = [
                "📄 Short Form (1-2 pages)", 
                "📑 Medium Form (3-5 pages)", 
                "📚 Long Form (6+ pages)"
            ]
            selected_num_pages = st.selectbox(
                "📏 **Select the length of your essay** (choose one or more):", 
                options=num_pages_options
            )
            
        st.markdown("**✨ Customize your essay settings to fit your needs. Happy writing!**")

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



if __name__ == "__main__":
    main()

