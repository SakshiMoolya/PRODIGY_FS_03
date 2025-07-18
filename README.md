Flask E-Commerce Website (Text README)
=======================================

Description:
------------
A simple full stack e-commerce website built using Python Flask, SQLite, and Bootstrap.
Users can view products, add them to a cart, remove items, and simulate a checkout
with a randomly estimated delivery date.

Features:
---------
- Product catalog with images, description, and price
- Add to Cart / Remove from Cart functionality
- View total cost in cart
- Checkout form to collect name and address
- Random delivery date (3 to 7 days from current date)
- Purchase success page with delivery estimate
- Responsive UI with Bootstrap 5
- Database: SQLite (lightweight and easy to use)

Project Structure:
------------------
ecommerce-flask/
│
├── app.py              → Main Flask application
├── init_db.py          → Initializes the database and inserts sample products
├── data/
│   └── store.db        → SQLite database
├── static/
│   └── images/         → Product images (tshirt.jpg, jeans.jpg, sneakers.jpg)
├── templates/
│   ├── base.html       → Shared layout
│   ├── home.html       → Welcome / landing page
│   ├── products.html   → Product listing page
│   ├── cart.html       → Shopping cart page
│   ├── checkout.html   → Checkout form for user details
│   └── success.html    → Purchase confirmation and delivery estimate

How to Run:
-----------
1. Make sure Python 3 is installed.
2. (Optional) Create a virtual environment:
   > python -m venv venv
   > venv\Scripts\activate  (on Windows)

3. Install Flask:
   > pip install flask

4. Initialize the database:
   > python init_db.py

5. Run the application:
   > python app.py

6. Open your browser and go to:
   http://localhost:5000

Optional Improvements:
----------------------
- User login & order history
- Admin dashboard for managing products
- Payment integration 
- Product categories, filtering, or search
- Quantity selector in cart

License:
--------
This project is free to use for learning and development purposes.
