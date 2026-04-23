import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# -------------------------
# Physics Prompt Builder
# -------------------------
def physics_prompt(user_prompt):
    return f"""
You are an expert Physics Tutor for JAM, JEST, GATE, MSc students.

Rules:
1. Solve step-by-step.
2. Use equations clearly.
3. Explain simply.
4. Give final answer.
5. If unsure, say so.

Question:
{user_prompt}
"""


# -------------------------
# Gemini Single Call
# -------------------------
def run_gemini(prompt, model_name):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text


# -------------------------
# Ollama Fallback
# -------------------------
def run_ollama(prompt, model="qwen3.5:4b"):
    import ollama

    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


# -------------------------
# Smart Router
# -------------------------
def route_prompt(mode, user_prompt):

    prompt = physics_prompt(user_prompt)

    # Manual Ollama mode
    if mode == "Ollama":
        return run_ollama(prompt)

    # Manual Gemini Pro
    if mode == "Gemini Pro":
        try:
            return run_gemini(prompt, "gemini-3.1-pro-preview")
        except:
            return run_ollama(prompt)

    # Smart Auto Mode
    models = [
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-3-flash-preview",
        "gemini-3-pro-preview"
    ]

    for m in models:
        try:
            return run_gemini(prompt, m)
        except Exception:
            continue

    # Final fallback
    return run_ollama(prompt)