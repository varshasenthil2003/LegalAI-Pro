"""
AI Assistant Tab Module
"""
import streamlit as st
from datetime import datetime
from ai_services import call_ai_api
from utils import export_chat_history

def render_assistant_tab():
    """Render the AI Assistant tab"""
    st.markdown("""
    <style>
    .main-heading {
        text-align: center;
        color: #1e3a8a;
        font-size: 28px;
        font-weight: bold;
        margin: 10px 0 30px;
    }
    .chat-container {
        background-color: #f8fafc;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 30px;
    }
    .stChatMessage div, 
    .stChatMessage p, 
    .stChatMessage span, 
    .stChatMessage h1, 
    .stChatMessage h2, 
    .stChatMessage h3, 
    .stChatMessage li, 
    .stChatMessage a,
    .stChatMessage strong,
    .stChatMessage em,
    .stChatMessage code {
        color: #0f172a !important;
        font-weight: 500 !important;
    }
    .stChatMessage[data-testid="stChatMessage"] {
        color: #0f172a !important;
    }
    .stChatMessage [data-testid="stMarkdownContainer"] * {
        color: #0f172a !important;
    }
    .stChatMessage [data-testid="stChatMessageContent"] {
        background-color: #f1f5f9;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    <div class="main-heading">🤖 Professional AI Legal Assistant</div>
    """, unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown('<p style="color: #334155; font-size: 20px; font-weight: 600;">💬 Legal Consultation Chat</p>', unsafe_allow_html=True)
        with col2:
            if st.button("📤 Export Chat", use_container_width=True):
                chat_data = export_chat_history()
                st.download_button(
                    label="💾 Download",
                    data=chat_data,
                    file_name=f"legal_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True,
                    key="download_chat"
                )

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your AI legal assistant. I can help you with legal research, document analysis, case summaries, and legal drafting. How can I assist you today?"}
        ]

    # Chat Interface
    with st.container():
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                if message["role"] == "assistant":
                    html_content = f"""
                    <div style="color: #0f172a !important; font-weight: 500 !important;">
                        {message["content"]}
                    </div>
                    """
                    st.markdown(html_content, unsafe_allow_html=True)
                else:
                    st.markdown(f'<div style="color: #334155 !important;">{message["content"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if prompt := st.chat_input("Ask me anything about legal matters..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(f'<div style="color: #334155 !important;">{prompt}</div>', unsafe_allow_html=True)

        with st.chat_message("assistant"):
            with st.spinner("AI is thinking..."):
                messages = [
                    {"role": "system", "content": "You are an expert legal AI assistant. Provide helpful, accurate, and professional legal guidance. Always remind users to consult with qualified legal professionals for specific legal advice."}
                ]
                for msg in st.session_state.messages[-5:]:
                    messages.append({"role": msg["role"], "content": msg["content"]})

                response = call_ai_api(messages, max_tokens=2000)
                html_response = f"""
                <div style="color: #0f172a !important; font-weight: 500 !important;">
                    {response}
                </div>
                """
                st.markdown(html_response, unsafe_allow_html=True)

        st.session_state.messages.append({"role": "assistant", "content": response})

    # Quick Actions
    st.markdown('<p style="color: #1e3a8a; font-size: 22px; font-weight: 600; margin-top: 40px;">⚡ Quick Actions</p>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    quick_actions = [
        ("📋 Research Tips", "Provide 5 essential tips for effective legal research"),
        ("⚖️ Case Analysis", "Explain how to effectively analyze case law"),
        ("📝 Drafting Guide", "Provide guidelines for drafting legal documents"),
        ("🔄 Clear Chat", None)
    ]
    
    for i, (col, (button_text, prompt)) in enumerate(zip([col1, col2, col3, col4], quick_actions)):
        with col:
            if st.button(button_text, use_container_width=True):
                if prompt:
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    with st.spinner("Getting response..."):
                        response = call_ai_api([
                            {"role": "system", "content": "You are a legal expert. Provide practical advice."},
                            {"role": "user", "content": prompt}
                        ])
                        st.session_state.messages.append({"role": "assistant", "content": response})
                else:
                    st.session_state.messages = [
                        {"role": "assistant", "content": "Chat cleared! Ready for new questions."}
                    ]
                st.rerun()
