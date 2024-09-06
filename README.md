# App Dashboard API

This project is a Django-based backend service that exposes a set of REST API endpoints, enabling users to:

- Register, login, and reset passwords
- Create, retrieve, update, and delete applications
- Associate subscriptions with pricing plans
- Manage subscriptions (activate/deactivate)

The project uses Django Rest Framework (DRF) and JWT (JSON Web Token) for authentication.

## Project Features

### Applications

- Users can create, update, retrieve, and delete applications.
- Applications are automatically subscribed to the "Free" plan when created.

### Subscriptions

- Each app is associated with a subscription.
- Subscriptions can be updated with different pricing plans.
- Subscriptions can be deactivated instead of deleted.

### Plans

Three pre-configured pricing plans are available:
- Free ($0)
- Standard ($10)
- Pro ($25)

## Authentication

Registration, login, and token refresh are managed through JWT.

## Technologies Used

- **Django** - Python Web Framework
- **Django Rest Framework (DRF)** - For building the RESTful API
- **Django Rest Framework SimpleJWT** - For JWT authentication
- **SQLite (default)** - Database (can be changed to PostgreSQL, MySQL, etc.)

## Installation

Follow these steps to get the project up and running locally:

1. Clone the repository:

    ```bash
    git clone https://github.com/omersaleem09/subscription_django
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/Mac
    # For Windows, use venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Create superuser (optional but recommended):

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Running the Project

Once you have followed the installation steps, you can start the server and access the API at:

- API: [http://localhost:8000/api/](http://localhost:8000/api/)
- Django Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## API Endpoints

### Authentication Endpoints

- **POST /api/register/**: Register a new user.
- **POST /api/token/**: Obtain a JWT token (login).
- **POST /api/token/refresh/**: Refresh the JWT token.

### Application Endpoints

- **GET /api/apps/**: Retrieve the list of apps.
- **POST /api/apps/**: Create a new app (auto-subscribes to the Free plan).
- **GET /api/apps/{id}/**: Retrieve details of a specific app.
- **PUT /api/apps/{id}/**: Update a specific app.
- **DELETE /api/apps/{id}/**: Delete an app.

### Subscription Endpoints

- **GET /api/subscriptions/**: Retrieve the list of subscriptions.
- **PUT /api/subscriptions/{id}/**: Update a subscription (change plan).
- **DELETE /api/subscriptions/{id}/**: Deactivate a subscription.

### Plan Endpoints

- **GET /api/plans/**: Retrieve the list of pricing plans.

## Curl Request's


```bash
curl --location 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/json' \
--data-raw '{"username": "your_username", "password": "your_password"}'


curl --location 'http://localhost:8000/api/token/refresh/' \
--header 'Content-Type: application/json' \
--data-raw '{"refresh": "your_refresh_token"}'


curl --location 'http://localhost:8000/api/register/' \
--header 'Content-Type: application/json' \
--data-raw '{"username": "new_user", "password": "password123", "email": "new_user@example.com"}'



curl --location 'http://localhost:8000/api/apps/' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "My App", "description": "An awesome app"}'

curl --location 'http://localhost:8000/api/apps/' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'


curl --location 'http://localhost:8000/api/apps/{id}/' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'


curl --location --request PUT 'http://localhost:8000/api/apps/{id}/' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "Updated App", "description": "Updated description"}'


curl --location --request DELETE 'http://localhost:8000/api/apps/{id}/' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'


curl --location --request PUT 'http://localhost:8000/api/subscriptions/{id}/' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{"plan": 2}'  # Change the plan ID as needed

curl --location --request DELETE 'http://localhost:8000/api/subscriptions/{id}/' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

curl --location 'http://localhost:8000/api/plans/' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

