#!/usr/bin/env python3
"""Flask application"""

import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_data(filename='products.json'):
    """Read data"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def read_csv_data(filename='products.csv'):
    """Read data"""
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            products = []
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
            return products
    except FileNotFoundError:
        return None


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

@app.route('/products')
def products():
    """Render the products page"""
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products_data = read_json_data()
    else:
        products_data = read_csv_data()

    if products_data is None:
        return render_template('product_display.html', error="File not found")

    if product_id is not None:
        products_data = [p for p in products_data if p['id'] == product_id]
        if not products_data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
