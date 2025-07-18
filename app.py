from flask import Flask, render_template, redirect, url_for, request, session
import sqlite3
from datetime import datetime, timedelta
import random

app = Flask(__name__)
app.secret_key = 'secret123'

def get_db_connection():
    conn = sqlite3.connect('data/store.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('products.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    session['cart'] = session.get('cart', [])
    session['cart'].append(product_id)
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    conn = get_db_connection()
    cart_items = []
    total = 0
    if 'cart' in session:
        for pid in session['cart']:
            product = conn.execute('SELECT * FROM products WHERE id = ?', (pid,)).fetchone()
            if product:
                cart_items.append(product)
                total += product['price']
    conn.close()
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' in session:
        session['cart'] = [pid for pid in session['cart'] if pid != product_id]
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']

        # Simulate random delivery between 3 to 7 days from now
        delivery_days = random.randint(3, 7)
        delivery_date = datetime.now() + timedelta(days=delivery_days)

        # Clear the cart
        session.pop('cart', None)

        return render_template('success.html', name=name, delivery_date=delivery_date.strftime('%d %B %Y'))

    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
