import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use stable model
model = genai.GenerativeModel("gemini-3.1-flash-lite")

def process_query(df, query):

    df.columns = df.columns.str.strip()

    query_lower = query.lower()

    #  BASIC PANDAS HANDLING (more accurate)

    if "average" in query_lower and "budget" in df.columns:
        return f"Average Budget = {df['Budget'].mean()}"

    if "how many" in query_lower:
        return f"Total Rows = {len(df)}"

    if "pune" in query_lower and "City" in df.columns:
        count = df[df["City"].str.lower() == "pune"].shape[0]
        return f"Customers in Pune = {count}"

    #  AI fallback (ONLY sample data)
    data_context = f"""
COLUMNS:
{list(df.columns)}

SAMPLE DATA:
{df.to_string(index=False)}
"""

    prompt = f"""
You are a data analyst AI.

Dataset:
{data_context}

User Question:
{query}

Rules:
- Use only given sample data
- If calculation needed, explain logically
- Return clean answer
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"