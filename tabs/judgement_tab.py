"""
Judgement Hub Tab Module
"""
import streamlit as st
import json
import re
from ai_services import ai_summarize, ai_extract_entities, ai_legal_analysis
from utils import get_document_metrics, format_entity_value
from ui_components import render_metrics

def render_judgement_tab():
    """Render the Judgement Hub tab"""
    st.markdown("""
    <h3 style="text-align: center;">⚖️ Professional Judgement Analysis</h3>
    """, unsafe_allow_html=True)

    # File Upload
    st.markdown("""
    <div class="pro-card">
        <div class="pro-card-header">📁 Judgement Document Upload</div>
    """, unsafe_allow_html=True)

    judgement_file = st.file_uploader(
        "Choose a Judgement Document",
        type=["txt", "pdf", "docx"],
        help="Upload a complete Judgement document for comprehensive analysis"
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if judgement_file:
        if judgement_file.type == "text/plain":
            judgement_text = judgement_file.read().decode("utf-8")
        else:
            judgement_text = "File type not fully supported. Please use .txt files for optimal results."
            st.warning("For best AI analysis, please upload .txt files.")

        metrics = get_document_metrics(judgement_text)
        render_metrics(metrics)
        
        # Custom CSS for disabled textarea
        st.markdown("""
        <style>
        section textarea[disabled] {
            color: #212529 !important;
            background-color: #f8f9fa !important;
            font-weight: 500 !important;
            border: 1px solid #dee2e6 !important;
            border-radius: 6px !important;
            padding: 0.75rem !important;
        }
        </style>
        """, unsafe_allow_html=True)

        # Document Preview
        st.markdown("### 📄 Judgement Preview")
        st.text_area(
            "Content",
            judgement_text[:3000] + "..." if len(judgement_text) > 3000 else judgement_text,
            height=300,
            disabled=True
        )
        
        col1, col2 = st.columns(2)

        # Initialize session states
        if "show_summary_options" not in st.session_state:
            st.session_state.show_summary_options = False
        if "analysis_output" not in st.session_state:
            st.session_state.analysis_output = ""
        if "show_entity_output" not in st.session_state:
            st.session_state.show_entity_output = False
            st.session_state.extracted_entities = {}
            
        with col1:
            # AI Summarization
            if st.button("📝 AI Summarization", key="summary_header", use_container_width=True):
                st.session_state.show_summary_options = not st.session_state.show_summary_options

            if st.session_state.show_summary_options:
                with st.container():
                    st.markdown("""
                    <div style="background-color: #f1f5fb; padding: 1rem; border-radius: 8px; margin-top: 0.5rem;">
                        <strong>Choose Summary Type:</strong>
                    </div>
                    """, unsafe_allow_html=True)

                    summary_type = st.select_slider(
                        "Summary Type",
                        options=["brief", "standard", "detailed"],
                        value="standard"
                    )

                    if st.button("🤖 Generate Summary", key="generate_summary", use_container_width=True):
                        with st.spinner("AI is creating your summary..."):
                            summary = ai_summarize(judgement_text, summary_type)
                        summary_html = re.sub(r"\*(.*?)\*", r"<b>\1</b>", summary)
                        summary_html = summary_html.replace('\n', '<br>')
                        st.markdown(f"""
                        <div class="pro-card">
                            <div class="pro-card-header">📋 AI Summary ({summary_type.title()})</div>
                            <div class="result-content">
                                {summary_html}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        st.download_button(
                            label="💾 Download Summary",
                            data=summary,
                            file_name=f"judgement_summary_{summary_type}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )

        with col2:
            # Entity Extraction
            if st.button("🔍 Entity Extraction", key="entity_toggle", use_container_width=True):
                with st.spinner("AI is extracting key information..."):
                    st.session_state.extracted_entities = ai_extract_entities(judgement_text)
                    st.session_state.show_entity_output = True

            if st.session_state.show_entity_output and st.session_state.extracted_entities:
                entities = st.session_state.extracted_entities
                
                if isinstance(entities, dict) and "error" not in entities:
                    st.markdown("""
                    <div style="background: linear-gradient(to right, #e3f2fd, #bbdefb); padding: 1rem 1.5rem; border-radius: 10px; color: #0d47a1; font-weight: bold; font-size: 1rem; margin-top: 1rem; border: 1px solid #90caf9;">
                        <div style="font-size: 1.1rem; margin-bottom: 0.5rem;">📋 Key Legal Information</div>
                    """, unsafe_allow_html=True)

                    for key, value in entities.items():
                        st.markdown(f"""
                        <div style="margin-bottom: 0.7rem; background: #ffffff; padding: 0.7rem 1rem; border-radius: 8px; border: 1px solid #e0e0e0;">
                            <div style="color: #1565c0; font-weight: 600; font-size: 0.95rem;">{key.replace('_', ' ').title()}</div>
                            <div style="color: #424242; font-size: 0.9rem;">{format_entity_value(value)}</div>
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.error(entities.get("error", "Unexpected error during entity extraction."))
                    
                st.download_button(
                    label="💾 Download Data",
                    data=json.dumps(entities, indent=2),
                    file_name="extracted_entities.json",
                    mime="application/json",
                    use_container_width=True
                )
        
        # Comprehensive Analysis
        if st.button("🧠 Comprehensive AI Analysis", use_container_width=True, type="primary"):
            with st.spinner("🤖 AI is performing comprehensive analysis..."):
                st.session_state.analysis_output = ai_legal_analysis(judgement_text)
            
        if st.session_state.analysis_output:
            st.markdown(f"""
            <div class="pro-card">
                <div class="pro-card-header">🧠 Legal Analysis Report</div>
                <div class="result-content">{st.session_state.analysis_output}</div>
            </div>
            """, unsafe_allow_html=True)
