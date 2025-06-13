"""
Configuration settings for LegalAI Pro
"""
import os

#im using openrouter model
# API Configuration
OPENAI_CONFIG = {
    "base_url": "https://openrouter.ai/api/v1",
    "api_key": "<ur-api-key>",
}

# Directory Configuration
SUMMARY_DIR = " summary directory in the local drive"

# App Configuration
APP_CONFIG = {
    "page_title": "LegalAI Pro - Advanced Legal Intelligence",
    "page_icon": "⚖️",
    "layout": "wide",
    "initial_sidebar_state": "collapsed"
}

# AI Model Configuration
AI_MODELS = {
    "default": "deepseek/deepseek-chat-v3-0324:free",
    "classification": "deepseek/deepseek-chat-v3-0324:free",
    "summarization": "deepseek/deepseek-chat-v3-0324:free",
    "analysis": "deepseek/deepseek-chat-v3-0324:free"
}

# Default Categories for Classification
LEGAL_CATEGORIES = [
    "Criminal case", "Civil dispute", "Constitutional petition", 
    "Corporate law", "Family law", "Property dispute", 
    "Labor law", "Tax law", "Contract dispute"
]
