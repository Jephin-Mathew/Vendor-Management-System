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
  - _Method_: POST
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`
  - _Body_:
    ```json
    {
      "name": "Vendor Name",
      "contact_details": "Contact Information",
      "address": "Vendor Address",
      "vendor_code": "VENDOR123"
    }
    ```

- **List Vendors**

  - Endpoint: `http://127.0.0.1:8000/vendor/`
  - _Method_: GET
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`

- **Get Details of a Specific Vendor**

  - Endpoint: `http://127.0.0.1:8000/vendor/<vendor_id>/`
  - _Method_: GET
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`

- **Update a Vendor**

  - Endpoint: `http://127.0.0.1:8000/vendor/<vendor_id>/edit/`
  - _Method_: PUT
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`
  - _Body_:
    ```json
    {
        "name": "vendor",
        "contact_details": "9293458854",
        "address": "vendor address",
        "vendor_code": "54321","
    }
    ```

- **Delete a Vendor**

  - Endpoint: `http://127.0.0.1:8000/vendor/<vendor_id>/delete/`
  - _Method_: DELETE
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`

- **Vendor Performance**
  - Endpoint: `http://127.0.0.1:8000/vendor/<vendor_id>/performance`
  - _Method_: GET
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`

### Purchase Order Endpoints

- **Create a Purchase Order**

  - Endpoint: `http://127.0.0.1:8000/purchase_order/create/`
  - _Method_: POST
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`
  - _Body_:

  ```json
  {
    "id": 1,
    "po_number": "1",
    "order_date": "2023-11-27T17:23:53+05:30",
    "delivery_date": "2023-12-01T17:23:59+05:30",
    "items": {
      "item": "mobile"
    },
    "quantity": 1,
    "status": "completed",
    "quality_rating": 5.0,
    "issue_date": "2023-11-27T17:25:12+05:30",
    "acknowledgment_date": "2023-11-27",
    "is_on_time_delivery": true,
    "vendor": 1
  }
  ```

- **List Purchase Orders**

  - Endpoint: `http://127.0.0.1:8000/purchase_order/`
  - _Method_: GET
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`

- **Get a Specific Purchase Order**

  - Endpoint: `http://127.0.0.1:8000/purchase_order/<po_id>`
  - _Method_: GET
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`

- **Update a Purchase Order**
  - Endpoint: `http://127.0.0.1:8000/purchase_order/<po_id>/edit/`
  - _Method_: PUT
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`
  - _Body_:
  ```json
  {
    "po_number": "3",
    "order_date": "2023-11-27T17:23:53+05:30",
    "delivery_date": "2023-12-10T00:00:00+05:30",
    "items": "Laptop",
    "quantity": 2,
    "status": "completed",
    "quality_rating": 4.5,
    "issue_date": "2023-11-27T17:25:12+05:30",
    "vendor": 1
  }
  ```
- **Delete a Purchase Order**
  - Endpoint: `http://127.0.0.1:8000/purchase_order/<po_id>/delete/`
  - _Method_: DELETE
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`
- **Update Acknowledgment**
  - Endpoint: `http://127.0.0.1:8000/purchase_order/<po_id>/acknowledge/`
  - _Method_: POST
  - _Headers_:  
    `Authorization:Token a74336a3ea0b76239abd630e2bda5142d7f12972`
  - _Body_
  ```json
  {
    "po_number": 1,
    "order_date": "2023-12-10",
    "delivery_date": "2023-12-20",
    "items": "Tv",
    "quantity": 1,
    "status": "pending",
    "issue_date": "2023-12-12",
    "vendor": 1
  }
  ```
