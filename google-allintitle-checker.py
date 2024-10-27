import re
import requests
import pandas as pd
import streamlit as st
from io import StringIO

# Define user agent
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

# Function to get the exact allintitle result count from Google search
def get_allintitle_count(keyword):
    search_url = f'https://www.google.com/search?q=allintitle%3A{keyword}'
    response = requests.get(search_url, headers=HEADERS)

    if response.status_code == 200:
        # Use regex to find the result count text
        match = re.search(r'About ([\d,]+) results', response.text)
        if match:
            return int(match.group(1).replace(',', ''))
        else:
            return 0  # No results found for the keyword
    else:
        return None  # Unable to connect to Google

# Streamlit app
def main():
    st.title("Google Allintitle Checker")

    # Upload keywords file
    uploaded_file = st.file_uploader("Upload your keywords file (txt)", type="txt")
    
    if uploaded_file:
        # Read keywords from file
        keywords = StringIO(uploaded_file.getvalue().decode("utf-8")).read().splitlines()
        
        # Initialize data structure for results
        results = []

        # Process each keyword
        for keyword in keywords:
            count = get_allintitle_count(keyword)
            results.append({'Keyword': keyword, 'Allintitle Count': count})
        
        # Create DataFrame and display
        df = pd.DataFrame(results)
        st.write(df)
        
        # Download CSV
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download as CSV",
            data=csv,
            file_name="allintitle_results.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
