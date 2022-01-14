# flask_web/app.py

from flask import Flask
from sentiment-analysis import sentiment_analysis

app = Flask(__name__)

@app.route('/')
def hello_world():
    phrase = request.data
    return sentiment_analysis(phrase)

    # return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
