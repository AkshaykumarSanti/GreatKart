# GreatKart – Django E-Commerce Web Application

GreatKart is a Django-based e-commerce web application that provides essential online shopping features, including user authentication, product and category management, product search, product variations, and shopping cart functionality.

## 🚀 Features

- **User Authentication:** User registration and login using email and password.
- **Product Management:** Manage products and categories through the Django Admin panel.
- **Product Catalog:** Display products with images, details, and availability status.
- **Product Variations:** Support for different product sizes and colors.
- **Shopping Cart:** Add and remove products and manage cart items.
- **Dynamic Cart Summary:** Display cart item count and calculate the total price dynamically.
- **Variation-Based Cart Items:** Group identical product variations and maintain different variation combinations as separate cart items.
- **Product Search:** Search for products using keywords.
- **Pagination:** Display products across multiple pages for easier navigation.
- **Responsive UI:** Bootstrap-based interface with navigation and footer sections.
- **Out-of-Stock Handling:** Indicate product availability to users.

## 🛠️ Technologies Used

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap
- **Tools:** Git, GitHub, VS Code

## 📂 Project Modules

- **Accounts:** Handles user registration, login, and authentication.
- **Category:** Manages product categories.
- **Store:** Handles product details, product listings, search, and pagination.
- **Cart:** Manages cart items, product variations, quantities, and pricing.

## 📈 Development Progress

### Day 01 – Project Setup and UI Structure
- Initialized the Django project and established the initial UI structure.
- Integrated a Bootstrap template.
- Created the navigation bar and footer.
- Set up the basic HTML and CSS layout.

### Day 02 – Authentication and Category Module
- Created the `accounts` application for user management.
- Implemented email-and-password-based authentication.
- Created the `category` application for product categorization.
- Configured project settings, URL routing, and database migrations.

### Day 03 – Store Module Setup
- Created and configured the `store` application.
- Set up media configuration for product images.
- Updated URL routing for the store module.
- Prepared models, views, and admin configuration for product management.

### Day 04 – Category and Product Management
- Implemented category and product management.
- Created product models and product details.
- Established relationships between products and categories.
- Configured Django Admin for managing products and categories.

### Day 05 – Product Display Enhancements
- Implemented out-of-stock product handling.
- Made product images and names clickable.
- Added navigation to individual product detail pages.
- Improved product browsing functionality.

### Day 06 – Shopping Cart Implementation
- Implemented shopping cart functionality.
- Displayed selected products in the cart.
- Calculated the total cart price dynamically.
- Added a cart item count and summary.

### Day 07 – Add to Cart Functionality
- Added a shopping cart icon to the navigation bar.
- Implemented the Add to Cart feature.
- Enabled users to add products to the cart.
- Updated the cart item count dynamically.

### Day 08 – Search and Pagination
- Implemented keyword-based product search.
- Added pagination to product listings.
- Improved product discovery and catalog navigation.

### Day 09 – Product Variations and Cart Improvements
- Added size and color variations to products.
- Displayed available variations on product detail pages.
- Stored selected variations in cart items.
- Grouped identical product variations and updated their quantities.
- Maintained separate cart items for different variation combinations.
- Displayed selected sizes and colors in the cart.
- Updated cart add/remove functionality to support product variations.

### Day 10 – Login and Registration UI
- Created user login and registration pages.
- Designed responsive authentication forms using Bootstrap.
- Integrated authentication pages with the project layout.
- Improved navigation between login and registration pages.
- Prepared the authentication interface for backend integration.

## ⚙️ Installation and Setup

### Prerequisites
- Python 3.x
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/AkshaykumarSanti/GreatKart.git
```

### 2. Navigate to the Project Directory

```bash
cd GreatKart
```

### 3. Create and Activate a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install django
```

If a `requirements.txt` file is available, install the project dependencies using:

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser at:

`http://127.0.0.1:8000/`

Access the Django Admin panel at:

`http://127.0.0.1:8000/admin/`

## 🎯 Learning Outcomes

This project provides practical experience with:

- Django project structure and application development.
- Model creation and database relationships using Django ORM.
- User authentication and URL routing.
- Product catalog and category management.
- Shopping cart logic and product variation handling.
- Search, pagination, and dynamic price calculations.
- Integrating Bootstrap templates with Django.

## 🔮 Future Enhancements

- Implement order placement and order history.
- Integrate a payment gateway.
- Add product reviews and ratings.
- Add automated tests for core functionality.
- Improve deployment and production configuration.

## 👨‍💻 Author

**Akshaykumar Santi**

- GitHub: [AkshaykumarSanti](https://github.com/AkshaykumarSanti)
- LinkedIn: [Akshaykumar Santi](https://www.linkedin.com/in/akshaykumar-santi/)

---

*Developed as a Django e-commerce project to practice backend development and core online shopping functionality.*
