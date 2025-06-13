"""
Smart Search Tab Module
"""
import streamlit as st
from ai_services import ai_semantic_search
from utils import load_summaries, parse_ai_search_results
from ui_components import render_search_result
from config import SUMMARY_DIR

def render_search_tab():
    """Render the Smart Search tab"""
    st.markdown("""
    <style>
    section[data-testid="stExpander"] textarea[disabled] {
        color: #0f172a !important;
        background-color: #ffffff !important;
        font-weight: 600 !important;
        opacity: 1 !important;
        border: 1px solid #cbd5e1 !important;
    }
    section[data-testid="stExpander"] .stTextArea textarea {
        font-size: 15px !important;
        line-height: 1.5 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3 style="text-align: center;">🔍 Intelligent Legal Case Search</h3>
    """, unsafe_allow_html=True)
      
    # Search Input + Button
    col1, col2 = st.columns([4, 1])
    with col1:
        query = st.text_input(
            "Enter your legal query", 
            placeholder="e.g., Property dispute between landlord and tenant involving lease violations",
            key="search_query"
        )
    
    with col2:
        st.write("")  # spacing
        search_clicked = st.button("🚀 Search", use_container_width=True)

    num_results = 5
    
    # Handle Search Logic
    if search_clicked and query:
        with st.spinner("🤖 AI is analyzing your query..."):
            summaries = load_summaries(SUMMARY_DIR)
            search_response = ai_semantic_search(query, summaries, num_results)
            results = parse_ai_search_results(search_response, summaries)

        st.markdown("### 📋 Search Results")
        
        # Results
        for i, (summary, score) in enumerate(results, 1):
            render_search_result(summary, score, i)
            
            # Collapsible Full Content
            with st.expander(f"📖 View Full Case {i}"):
                st.text_area(f"Complete Case Summary", summary, height=300, disabled=True)
                
                st.download_button(
                    label=f"💾 Download Case {i}",
                    data=summary,
                    file_name=f"case_{i}_summary.txt",
                    mime="text/plain",
                    key=f"download_case_{i}",
                    use_container_width=True
                )
