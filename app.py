import streamlit as st
import pandas as pd
from query_engine import process_query

# Initialize history
if "history" not in st.session_state:
    st.session_state.history = []

# Page settings
st.set_page_config(page_title="AI Excel Analyst")

# Title
st.title("📊 Chat with Customer Excel Data")

# Upload file
file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if file:

    # Read Excel
    df = pd.read_excel(file)

    st.success("✅ Excel file uploaded successfully")

    # Ask question
    query = st.text_input(
        "Ask question about your data"
    )

    if query:

        with st.spinner("Analyzing Data..."):

            result = process_query(df, query)

        # Save history
        st.session_state.history.append({
            "question": query,
            "answer": result
        })

        st.subheader("Answer")
        st.write(result)

#  Show history
if st.session_state.history:

    st.subheader("📜 Search History")

    for item in st.session_state.history:

        st.write("❓", item["question"])
        st.write("✅", item["answer"])
        st.write("---")

