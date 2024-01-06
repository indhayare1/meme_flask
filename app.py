from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    try:
        response = requests.get('https://api.quotable.io/random')
        response.raise_for_status()  # Raises HTTPError if response code is not successful
        quotes_data = response.json()
        quotes = quotes_data['content']

        author = quotes_data['author']
        taariikhda = quotes_data['dateAdded']
        numberkisa = quotes_data['length']
        #famous = quotes_data['Epictetus']
        return render_template('index.html', quotes = quotes , author = author, taariikhda = taariikhda, numberkisa = numberkisa)
    except requests.RequestException as e:
        # If an error occurs during the request, render the error template
        return render_template('error.html', error=str(e))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error='Page Not Found'), 404

if __name__ == '__main__':
    app.run(debug=True)
