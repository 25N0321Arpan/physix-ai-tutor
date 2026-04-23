import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def build_prompt(user_prompt, mode):

    if mode == "Concept":
        style = "Explain clearly in simple language with examples."

    elif mode == "Exam":
        style = "Answer in concise IIT JAM/JEST/GATE exam style with key steps."

    elif mode == "Derivation":
        style = "Give full mathematical derivation step-by-step."

    elif mode == "Hint":
        style = "Give only hints and approach, not full answer."

    elif mode == "Viva":
        style = "Act like professor asking viva questions and evaluating."

    else:
        style = "Solve clearly."

    return f"""
You are an expert Physics Tutor.

{style}

Question:
{user_prompt}
"""

def ask_gemini(prompt):

    models = [
        "gemini-2.0-flash",
        "gemini-2.5-flash",
        "gemini-pro-latest"
    ]

    for m in models:
        try:
            model = genai.GenerativeModel(m)
            r = model.generate_content(prompt)
            return r.text
        except:
            continue

    return "AI temporarily unavailable."

def route_prompt(mode, question):
    prompt = build_prompt(question, mode)
    return ask_gemini(prompt)