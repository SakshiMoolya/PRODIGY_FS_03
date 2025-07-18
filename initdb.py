import sqlite3
import os

os.makedirs('data', exist_ok=True)

conn = sqlite3.connect('data/store.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL,
    image TEXT
)
''')

cursor.execute('DELETE FROM products')  # Clear table before inserting

products = [
    ('T-Shirt', '100% cotton t-shirt', 499.00, 'tshirt.jpg'),
    ('Jeans', 'Comfort fit blue jeans', 899.00, 'jeans.jpg'),
    ('Sneakers', 'Stylish sneakers', 1299.00, 'sneakers.jpg'),
    ('Top', 'Rayon top for womens', 399.00, 'Top womens.jpeg'),
    ('Linen Pant', '100% pure cotton pant', 1850.00, 'Women pant.jpeg'),
    ('Heels', 'Stylish heels', 1500.00, 'Women heels.jpeg')
]

cursor.executemany('''
INSERT INTO products (name, description, price, image)
VALUES (?, ?, ?, ?)
''', products)

conn.commit()
conn.close()

print("Database created and populated successfully ✅")
