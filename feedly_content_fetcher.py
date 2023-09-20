import requests
import json
import sqlite3

# Your Feedly user ID and access token
user_id = '6bda7e9d-c3fd-4b80-ab38-403a02a8b06d'
access_token = 'A-GCTZQ7wBsmQvqB8wormk9OcoNXH6Pc0kjGoHvAWh6xm1q9y15ZW1rBCdJEShJUgiNigs09jgIMUoiiAWna-5uGuSCO4OKOE__OP_zlt-tI7_5VGQhZ2sMKhuotL8Q2wh0ylRmmUFhvsRBe1zhAU9liovZCftXD8APXTpc3m-TMjZLPvrwdZs3qHkbQFQLyoRAZREDzyXkdpjStYYB8ePSJLbfurKAf5Uy_-DnFdsP9OhAZbPz6JhzE1-5X_g:feedlydev'


# Function to get user profile
def get_user_profile(access_token):
    url = 'https://cloud.feedly.com/v3/profile'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers)
    return response.json()


# Function to get category IDs
def get_categories(access_token):
    url = 'https://cloud.feedly.com/v3/categories'
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers)
    return response.json()


# Fetch and print categories
categories = get_categories(access_token)
for category in categories:
    print(f"Label: {category['label']}")
    print(f"ID: {category['id']}")
    print("\n")

# ID of your "AI Everything" category
folder_id = 'user/6bda7e9d-c3fd-4b80-ab38-403a02a8b06d/category/5c66c388-4fc3-4268-808a-522715b1f762'

# Define the URL for the Feedly API endpoint
url = f"https://cloud.feedly.com/v3/streams/contents?streamId={folder_id}"

# Define the headers for the API request
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Send the GET request to the Feedly API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = json.loads(response.text)

    # Print the articles
    for item in data['items']:
        print(f"Title: {item['title']}")
        print(f"URL: {item['originId']}")
        print("\n")
else:
    print(f"Failed to fetch data from Feedly API: {response.text}")


# to save articles into a database and query
def store_articles_in_db():
    # Connect to the SQLite database
    conn = sqlite3.connect('ai_everything.db')

    # Create a cursor object
    c = conn.cursor()

    # Create table
    c.execute('''
        CREATE TABLE IF NOT EXISTS articles
        (title text, url text)
    ''')

    # Save (commit) the changes
    conn.commit()

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)

        # Store the articles in the database
        for item in data['items']:
            # Check if the article is already in the database
            c.execute("SELECT * FROM articles WHERE url = ?", (item['originId'],))
            if c.fetchone() is None:
                # If the article is not in the database, insert it
                c.execute("INSERT INTO articles VALUES (?, ?)", (item['title'], item['originId']))

        # Save (commit) the changes
        conn.commit()
    else:
        print(f"Failed to fetch data from Feedly API: {response.text}")

    # Close the database connection
    conn.close()


def get_articles_from_db():
    # Connect to the SQLite database
    conn = sqlite3.connect('ai_everything.db')

    # Create a cursor object
    c = conn.cursor()

    # Get all articles
    c.execute("SELECT * FROM articles")

    # Fetch all rows from the last executed SQL command
    articles = c.fetchall()

    # Print the articles
    for article in articles:
        print(f"Title: {article[0]}")
        print(f"URL: {article[1]}")
        print("\n")

    # Close the database connection
    conn.close()

# Call the functions
store_articles_in_db()

# TIME FOR CONTENT PROCESSING
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download the NLTK English stopwords and the Punkt Tokenizer Models
nltk.download('punkt')
nltk.download('stopwords')

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Assume we have the following article content
article_content = "This is an example of article content. It talks about AI and Machine Learning."

# Tokenize the article content
tokens = word_tokenize(article_content)

# Remove stopwords
tokens = [token for token in tokens if token not in stopwords.words('english')]

# Perform stemming
tokens = [stemmer.stem(token) for token in tokens]

# Now 'tokens' is a list of words from the article content, with stopwords removed and words stemmed
print(tokens)



