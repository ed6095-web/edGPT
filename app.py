import os
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Secure API Key Storage
API_KEY = os.getenv('sk-c1483f69ae2c4527b056f83dc0d3e9bf')
API_URL = API_URL = API_URL = 'https://api.deepseek.com/v1/chat/completions'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'reply': 'No message provided'}), 400

    try:
        response = requests.post(
            API_URL,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {sk-c1483f69ae2c4527b056f83dc0d3e9bf}'
            },
            json={
                "model": "deepseek-chat",  # Ensure this is the correct model name
                "messages": [{"role": "user", "content": user_message}]
            }
        )

        if response.status_code != 200:
            return jsonify({'reply': f'Error: {response.status_code} {response.text}'}), response.status_code

        data = response.json()
        return jsonify({'reply': data.get('choices', [{}])[0].get('message', {}).get('content', 'No reply from AI')})
    except Exception as e:
        return jsonify({'reply': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Production-ready settings
