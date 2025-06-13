"""
Utility functions for LegalAI Pro
"""
import os
import re
import streamlit as st
from datetime import datetime
from config import SUMMARY_DIR

@st.cache_data
def load_summaries(path):
    """Load legal case summaries from directory"""
    summaries = []
    if os.path.exists(path):
        for filename in os.listdir(path):
            if filename.endswith(".txt"):
                try:
                    with open(os.path.join(path, filename), 'r', encoding='utf-8') as f:
                        summaries.append(f.read())
                except Exception as e:
                    st.warning(f"Could not read {filename}: {e}")
    else:
        summaries = [
            "Sample Case 1: Property dispute between landlord and tenant regarding lease agreement violations...",
            "Sample Case 2: Criminal appeal challenging conviction under Section 302 IPC for murder charges...",
            "Sample Case 3: Constitutional petition challenging validity of government notification...",
            "Sample Case 4: Civil suit for recovery of money and damages in breach of contract case...",
            "Sample Case 5: Family court matter regarding custody of minor children in divorce proceedings..."
        ]
    return summaries

def parse_ai_search_results(search_response, original_docs):
    """Parse AI search results and return structured data"""
    try:
        results = []
        lines = search_response.split('\n')
        
        for line in lines:
            if 'Doc' in line and '%' in line:
                match = re.search(r'Doc (\d+).*?(\d+)%', line)
                if match:
                    doc_num = int(match.group(1)) - 1
                    score = int(match.group(2))
                    if 0 <= doc_num < len(original_docs):
                        results.append((original_docs[doc_num], score))
        
        if not results:
            for i, doc in enumerate(original_docs[:5]):
                results.append((doc, 85 - i*5))
                
        return results[:5]
        
    except Exception as e:
        return [(doc, 80 - i*10) for i, doc in enumerate(original_docs[:5])]

def export_chat_history():
    """Export chat history to text format"""
    if "messages" in st.session_state and st.session_state.messages:
        chat_export = f"LegalAI Pro Chat Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        chat_export += "=" * 60 + "\n\n"
        
        for i, message in enumerate(st.session_state.messages, 1):
            role = "🤖 AI Assistant" if message["role"] == "assistant" else "👤 User"
            chat_export += f"{role} (Message {i}):\n"
            chat_export += f"{message['content']}\n\n"
            chat_export += "-" * 40 + "\n\n"
        
        return chat_export
    return "No chat history available."

def format_entity_value(value):
    """Format entity values for display"""
    if isinstance(value, list):
        return "<ul style='margin-top: 0.3rem;'>" + "".join(f"<li>{v}</li>" for v in value) + "</ul>"
    elif isinstance(value, dict):
        return "<ul style='margin-top: 0.3rem;'>" + "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in value.items()) + "</ul>"
    else:
        return f"{value}"

def get_document_metrics(content):
    """Calculate document metrics"""
    word_count = len(content.split())
    paragraph_count = len([p for p in content.split('\n\n') if p.strip()])
    estimated_time = max(1, word_count // 1000)
    
    return {
        "word_count": word_count,
        "paragraph_count": paragraph_count,
        "estimated_time": estimated_time
    }
