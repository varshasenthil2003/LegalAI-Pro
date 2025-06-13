"""
Main Application File for LegalAI Pro
Modular version with organized structure
"""
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

# Import modules
from config import APP_CONFIG
from ui_components import load_custom_css, render_header, render_footer
from tabs.search_tab import render_search_tab
from tabs.analysis_tab import render_analysis_tab
from tabs.judgement_tab import render_judgement_tab
from tabs.assistant_tab import render_assistant_tab
from tabs.dashboard_tab import render_dashboard_tab

def main():
    """Main application function"""
    # Page Configuration
    st.set_page_config(**APP_CONFIG)
    
    # Load Custom CSS
    load_custom_css()
    
    # Render Header
    render_header()
    
    # Initialize session state
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "search"

    # Tab Navigation
    def set_active_tab(tab):
        st.session_state.active_tab = tab

    # Tab buttons
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("🔍 Smart Search"):
            set_active_tab("search")
    with col2:
        if st.button("📊 Case Analysis"):
            set_active_tab("analysis")
    with col3:
        if st.button("⚖️ Judgement Hub"):
            set_active_tab("judgement")
    with col4:
        if st.button("🤖 AI Assistant"):
            set_active_tab("assistant")
    with col5:
        if st.button("📈 Dashboard"):
            set_active_tab("dashboard")

    # Render active tab
    if st.session_state.active_tab == "search":
        render_search_tab()
    elif st.session_state.active_tab == "analysis":
        render_analysis_tab()
    elif st.session_state.active_tab == "judgement":
        render_judgement_tab()
    elif st.session_state.active_tab == "assistant":
        render_assistant_tab()
    elif st.session_state.active_tab == "dashboard":
        render_dashboard_tab()
    
    # Render Footer
    render_footer()

if __name__ == "__main__":
    main()
