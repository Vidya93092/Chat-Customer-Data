# Chat with Customer Excel Data (AI Tool)

##  Overview
This project is an AI-powered data analyst tool that allows users to upload Excel files and ask questions in natural language.

The system uses:
- Gemini AI
- Pandas
- Streamlit

to analyze customer datasets and generate answers.

##  Features

1. Upload Excel (.xlsx) files  
2. Ask questions in plain English  
3. AI-powered customer data analysis  
4. Natural language query system  
5. Clean Streamlit UI  
6. Save search/query history    

##  Tech Stack

- Python
- Streamlit
- Pandas
- Gemini AI
- OpenPyXL

##  Project Structure

chat_with-customer-data

1. app.py
2. query_engine.py
3. requirements.txt
4. .env
5. README.md
6. test.py

##  Installation

Install required libraries:

pip install -r requirements.txt

##  Run Project

streamlit run app.py

##  Example Questions

- How many customers are from Pune?
- Average customer budget?
- Show high intent customers
- Which city has highest budget?

##  How It Works

1. User uploads Excel file
2. Pandas reads dataset
3. User asks question
4. Dataset + question sent to Gemini AI
5. AI analyzes data
6. Answer displayed in Streamlit UI
7. Search history saved automatically


##  Future Improvements

- Dashboard analytics
- Advanced filters
- Multi-sheet Excel support

##  Developed Using

Python + Streamlit + Gemini AI