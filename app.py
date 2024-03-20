from flask import Flask, render_template
import requests
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to fetch memes from GitHub-hosted JSON file
def get_memes():
    url = "https://raw.githubusercontent.com/vinghost/Random-memes/master/memes.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
        memes = []
        for post in data['data']['children']:
            if 'url_overridden_by_dest' in post['data']:
                memes.append(post['data']['url_overridden_by_dest'])
        return memes
    except Exception as e:
        logger.error(f"Error fetching memes: {e}")
        return []

# Route to display memes
@app.route('/')
def index():
    try:
        memes = get_memes()
        return render_template('meme.html', memes=memes)
    except Exception as e:
        logger.error(f"Error rendering template: {e}")
        return "An error occurred while fetching memes. Please try again later."

if __name__ == '__main__':
    app.run(debug=True)
