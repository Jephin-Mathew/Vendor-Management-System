# Vendor Management System

## Requirements

- **Python Version:** 3.11
- **Database:** MySQL

## Installation

1. Install virtualenvwrapper-win:

```bash
pip3 install virtualenvwrapper-win
```

2. Create a new virtual environment:

   ```bash
   mkvirtualenv your_project_env
   ```

3. Activate the virtual environment:

   ```bash
   workon your_project_env
   ```

4. Install Django inside the virtual environment:

   ```bash
   pip3 install django
   ```

5. Install project dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

## Database Setup

1. **Create a MySQL Database:**

   ```bash
   # Log in to MySQL with your credentials

   # Create a new database
   ```

2. **Update Django Settings:**

   Update the `DATABASES` configuration in your Django project's `settings.py` file with your MySQL database credentials.

## Database Migrations

To create and apply database migrations:

1. Apply migrations to create the database arrangements:

   ```bash
   python manage.py migrate
   ```

## Run server

Run the development server:

```bash
   python manage.py runserver
```

## Authorization Token

An authorization token is required for authentication.

The authorization header should contain the following:

```bash
Token a74336a3ea0b76239abd630e2bda5142d7f12972
```

## API Endpoints

- **Create a Vendor**

  - Endpoint: `http://127.0.0.1:8000/vendor/create/`

- **List Vendors**

  - Endpoint: `http://127.0.0.1:8000/vendor/`

- **Get Details of a Specific Vendor**

  - Endpoint: `http://127.0.0.1:8000/vendor/<vendor_id>/`

- **Update a Vendor**

  - Endpoint: `http://127.0.0.1:8000/vendor/<vendor_id>/edit/`

- **Delete a Vendor**

  - Endpoint: `http://127.0.0.1:8000/vendor/<vendor_id>/delete/`

- **Vendor Performance**
  - Endpoint: `http://127.0.0.1:8000/vendor/<vendor_id>/performance`

### Purchase Order Endpoints

- **Create a Purchase Order**

  - Endpoint: `http://127.0.0.1:8000/purchase_order/create/`

- **List Purchase Orders**

  - Endpoint: `http://127.0.0.1:8000/purchase_order/`

- **Get a Specific Purchase Order**

  - Endpoint: `http://127.0.0.1:8000/purchase_order/<po_id>`

- **Update a Purchase Order**

  - Endpoint: `http://127.0.0.1:8000/purchase_order/<po_id>/edit/`

- **Delete a Purchase Order**

  - Endpoint: `http://127.0.0.1:8000/purchase_order/<po_id>/delete/`

- **Update Acknowledgment**
  - Endpoint: `http://127.0.0.1:8000/purchase_order/<po_id>/acknowledge/`
