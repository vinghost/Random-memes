from flask import Flask, render_template
import requests

app = Flask(__name__)

# Function to fetch memes using the requests library
def get_memes():
    url = "https://www.reddit.com/r/memes.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    data = response.json()
    memes = []
    for post in data['data']['children']:
        if 'url_overridden_by_dest' in post['data']:
            memes.append(post['data']['url_overridden_by_dest'])
    return memes

# Route to display memes
@app.route('/')
def index():
    memes = get_memes()
    return render_template('meme.html', memes=memes)

if __name__ == '__main__':
    app.run(debug=True)
