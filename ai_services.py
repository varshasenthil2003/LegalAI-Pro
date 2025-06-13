"""
AI Services Module for LegalAI Pro
Handles all AI-related functionality including summarization, classification, and analysis
"""
import json
import re
from openai import OpenAI
from config import OPENAI_CONFIG, AI_MODELS

# Initialize OpenAI client
client = OpenAI(
    base_url=OPENAI_CONFIG["base_url"],
    api_key=OPENAI_CONFIG["api_key"]
)

def call_ai_api(messages, model=None, max_tokens=2000, temperature=0.7):
    """Generic function to call AI API"""
    if model is None:
        model = AI_MODELS["default"]
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"API Error: {str(e)}"

def ai_summarize(text, length="standard"):
    """Summarize text using AI"""
    length_instructions = {
        "brief": "Provide a very brief summary in 2-3 sentences.",
        "standard": "Provide a comprehensive summary in 4-6 sentences.",
        "detailed": "Provide a detailed summary covering all key points in 8-10 sentences."
    }
    
    messages = [
        {"role": "system", "content": f"You are a legal expert. {length_instructions.get(length, length_instructions['standard'])} Focus on key legal points, parties involved, and main outcomes."},
        {"role": "user", "content": f"Summarize this legal document:\n\n{text[:4000]}"}
    ]
    
    return call_ai_api(messages, model=AI_MODELS["summarization"], max_tokens=1000)

def ai_classify(text, categories):
    """Classify text using AI"""
    categories_str = ", ".join(categories)
    
    messages = [
        {"role": "system", "content": f"You are a legal document classifier. Classify the given text into one of these categories: {categories_str}. Respond with only the category name and confidence percentage."},
        {"role": "user", "content": f"Classify this legal document:\n\n{text[:2000]}"}
    ]
    
    return call_ai_api(messages, model=AI_MODELS["classification"], max_tokens=200, temperature=0.3)

def ai_extract_entities(text):
    """Extract legal entities using AI"""
    messages = [
        {"role": "system", "content": "You are a legal document analyzer. Extract key information from legal documents including: case name, petitioner, respondent, court, judges, case number, date, and legal sections. Format as JSON."},
        {"role": "user", "content": f"Extract key legal entities from this document:\n\n{text[:3000]}"}
    ]

    response = call_ai_api(messages, max_tokens=1500)

    # Use regex to extract JSON content
    try:
        json_str_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_str_match:
            return json.loads(json_str_match.group())
        else:
            return {"error": "Could not find JSON object in response."}
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON. Please ensure AI output is valid JSON."}

def ai_generate_petition(case_summary, extracted_info):
    """Generate legal petition using AI"""
    messages = [
        {"role": "user", "content": f"Generate a writ petition based on this case summary: {case_summary[:2000]}\n\nExtracted information: {extracted_info}"}
    ]
    
    return call_ai_api(messages, max_tokens=3000)

def ai_semantic_search(query, documents, top_k):
    """Perform semantic search using AI"""
    messages = [
        {"role": "system", "content": f"You are a legal research assistant. Given a query and a list of legal documents, rank the top {top_k} most relevant documents. Provide the ranking with relevance scores (0-100) and brief explanations."},
        {"role": "user", "content": f"Query: {query}\n\nDocuments: {documents[:5000]}"}
    ]
    
    return call_ai_api(messages, max_tokens=2000)

def ai_legal_analysis(text):
    """Comprehensive legal analysis using AI"""
    messages = [
        {"role": "system", "content": "You are a senior legal analyst. Provide a comprehensive analysis of the legal document including key legal issues, precedents, arguments, and potential outcomes. Focus on analysis and insights."},
        {"role": "user", "content": f"Analyze this legal document:\n\n{text[:4000]}"}
    ]
    
    return call_ai_api(messages, model=AI_MODELS["analysis"], max_tokens=2500)
