from dotenv import load_dotenv
import json
import os

import google.generativeai as genai
from google.api_core.exceptions import (
    ResourceExhausted,
    NotFound,
)

load_dotenv()

api_key = (
    os.getenv("GEMINI_API_KEY")
    or os.getenv("GOOGLE_API_KEY")
)

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set.")

genai.configure(api_key=api_key)

MODELS = [
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
    "gemini-flash-latest",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
]


def generate(prompt: str) -> str:
    last_error = None

    for model_name in MODELS:
        try:
            print(f"Using model: {model_name}")

            model = genai.GenerativeModel(
                model_name
            )

            response = model.generate_content(
                prompt
            )

            return response.text

        except (
            ResourceExhausted,
            NotFound,
        ) as e:
            print(
                f"{model_name} unavailable:"
                f" {e}"
            )
            last_error = e

        except Exception as e:
            print(
                f"{model_name} failed:"
                f" {e}"
            )
            last_error = e

    raise RuntimeError(
        f"All Gemini models failed.\n{last_error}"
    )


def generate_summary(metrics: dict) -> str:
    prompt = f"""
You are an elite Chief Financial Officer (CFO), financial strategist, and senior management consultant with extensive experience advising Fortune 500 executives, startup founders, investors, and board members.

Your reports are written for executive leadership meetings. They are concise, insightful, actionable, and based strictly on the provided financial information.

Financial Metrics
-----------------
Revenue: ₱{metrics['revenue']:,.2f}
Expenses: ₱{metrics['expenses']:,.2f}
Net Profit: ₱{metrics['profit']:,.2f}
Profit Margin: {metrics['profit_margin']:.1f}%

Writing Rules
-------------
- Return ONLY GitHub-Flavored Markdown.
- Maximum 250 words.
- Write naturally and professionally.
- Never mention that you are an AI.
- Never fabricate information.
- Base every conclusion strictly on the provided metrics.
- Explain the business meaning behind the numbers instead of simply repeating them.
- Avoid repetitive wording.
- Vary sentence structure naturally.
- Keep paragraphs concise.
- Use bullet points where appropriate.
- Bold important financial values.
- Do NOT use markdown tables.

Return the report using EXACTLY this structure.

# Executive Summary

Write one concise paragraph summarizing the company's current financial position and outlook.

---

## 📊 Financial Highlights

Explain what the financial metrics indicate about profitability, efficiency, and overall business performance.

---

## 💪 Key Strengths

Provide exactly 3 bullet points.

Each bullet should:
- Describe the observation.
- Explain why it matters.
- Mention the business implication.

---

## ⚠ Risks

Provide exactly 3 realistic business risks.

Do not exaggerate.

Base every risk on the supplied metrics.

---

## 🚀 Strategic Recommendations

Provide exactly 3 numbered recommendations.

Each recommendation must include:

- Action
- Business rationale
- Expected impact

Each recommendation should be 2-3 concise sentences.

---

## 🎯 Overall Assessment

Write one concise executive conclusion.

Finish with:

**Bottom Line:** <one impactful sentence summarizing the company's overall financial condition>.
"""

    return generate(prompt)

def generate_recommendations(metrics: dict) -> list:
    prompt = f"""
You are an elite Chief Financial Officer.

Analyze the following financial metrics.

Revenue: ₱{metrics['revenue']:,.2f}
Expenses: ₱{metrics['expenses']:,.2f}
Net Profit: ₱{metrics['profit']:,.2f}
Profit Margin: {metrics['profit_margin']:.1f}%

Return ONLY valid JSON.

Do not include markdown.

Do not include explanations.

Return EXACTLY this format:

[
  {{
    "title": "Short recommendation title",
    "description": "One concise executive recommendation.",
    "priority": "High"
  }},
  {{
    "title": "...",
    "description": "...",
    "priority": "Medium"
  }},
  {{
    "title": "...",
    "description": "...",
    "priority": "Low"
  }}
]
"""

    response = generate(prompt)

    response = (
        response.replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(response)


def chat(
    message: str,
    dashboard: dict | None,
):
    prompt = f"""
You are an AI CFO.

Financial Dashboard:

{dashboard}

User Question:

{message}

Respond professionally using markdown.
"""

    return generate(prompt)