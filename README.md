# GreatKart — Django E-Commerce Web Application

GreatKart is a full-stack e-commerce web application built with **Python and Django**. It provides a platform for users to browse product categories, explore products, manage their shopping cart, and interact with an online store through a structured web application.

## 🚀 Features

- **User Authentication** — User registration, login, and account management.
- **Product Catalog** — Browse products organized by categories.
- **Product Variations** — Support for product attributes such as size and color.
- **Shopping Cart** — Add products to the cart and manage cart items.
- **Product Search** — Find products using search functionality.
- **Inventory Availability** — Display product availability, including out-of-stock items.
- **Django ORM** — Manage application data through Django's object-relational mapper.
- **Admin Interface** — Manage application data using Django's administrative capabilities.
- **Responsive Interface** — Browse the store through a web-based user interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework and application logic |
| Django ORM | Database operations |
| SQLite | Development database, if configured |
| HTML and CSS | Page structure and styling |
| JavaScript | Client-side interactions |
| Bootstrap | Responsive UI components, if used by the project |

## 📁 Project Structure

```text
GreatKart/
├── accounts/              # User authentication and accounts
├── carts/                 # Shopping cart functionality
├── category/              # Product categories
├── orders/                # Order-related application module
├── store/                 # Product catalog and store functionality
├── greatkart/              # Main Django project configuration
├── templates/              # HTML templates
├── static/                 # CSS, JavaScript, and static assets
├── media/
│   └── photos/
│       └── products/       # Product images
├── manage.py               # Django management utility
├── requirements.txt        # Python dependencies
├── .env-sample             # Example environment configuration
├── .gitignore              # Git exclusion rules
└── README.md               # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AkshaykumarSanti/GreatKart.git
cd GreatKart
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Review `.env-sample` and create a local `.env` file if the project uses environment variables. Set the required values for your local environment.

**Important:** Never commit actual secret keys, passwords, or other credentials to GitHub.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an administrator account (optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to configure the administrator account.

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

**http://127.0.0.1:8000/**

> Follow any additional project-specific setup steps if your local configuration requires them.

## 🧪 Testing the Application

After starting the server, you can:

1. Register a user account and test login.
2. Browse product categories and product details.
3. Search for products.
4. Test adding products to the shopping cart.
5. Check product availability and variations.
6. Access the Django administration site if an administrator account is configured.

## 🔐 Security Notes

- Keep `.env` and other files containing credentials out of version control.
- Use a secure, unique Django `SECRET_KEY` outside local development.
- Set `DEBUG = False` and configure `ALLOWED_HOSTS` appropriately before deployment.
- Review the database and static/media configuration before deploying the application.

## 🔮 Future Enhancements

Potential improvements include:

- Payment gateway integration.
- Order placement and order history.
- Order tracking and notifications.
- Automated tests for key application features.
- Production deployment and improved security configuration.

## 👨‍💻 Author

**Akshaykumar Santi**

- GitHub: [AkshaykumarSanti](https://github.com/AkshaykumarSanti)
- LinkedIn: [Akshaykumar Santi](https://www.linkedin.com/in/akshaykumar-santi/)

## 📄 License

This project is available for educational and portfolio purposes. Add a formal license file if you intend to specify permissions for reuse and distribution.
