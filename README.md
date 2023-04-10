# ecom_backend
This ecom repo is a full-stack web application built with Django, Django Rest Framework, React, TypeScript, Material UI, Postgres, and Stripe. The project includes an admin CMS and allows users to add items to their cart and make purchases. The website is currently hosted at <<Deploying Soon>>.

## Tech Stacks
- Django
- Django Rest Framework
- React
- TypeScript
- Material UI
- PostgreSQL
- Stripe

## Features

- User authentication with Django's built-in authentication system
- User registration and password reset functionality
- User profile management
- Product management via an admin CMS
- Ability to add products to cart
- Secure checkout process with Stripe integration
- Order history and details for users
- Responsive design using Material UI

## Getting Started

- Clone the repository:
```
git clone https://github.com/rlopxhan21/ecom_backend.git
```

- Create virtual environment and Install the dependicies:
```
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
```
- Set up the database:
```
python3 manage.py migrate
```

- Create a superuser:
```
python3 manage.py createsuperuser
```

- Start the development server:
```
python3 manage.py runserver
```

- Open http://localhost:8000 in your browser to view the app.

## Contributing

Contributions are welcome! To contribute to the project, follow these steps:

- Fork the repository
- Create a new branch
- Make your changes and commit them
- Push your changes to your fork
- Create a pull request

## Licence
This project is licensed under the Creative Commons Zero v1.0 Universal.
