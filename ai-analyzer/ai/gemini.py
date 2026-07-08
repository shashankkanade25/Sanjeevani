import os

from dotenv import load_dotenv

import google.generativeai as genai

# =====================================
# Gemini Configuration
# =====================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def analyze_logs(logs):
    """
    Send Kubernetes logs to Gemini and return
    the generated Root Cause Analysis.
    """

    prompt = f"""
You are a Senior Site Reliability Engineer.

Analyze the Kubernetes logs and return ONLY the following fields.

Status:
Severity:
Root Cause:
Impact:
Recommended Fix:
Confidence:

Rules:

- Maximum 1 sentence per field.
- Root Cause should be under 20 words.
- Impact should be under 20 words.
- Confidence should be High, Medium or Low only.
- Recommended Fix should be under 20 words.
- Do not explain.
- Do not repeat information.
- Do not use markdown.
- Return plain text only.

Logs:

{logs}
"""

    response = model.generate_content(prompt)

    return response.text
