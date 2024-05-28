
# WeatherApp Backend

This is the backend for the WeatherApp, a RESTful API implemented using Django and Python. The API supports functionalities such as adding/removing comments and includes a JWT authorization system with roles such as admin, authorized user, and non-authorized user. The API documentation is provided through Swagger for easy reference and interaction.

## Features

- RESTful API for managing comments
- JWT authorization system with roles
- Swagger documentation for API endpoints
- Clean and well-structured codebase

## Technologies Used

- Django
- Python
- Swagger

## Installation

### Prerequisites

- Python 3.6+
- pip (Python package installer)
- virtualenv (recommended)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/denis-svg/weather_app_backend.git
   cd weather_app_backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply the migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for accessing the admin interface):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at `http://127.0.0.1:8000/`.

## API Documentation

The API documentation is provided through Swagger. You can access it by navigating to `http://127.0.0.1:8000/swagger/` in your web browser once the server is running.

## Usage

### Authorization

The API uses JWT for authorization. Ensure to include the token in the `Authorization` header for protected endpoints.

### Endpoints

- **/comments/**: Manage comments
- **/auth/**: Authorization-related endpoints

## Project Structure

```
weather_app_backend/
├── manage.py
├── myapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── swagger.py
├── weather_app_backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to suggest.

## Contact

For any inquiries or support, please contact me at [denis.prodan22@proton.me](mailto:denis.prodan22@proton.me).
