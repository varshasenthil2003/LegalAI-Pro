"""
UI Components and Styling for LegalAI Pro
"""
import streamlit as st

def load_custom_css():
    """Load custom CSS styling"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;900&family=Roboto+Condensed:wght@300;400;700&display=swap');
        
        /* Global Professional Corporate Styling */
        .stApp {
            background: #f8f9fa;
            font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            color: #212529;
            line-height: 1.6;
        }
        
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {visibility: hidden;}
        
        /* Professional Header */
        .corporate-header {
            background: linear-gradient(135deg, #1a365d 0%, #2c5282 100%);
            color: white;
            padding: 2rem 0;
            margin: -1rem -1rem 2rem -1rem;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }
        
        .main-title {
            font-family: 'Roboto Condensed', sans-serif;
            font-size: 2.8rem;
            font-weight: 700;
            margin: 0;
            letter-spacing: -0.02em;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        .subtitle {
            font-size: 1.1rem;
            margin: 0.5rem 0 0 0;
            opacity: 0.9;
            font-weight: 400;
        }
        
        /* Professional Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #2c5282 0%, #1a365d 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 6px !important;
            padding: 0.75rem 1.5rem !important;
            font-family: 'Roboto', sans-serif !important;
            font-weight: 500 !important;
            font-size: 0.9rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 2px 8px rgba(44, 82, 130, 0.3) !important;
            width: 100% !important;
            min-height: 2.8rem !important;
            text-transform: none !important;
            letter-spacing: 0.01em !important;
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, #1a365d 0%, #2c5282 100%) !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 12px rgba(44, 82, 130, 0.4) !important;
        }
        
        /* Professional Cards */
        .pro-card {
            background: white;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }
        
        .pro-card:hover {
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }
        
        .pro-card-header {
            font-size: 1.2rem;
            font-weight: 600;
            color: #1a365d;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #e9ecef;
        }
        
        /* Professional Metrics */
        .metric-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 1.5rem 0;
        }
        
        .metric-card {
            background: white;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        
        .metric-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #1a365d;
            margin-bottom: 0.5rem;
            font-family: 'Roboto Condensed', sans-serif;
        }
        
        .metric-label {
            color: #6c757d;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 500;
        }
        
        /* Professional Results */
        .result-item {
            background: white;
            border: 1px solid #e9ecef;
            border-left: 4px solid #2c5282;
            border-radius: 8px;
            padding: 1.5rem;
            margin: 1rem 0;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        
        .result-item:hover {
            transform: translateX(4px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        }
        
        .result-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            flex-wrap: wrap;
            gap: 1rem;
        }
        
        .result-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #1a365d;
            margin: 0;
        }
        
        .result-score {
            background: linear-gradient(135deg, #28a745, #20c997);
            color: white;
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
        }
        
        .result-content {
            color: #495057;
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        
        .result-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 1rem;
            border-top: 1px solid #e9ecef;
            font-size: 0.85rem;
            color: #6c757d;
        }
        
        /* Chat Interface Styling */
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
        
        /* Disabled textarea styling */
        section textarea[disabled] {
            color: #212529 !important;
            background-color: #f8f9fa !important;
            font-weight: 500 !important;
            border: 1px solid #dee2e6 !important;
            border-radius: 6px !important;
            padding: 0.75rem !important;
        }
        
        textarea[disabled] {
            color: #212529 !important;
            background-color: #f8f9fa !important;
            font-weight: 500 !important;
            -webkit-text-fill-color: #212529 !important;
            opacity: 1 !important;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .result-header {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .metric-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """, unsafe_allow_html=True)

def render_header():
    """Render the professional header"""
    st.markdown("""
    <div class="corporate-header">
        <div class="main-title">⚖️ LegalAI Pro</div>
        <div class="subtitle">Advanced Legal Intelligence & Document Processing Platform</div>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Render the professional footer"""
    st.markdown("""
    <div style="margin-top: 3rem; padding: 2rem; text-align: center; background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #e9ecef;">
        <h4 style="color: #1a365d; margin-bottom: 1rem; font-family: 'Roboto Condensed', sans-serif;">⚖️ LegalAI Pro</h4>
        <p style="color: #6c757d; margin-bottom: 0.5rem;">Professional Legal Intelligence Platform</p>
        <p style="color: #495057; font-size: 0.9rem;">Advanced AI • Professional Results • Secure Processing</p>
    </div>
    """, unsafe_allow_html=True)

def render_metrics(metrics):
    """Render metrics in a grid layout"""
    st.markdown(f"""
    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-value">{metrics['word_count']:,}</div>
            <div class="metric-label">Words</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">{metrics['paragraph_count']}</div>
            <div class="metric-label">Paragraphs</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">{metrics['estimated_time']}</div>
            <div class="metric-label">Min Read</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_search_result(summary, score, index):
    """Render a single search result"""
    st.markdown(f"""
    <div class="result-item">
        <div class="result-header">
            <h4 class="result-title">📄 Case {index}</h4>
            <div class="result-score">🎯 {score}% Match</div>
        </div>
        <div class="result-content">{summary[:400]}...</div>
        <div class="result-footer">
            <span>🤖 AI Analyzed</span>
            <span>Relevance: {score}%</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
