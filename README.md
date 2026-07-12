# AI CFO

> AI-powered Financial Intelligence Platform built with Gemini AI.

Transform raw financial statements into executive dashboards, AI-generated summaries, forecasts, recommendations, and interactive business insights.

---

## Executive Dashboard

> Upload a CSV financial statement and instantly receive:

- 📊 Executive Financial Dashboard
- 🤖 AI Executive Summary
- 📈 Financial Forecast
- 💬 AI CFO Chat Assistant
- 📑 Executive Reports
- 🧠 AI Recommendations
- ⚡ Financial Health Score

---

## Features

### AI Financial Analysis

- Executive Summary Generation
- Financial Health Score
- Profit Margin Analysis
- Revenue Analysis
- Expense Breakdown

### Interactive Dashboard

- Animated KPI Cards
- Revenue Charts
- Expense Charts
- Profit Forecast
- AI Insights

### AI CFO Assistant

Powered by **Google Gemini**

Ask questions like:

- Explain my revenue.
- Identify financial risks.
- Suggest growth opportunities.
- Improve profit margin.
- Reduce operating expenses.

### Upload Pipeline

1. Upload CSV
2. Parse Financial Data
3. AI Analysis
4. Dashboard Generation
5. Executive Report

---

# Tech Stack

## Frontend

- Next.js 16
- React 19
- TypeScript
- Tailwind CSS
- Framer Motion
- Zustand
- Recharts

## Backend

- FastAPI
- Python
- Pandas

## AI

- Google Gemini API
- Executive Summary Generation
- AI Financial Chat
- AI Recommendation Engine

---

# Architecture

```text
          CSV Upload
               │
               ▼
        FastAPI Backend
               │
      Financial Processing
               │
               ▼
         Google Gemini
               │
 ┌─────────────┼─────────────┐
 ▼             ▼             ▼
Dashboard   Forecast      AI Chat
```

---

# Installation

## Clone

```bash
git clone https://github.com/Upstart-Union/ai-cfo-web.git

cd ai-cfo-web
```

Install

```bash
npm install

npm run dev
```

Backend

```bash
cd ../ai-cfo-api

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

# Built For

AMD Developer Hackathon Act II

Powered by Google Gemini AI.
Built With Notebook LLM AMD & Digital Ocean