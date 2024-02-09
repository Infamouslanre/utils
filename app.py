from flask import Flask, render_template, request
from spotify_utils import fetch_new_releases, fetch_new_releases_sorted

app = Flask(__name__)

@app.route('/')
def index():
    # Get the sorting parameter from the URL
    sort_by = request.args.get('sort')

    # Fetch new releases and apply sorting if requested
    if sort_by == 'newest':
        new_releases = fetch_new_releases_sorted()
    else:
        new_releases = fetch_new_releases()

    return render_template('index.html', new_releases=new_releases)

if __name__ == '__main__':
    app.run(debug=True)
