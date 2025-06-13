"""
Case Analysis Tab Module
"""
import streamlit as st
from ai_services import ai_classify, ai_generate_petition, ai_extract_entities, ai_legal_analysis
from utils import get_document_metrics
from ui_components import render_metrics
from config import LEGAL_CATEGORIES

def render_analysis_tab():
    """Render the Case Analysis tab"""
    st.markdown("""
    <h3 style="text-align: center;">📊 Professional Case Analysis</h3>
    """, unsafe_allow_html=True)

    # File Upload Section
    st.markdown("""
    <div class="pro-card">
        <div class="pro-card-header">📁 Document Upload</div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose a legal document", 
        type=["txt", "pdf", "docx"],
        help="Upload a legal document for comprehensive AI analysis"
    )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    if uploaded_file:
        if uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode("utf-8")
        else:
            content = "File type not fully supported. Please use .txt files for optimal results."
            st.warning("For best AI analysis, please upload .txt files.")
        
        # Document Metrics
        metrics = get_document_metrics(content)
        render_metrics(metrics)
        
        # Document Preview
        st.markdown("### 📄 Document Preview")
        st.text_area("Content", content[:2000] + "..." if len(content) > 2000 else content, height=250, disabled=True)
        
        # Analysis Tools
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🤖 Classify Document", use_container_width=True, type="primary"):
                with st.spinner("🤖 AI is classifying your document..."):
                    classification = ai_classify(content, LEGAL_CATEGORIES)
                
                st.markdown(f"""
                <div class="pro-card" style="
                    background: linear-gradient(145deg, #ffffff, #f1f3f5);
                    border: 1px solid #dee2e6;
                    border-radius: 10px;
                    padding: 1.5rem;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
                    transition: all 0.3s ease;
                ">
                    <div style="
                        font-size: 1.2rem;
                        font-weight: 700;
                        color: #1a365d;
                        margin-bottom: 1rem;
                        border-bottom: 2px solid #e9ecef;
                        padding-bottom: 0.5rem;
                    ">
                        🎯 Classification Result
                    </div>
                    <div style="
                        color: #495057;
                        font-size: 1rem;
                        line-height: 1.6;
                    ">
                        {classification}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            if st.button("✍️ Generate Petition", use_container_width=True):
                with st.spinner("🤖 AI is drafting your petition..."):
                    entities = ai_extract_entities(content)
                    petition = ai_generate_petition(content, entities)
                
                st.code(petition, language="text")
                
                st.download_button(
                    label="💾 Download Petition",
                    data=petition,
                    file_name="ai_generated_petition.txt",
                    mime="text/plain",
                    use_container_width=True
                )
        
        # Comprehensive Analysis
        if st.button("🧠 Comprehensive AI Analysis", use_container_width=True, type="primary"):
            with st.spinner("🤖 AI is performing comprehensive analysis..."):
                analysis = ai_legal_analysis(content)
            
            st.markdown(f"""
            <div class="pro-card">
                <div class="pro-card-header">🧠 Legal Analysis Report</div>
                <div class="result-content">{analysis}</div>
            </div>
            """, unsafe_allow_html=True)
