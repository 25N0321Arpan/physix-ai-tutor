import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# -------------------------
# Physics Prompt Builder
# -------------------------
def physics_prompt(user_prompt):
    return f"""
You are an expert Physics Tutor for JAM, JEST, GATE, MSc and university students.

Rules:
1. Solve step-by-step.
2. Use equations clearly.
3. Explain concepts simply.
4. If numerical, show final answer.
5. If unsure, say so honestly.
6. Format cleanly.

Question:
{user_prompt}
"""


# -------------------------
# Run Gemini Model
# -------------------------
def run_gemini(prompt, model_name):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text


# -------------------------
# Smart Gemini Router
# -------------------------
def route_prompt(mode, user_prompt):

    prompt = physics_prompt(user_prompt)

    # Pro mode
    if mode == "Gemini Pro":
        try:
            return run_gemini(prompt, "gemini-3.1-pro-preview")
        except Exception:
            pass

    # Try models in order
    models = [
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-3-flash-preview",
        "gemini-pro-latest"
    ]

    for model_name in models:
        try:
            return run_gemini(prompt, model_name)
        except Exception:
            continue

    return """
All Gemini models are temporarily unavailable or quota exhausted.

Please try again later.
"""
