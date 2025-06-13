# ⚖️ LegalAI Pro – Smart Legal Intelligence Suite 🚀

**LegalAI Pro** is a next-gen modular web application designed to assist legal professionals with:

* 🧠 Intelligent legal document analysis
* 🔍 Semantic case search
* 📂 Case classification
* 🧾 Judgment summarization
* ✍️ AI-powered petition generation

Powered by advanced NLP models and a clean **Streamlit** UI, this system transforms unstructured legal data into structured, actionable insights.

---

## 📝 Introduction

The goal of **LegalAI Pro** is to streamline legal document processing using artificial intelligence.
Whether you're searching semantically across case law, extracting critical judgment metadata, or generating petitions based on case summaries — this tool helps you work **smarter, not harder**.

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)
![Streamlit](https://img.shields.io/static/v1?style=for-the-badge\&message=Streamlit\&color=FF4B4B\&logo=Streamlit\&logoColor=FFFFFF\&label=)
![OpenAI API](https://img.shields.io/badge/OpenAI_API-10a37f?style=for-the-badge\&logo=openai\&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-323330?style=for-the-badge\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge\&logo=numpy\&logoColor=white)
![TQDM](https://img.shields.io/badge/TQDM-blue?style=for-the-badge)
![Pillow](https://img.shields.io/badge/Pillow-316192?style=for-the-badge)
![psutil](https://img.shields.io/badge/psutil-FFD43B?style=for-the-badge\&logo=python\&logoColor=black)

---

## ⚙️ Features

### 🔍 1. Smart Case Search

* Enter legal queries
* Perform **semantic + keyword-based** hybrid search
* View and download top-ranked matching cases
---
### 🧠 2. Case Analysis & Petition Generator

* Upload legal case summaries
* AI-based case classification
* Auto-generate formatted **writ petitions** using OpenAI
---
### 🧾 3. Judgement Hub

* Upload full court judgments
* Extract & display:

  * 📌 Case number, date, court, judges
  * ⚖️ Parties, Acts, and Sections involved
* Summarize judgments using LLMs with customizable length
---
### 🤖 4. Legal AI Assistant

* Chat-style assistant powered by OpenAI API
* Ask legal questions or document-related queries
* Securely integrated into the application
---
### 📊 5. Dashboard & Monitoring

* Real-time system statistics
* CPU, memory, and runtime monitoring with `psutil`
* Useful for developers and system administrators
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
└── README.md               # Project documentation
```

---

## 🚀 Quick Start

### 🔧 Method 1: Using the Runner Script

```bash
python run.py
```

### 🛠️ Method 2: Manual Setup

```bash
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
```

---

## 📦 Modules Description

### Core Modules

| File               | Description                              |
| ------------------ | ---------------------------------------- |
| `main.py`          | Main entry point, handles tab navigation |
| `config.py`        | App configuration: API keys, paths       |
| `ai_services.py`   | Handles all AI logic and OpenAI calls    |
| `utils.py`         | Common helper functions                  |
| `ui_components.py` | Custom UI components and styling         |

---

### Tab Modules

| File               | Feature                             |
| ------------------ | ----------------------------------- |
| `search_tab.py`    | Intelligent legal case search       |
| `analysis_tab.py`  | Case analysis + petition generation |
| `judgement_tab.py` | Judgment metadata + summarization   |
| `assistant_tab.py` | Legal chatbot assistant             |
| `dashboard_tab.py` | System metrics and live stats       |

---

## 🔧 Configuration

Customize `config.py` for:

* API keys and service endpoints
* Local file paths and directories
* Model names and parameters
* UI preferences and theme settings

---

## 🛠️ Customization

LegalAI Pro is fully modular:

* Add custom AI tools via `ai_services.py`
* Create new UI tabs in the `tabs/` directory
* Adjust look and feel in `ui_components.py`
* Modify behavior globally in `config.py`

---

## 📝 Notes

* Ensure your **OpenAI API Key** is set in `config.py`
* Use **.txt** files for best AI performance
* Fully backward-compatible with any previous monolithic versions

---

