from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def get_ip():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }
    response = requests.get('https://api.ip.sb/geoip', headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return 'Bad request'

@app.route('/')
def index():
    return 'Hello, Dear User Happy Hacking!'

@app.route('/public-ip', methods=['GET'])
def public_ip():
    try:
        public_ip = get_ip()
        with open('public_ip_log.txt', 'a') as f:
            f.write(f"Public IP: {public_ip}\n")
        return jsonify({'public_ip': public_ip})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)