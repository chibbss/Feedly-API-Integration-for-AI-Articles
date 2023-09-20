# Feedly-API-Integration-for-AI-Articles

This project is aimed at fetching and processing AI-related articles using the Feedly API. It involves tasks such as API interaction, data storage in an SQLite database, and natural language processing (NLP) techniques.

# Table of Contents
  - Overview
  - Features
  - Prerequisites
  - Installation
  - Usage
  - Functions
  - Content Processing
  - Contributing
  - Licensing

# Overview
This project interacts with the Feedly API to fetch articles related to Artificial Intelligence. It then processes the content, removing stopwords and performing stemming using the NLTK library. The processed content can be used for various NLP tasks.

# Features
  - interact with the Feedly API to fetch articles.
  - Store articles in an SQLite database for later retrieval.
  - Process article content by removing stopwords and performing stemming.

# Prerequisites
  - python installed on your local machine
  - ```
    pip install requests nltk
    ```
    
# Installation

  - Clone the repository to your local machine.
  - Install the required libraries (if not already installed)

# Usage
  - Obtain a Feedly user ID and access token.
  - Replace the user_id and access_token variables in main.py with your own credentials.
  - ```
    python feedly_content_fetcher.py
    ```

# Functions
  - get_user_profile(access_token) - Retrieves the user profile using the provided access token.
  - get_categories(access_token) - Retrieves the categories from the Feedly API using the provided access token.
  - store_articles_in_db() - Stores fetched articles in an SQLite database.
  - get_articles_from_db() - Retrieves and prints articles from the SQLite database.
  - create_box_plot(data, x_col, color_col, title, color_map=None) - Creates and displays a box plot using Plotly Express.

# Content Processing
The content processing involves the following steps:
  - Tokenization of the article content.
  - Removal of stopwords using NLTK's predefined list.
  - Stemming of the remaining words using the Porter Stemmer.

# Contributing
Pull requests and contributions are welcome. For major changes, please open an issue first to discuss what you would like to change.

# License
MIT License


    
