"""
Dashboard Tab Module
"""
import streamlit as st
import psutil
from datetime import datetime
from ai_services import call_ai_api

def render_dashboard_tab():
    """Render the Dashboard tab"""
    st.markdown("""
    <style>
    .stAlert > div {
        color: #0f172a !important;
        font-weight: 500 !important;
    }
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 20px;
        margin: 20px 0;
    }
    .metric-card {
        background-color: #f1f5f9;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #e2e8f0;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #1e293b;
    }
    .metric-label {
        font-size: 14px;
        color: #64748b;
        margin-top: 5px;
    }
    .pro-card {
        background-color: #f8fafc;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        margin-bottom: 30px;
    }
    .pro-card-header {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 10px;
        color: #1e3a8a;
    }
    .result-content p {
        color: #0f172a;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h3 style="text-align: center;">📊 Professional Dashboard</h3>
    """, unsafe_allow_html=True)
    
    # System Status
    memory_usage = psutil.virtual_memory().percent
    cpu_usage = psutil.cpu_percent()
    
    st.markdown(f"""
    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-value">{memory_usage:.1f}%</div>
            <div class="metric-label">Memory Usage</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">{cpu_usage:.1f}%</div>
            <div class="metric-label">CPU Usage</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">Active</div>
            <div class="metric-label">AI Status</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">{datetime.now().strftime('%H:%M')}</div>
            <div class="metric-label">Current Time</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # System Overview
    st.markdown("""
    <div class="pro-card">
        <div class="pro-card-header">📊 System Overview</div>
        <div class="result-content">
            <p>✅ AI services are running optimally</p>
            <p>📁 Document processing ready</p>
            <p>🔍 Search functionality active</p>
            <p>💬 Chat assistant available</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Tools
    st.markdown("### 🔧 Quick Tools")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Refresh System", use_container_width=True):
            st.cache_data.clear()
            st.success("✅ System refreshed successfully!")
    
    with col2:
        if st.button("🧪 Test AI", use_container_width=True):
            with st.spinner("Testing AI connection..."):
                test_result = call_ai_api([{"role": "user", "content": "Test connection"}], max_tokens=10)
                if "Error" not in test_result:
                    st.success("✅ AI is working perfectly!")
                else:
                    st.error(f"❌ AI Issue: {test_result}")
    
    with col3:
        if st.button("📋 System Info", use_container_width=True):
            st.info("🚀 LegalAI Pro v2.0 - Professional Edition")
