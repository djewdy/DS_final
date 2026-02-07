#!/usr/bin/env python3
"""
Simple Web Services Dashboard - Flask Web Interface
A clean web app that connects to multiple free public APIs
"""

from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/weather')
def get_weather():
    """Get weather data"""
    city = request.args.get('city', 'London')
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            return jsonify({
                'success': True,
                'city': city,
                'temp': current['temp_C'],
                'desc': current['weatherDesc'][0]['value'],
                'humidity': current['humidity'],
                'wind': current['windspeedKmph']
            })
    except:
        pass
    return jsonify({'success': False, 'error': 'Could not fetch weather'})

@app.route('/api/quote')
def get_quote():
    """Get inspirational quote"""
    try:
        url = "https://api.quotable.io/random?minLength=30"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                'success': True,
                'quote': data['content'],
                'author': data['author']
            })
    except:
        pass
    return jsonify({'success': False, 'error': 'Could not fetch quote'})

@app.route('/api/fact')
def get_fact():
    """Get random fact"""
    try:
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                'success': True,
                'fact': data['text']
            })
    except:
        pass
    return jsonify({'success': False, 'error': 'Could not fetch fact'})

@app.route('/api/crypto')
def get_crypto():
    """Get crypto price"""
    crypto = request.args.get('crypto', 'bitcoin')
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd&include_24hr_change=true"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if crypto in data:
                price_data = data[crypto]
                return jsonify({
                    'success': True,
                    'crypto': crypto,
                    'price': price_data['usd'],
                    'change': price_data.get('usd_24h_change', 0)
                })
    except:
        pass
    return jsonify({'success': False, 'error': 'Could not fetch crypto data'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
