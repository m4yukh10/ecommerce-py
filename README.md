
# 🛒 Ecommerce‑Py

A simple e-commerce web application built using Django. It supports user and seller login, product listings, cart functionality, and purchase logic with stock tracking.

---

## 📁 Project Structure

```

ecommerce/
├── db.sqlite3
├── ecom/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
├── manage.py
├── seller/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── user/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── templates/
│   ├── home.html
│   ├── loginbuyer.html
│   ├── registerbuyer.html
│   ├── buy.html

````

---

## ✅ Features

- Custom login system for buyers and sellers
- Product listings by sellers
- Buyer registration and session-based login
- Dynamic product detail page
- Add to cart functionality
- Stock decrements when product is bought

---

## ⚙️ Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/m4yukh10/ecommerce-py.git
cd ecommerce-py
````

2. Set up virtual environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or macOS
source venv/bin/activate
```

3. Install dependencies

```bash
pip install django
```

4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server

```bash
python manage.py runserver
```

---

## 🛍️ Usage

* Visit `http://127.0.0.1:8000/` to view all products.
* Buyer registration and login available at `/user/register` and `/user/login`.
* Seller login at `/seller/login`.
* After login, buyers can add items to their cart by clicking **Buy Me**.
* Cart uses a `ManyToManyField` to track multiple products per buyer.
* Quantity decreases from the product stock on each purchase.

---

## 📦 Models Overview

### `Products` (in seller app)

* `name`
* `type`
* `quantity`

### `Buyer` (in user app)

* `name`
* `age`
* `address`

### `Cart` (in user app)

* Foreign key to `Buyer`
* Many-to-many field for `Products`

---

## 📌 Notes

* Uses Django's built-in session system (no `User` model).
* You should avoid duplicate product names or switch to using `id` or `slug` in production.
* Cart logic is built into the `buy_product` view directly.

---


