"""
Simple Flask application for Jenkins pipeline testing.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    """Welcome/home endpoint."""
    return jsonify({
        'message': 'Welcome to the Flask application',
        'status': 'ok'
    })


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'flask-app'
    }), 200


@app.route('/api/data')
def get_data():
    """Simple API endpoint returning dummy JSON data."""
    return jsonify({
        'data': [
            {'id': 1, 'name': 'Item 1', 'value': 100},
            {'id': 2, 'name': 'Item 2', 'value': 200},
            {'id': 3, 'name': 'Item 3', 'value': 300}
        ],
        'count': 3
    }), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

