# Service Center Job Card Management System

## Overview

The Service Center Job Card Management System is a REST API developed using Python, Django, and Django REST Framework to manage vehicle service requests.

The application allows users to register, create service requests, manage vehicle information, describe vehicle problems, select service types, assign priorities, and schedule service dates.

It includes authentication, user-specific data access, custom permissions, input validation, and service request filtering.

## Features

* User registration
* Basic Authentication
* Create service requests
* List service requests belonging to the authenticated user
* Retrieve individual service requests
* Update existing service requests
* Delete service requests
* Vehicle registration number validation and normalization
* Problem description validation
* User-specific service request management
* Ownership-based access control
* Count service requests belonging to the authenticated user
* Filter service requests by High and Critical priorities
* SQLite database integration

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* Django ORM
* Git
* GitHub
* VS Code REST Client

## Project Structure

```text
SERVICE-CENTER-JOB-CARD-MANAGEMENT-SYSTEM/
│
├── service_center/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── service_requests/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── .gitignore
├── APIDOC.http
├── manage.py
└── README.md
```

## Service Request Details

The `ServiceRequest` model manages vehicle service requests.

| Field                 | Description                              |
| --------------------- | ---------------------------------------- |
| `vehicle_number`      | Vehicle registration number              |
| `vehicle_model`       | Model of the vehicle                     |
| `problem_description` | Description of the vehicle problem       |
| `service_type`        | Type of service required                 |
| `priority`            | Priority assigned to the request         |
| `service_date`        | Scheduled service date                   |
| `created_date`        | Date and time the request was created    |
| `user`                | User associated with the service request |

### Service Types

* General Service
* Engine Repair
* Brake Repair
* Electrical
* AC Repair
* Tyre Service

### Priority Levels

* Low
* Medium
* High
* Critical

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/aravindbalaji4851-cmd/SERVICE-CENTER-JOB-CARD-MANAGEMENT-SYSTEM.git
```

### 2. Navigate to the Project Directory

```bash
cd SERVICE-CENTER-JOB-CARD-MANAGEMENT-SYSTEM
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages:

```bash
pip install django djangorestframework
```

### 6. Configure Environment Variables

The project uses environment-based configuration for the Django secret key.

Configure a valid `SECRET_KEY` in your local environment before starting the application if it is required by your settings.

Do not commit your `.env` file or expose secret keys in the repository.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

If new model migrations need to be created, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Start the Development Server

```bash
python manage.py runserver
```

The development server will run at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

All service request endpoints use the `/service-requests/` prefix.

| HTTP Method | Endpoint                           | Description                                    | Authentication |
| ----------- | ---------------------------------- | ---------------------------------------------- | -------------- |
| POST        | `/service-requests/user-register/` | Register a new user                            | Not required   |
| GET         | `/service-requests/`               | List the authenticated user's service requests | Required       |
| POST        | `/service-requests/`               | Create a service request                       | Required       |
| GET         | `/service-requests/<id>/`          | Retrieve a specific service request            | Required       |
| PUT         | `/service-requests/<id>/`          | Update a service request                       | Required       |
| DELETE      | `/service-requests/<id>/`          | Delete a service request                       | Required       |
| GET         | `/service-requests/count/`         | Count the user's service requests              | Required       |
| GET         | `/service-requests/high-critical/` | List High- and Critical-priority requests      | Required       |

## API Usage Examples

### 1. User Registration

**Endpoint:** `POST /service-requests/user-register/`

**Request Body:**

```json
{
    "username": "user01",
    "first_name": "Arun",
    "last_name": "K",
    "email": "arun01@example.com",
    "password": "your-test-password"
}
```

Creates a new user account that can be used to authenticate subsequent API requests.

### 2. Create a Service Request

**Endpoint:** `POST /service-requests/`

**Authentication:** Basic Authentication

**Request Body:**

```json
{
    "vehicle_number": "KL45Y5243",
    "vehicle_model": "Alto K10",
    "problem_description": "Engine light on.",
    "service_type": "Engine Repair",
    "priority": "High",
    "service_date": "2026-10-26"
}
```

The service request is associated with the authenticated user.

### 3. List Service Requests

**Endpoint:** `GET /service-requests/`

Returns the service requests belonging to the authenticated user.

### 4. Retrieve a Specific Service Request

**Endpoint:** `GET /service-requests/1/`

Retrieves the specified service request, subject to ownership permissions.

### 5. Update a Service Request

**Endpoint:** `PUT /service-requests/1/`

**Request Body:**

```json
{
    "vehicle_number": "KL45Y5243",
    "vehicle_model": "Alto K10",
    "problem_description": "Engine noise and vibration need inspection.",
    "service_type": "Engine Repair",
    "priority": "Critical",
    "service_date": "2026-10-27"
}
```

Updates an existing service request after validating the submitted data.

A PUT request generally requires all required fields.

### 6. Delete a Service Request

**Endpoint:** `DELETE /service-requests/1/`

Deletes the specified service request if the authenticated user is authorized to access it.

### 7. Count Service Requests

**Endpoint:** `GET /service-requests/count/`

Returns the total number of service requests belonging to the authenticated user.

Example response:

```json
{
    "total_services": 3
}
```

The count depends on the records associated with the authenticated user.

### 8. Filter High- and Critical-Priority Requests

**Endpoint:** `GET /service-requests/high-critical/`

Returns the authenticated user's service requests with either High or Critical priority.

## Authentication and Permissions

The application uses Django REST Framework's Basic Authentication.

Protected endpoints require valid user credentials.

Custom ownership permissions restrict users from accessing or modifying service requests belonging to other users.

The API is designed to ensure that authenticated users manage their own service requests.

## Validation

### Vehicle Number Validation

The application validates vehicle registration numbers according to the rules implemented in the serializer.

Validation includes checking the format of the registration number, removing spaces, and converting letters to uppercase.

### Problem Description Validation

The problem description is validated to prevent empty or whitespace-only values.

Leading and trailing whitespace is removed before saving.

## Database

The project uses SQLite for development and Django ORM for database operations.

Django migrations manage database schema changes.

A fresh installation can initialize its database by applying the project's migrations.

## API Testing

The API can be tested using:

* VS Code REST Client
* Postman
* Insomnia

The `APIDOC.http` file contains example HTTP requests for testing the API endpoints.

### Recommended Test Cases

* User registration
* Valid and invalid authentication
* Creating a service request
* Listing service requests
* Retrieving an individual request
* Updating a request
* Deleting a request
* Invalid vehicle registration numbers
* Empty problem descriptions
* Accessing another user's service request
* Counting service requests
* Filtering High- and Critical-priority requests

## Future Enhancements

* Service request status tracking
* Mechanic assignment
* Administrator and staff roles
* Service completion and delivery management
* Appointment scheduling
* Search by vehicle registration number
* Additional automated API tests
* Frontend integration

## Author

**Aravind Balaji K J**

GitHub: [aravindbalaji4851-cmd](https://github.com/aravindbalaji4851-cmd)

Project Repository: [SERVICE-CENTER-JOB-CARD-MANAGEMENT-SYSTEM](https://github.com/aravindbalaji4851-cmd/SERVICE-CENTER-JOB-CARD-MANAGEMENT-SYSTEM)
