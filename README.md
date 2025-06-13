# ⚖️ LegalAI Pro – Smart Legal Intelligence Suite 🚀

LegalAI Pro is a next-gen modular web application designed to assist legal professionals with intelligent legal document analysis, semantic case search, case classification, judgment summarization, and AI-powered petition generation. 
Powered by advanced NLP models and a clean Streamlit UI, this system transforms unstructured legal data into structured, actionable insights.

---

## 📝 Introduction

The goal of **LegalAI Pro** is to streamline legal document processing using artificial intelligence. 
Whether you're searching semantically across case law, extracting critical judgment metadata, or generating petitions based on case summaries — this tool helps you work smarter, not harder.

---

## 🛠️ Technologies Used

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Streamlit](https://img.shields.io/static/v1?style=for-the-badge&message=Streamlit&color=FF4B4B&logo=Streamlit&logoColor=FFFFFF&label=)
- ![OpenAI API](https://img.shields.io/badge/OpenAI_API-10a37f?style=for-the-badge&logo=openai&logoColor=white)
- ![FAISS](https://img.shields.io/badge/FAISS-323330?style=for-the-badge&logoColor=white)
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
- ![NumPy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
- ![TQDM](https://img.shields.io/badge/TQDM-blue?style=for-the-badge)
- ![Pillow](https://img.shields.io/badge/Pillow-316192?style=for-the-badge)
- ![psutil](https://img.shields.io/badge/psutil-FFD43B?style=for-the-badge&logo=python&logoColor=black)

---

## ⚙️ Features

### 🔍 1. **Smart Case Search**
- Type legal queries
- Perform **semantic + keyword-based** hybrid search
- View and download top-ranked matching cases

### 🧠 2. **Case Analysis & Petition Generator**
- Upload legal case summaries
- AI-based classification 
- Automatically generate formatted writ petitions using OpenAI

### 🧾 3. **Judgement Hub**
- Upload full court judgments
- Extract and display:
  - 📌 Case number, date, court, judges
  - ⚖️ Parties, acts, sections involved
- Summarize using LLMs with user-selectable length

### 🤖 4. **Legal AI Assistant**
- Chat-style AI assistant powered by **OpenAI API**
- Query legal topics, ask document-related questions
- Integrated securely in-app

### 📊 5. **Dashboard & Monitoring**
- Real-time stats and resource metrics using `psutil`
- System health insights for developers/admins

---

## 🏗️ Directory Structure

```bash
legal-ai-pro/
├── main.py                 # Main Streamlit app
├── run.py                  # Quick runner script
├── config.py               # Config: API keys, paths, settings
├── ai_services.py          # All AI logic and model functions
├── utils.py                # Common utilities and helpers
├── ui_components.py        # Styling and UI elements

├── tabs/                   # Modular tabs for each feature
│   ├── search_tab.py       # Semantic Search
│   ├── analysis_tab.py     # Case Analysis + Petition Gen
│   ├── judgement_tab.py    # Judgment Hub
│   ├── assistant_tab.py    # AI Assistant
│   └── dashboard_tab.py    # Dashboard

├── requirements.txt        # All dependencies
└── README.md               # This file
```
## 🚀 Quick Start

### Method 1: Using the Runner Script
\`\`\`bash
python run.py
\`\`\`

### Method 2: Manual Setup
# Clone the project
git clone https://github.com/yourusername/legalai-pro.git
cd legalai-pro

# Create virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Download NLP models
python -m spacy download en_core_web_sm

# Launch the app
streamlit run main.py


## 📦 Modules Description

### Core Modules
- **`main.py`**: Application entry point with tab navigation
- **`config.py`**: Centralized configuration management
- **`ai_services.py`**: All AI-related functionality
- **`utils.py`**: Helper functions and data processing
- **`ui_components.py`**: UI styling and reusable components

### Tab Modules
- **`search_tab.py`**: Intelligent legal case search
- **`analysis_tab.py`**: Document analysis and classification
- **`judgement_tab.py`**: Judgement document processing
- **`assistant_tab.py`**: AI chat assistant
- **`dashboard_tab.py`**: System monitoring and tools

## 🔧 Configuration
Edit `config.py` to customize:
- API keys and endpoints
- File paths
- Model configurations
- UI settings

## 🛠️ Customization
Each module can be independently modified:
- Add new AI models in `ai_services.py`
- Create new tabs in the `tabs/` directory
- Modify styling in `ui_components.py`
- Update configurations in `config.py`

## 📝 Notes
- Ensure your API keys are properly configured in `config.py`
- The application supports .txt files for optimal AI analysis
- All functionality from the original monolithic version is preserved
