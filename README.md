# Google Allintitle Checker

This Google Allintitle Checker is a simple Streamlit-based tool that lets SEO professionals and content creators analyze keyword competition by retrieving Google "allintitle" results for specified keywords. It displays the results in a table format and provides a CSV download option for efficient SEO and content planning.

## Features

- Upload a text file with a list of keywords (one keyword per line).
- Automatically searches Google using the `allintitle:` operator for each keyword.
- Displays the number of indexed pages containing each keyword in titles.
- Exports results to a CSV file for further analysis.

## Requirements

- Python 3.7 or higher
- [Streamlit](https://streamlit.io)
- [Pandas](https://pandas.pydata.org/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/google-allintitle-checker.git
    cd google-allintitle-checker
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `keywords.txt` file with your keywords, each on a new line.

## Usage

1. Start the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. In the app:
   - Upload your `keywords.txt` file.
   - View the "allintitle" results displayed in a table.
   - Download the results as a CSV file.
