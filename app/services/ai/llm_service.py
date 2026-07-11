from dotenv import load_dotenv
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
You are an experienced Chief Financial Officer.

Financial Metrics

Revenue: {metrics['revenue']}
Expenses: {metrics['expenses']}
Profit: {metrics['profit']}
Profit Margin: {metrics['profit_margin']}%

Generate a professional executive summary.

Use markdown.

Include:

## Executive Summary

## Financial Health

## Risks

## Recommendations
"""

    return generate(prompt)


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