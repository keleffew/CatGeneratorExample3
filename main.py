from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-cat')
def get_cat():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    cat_url = data[0]['url']
    return jsonify({'cat_url': cat_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)