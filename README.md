# Job Board REST API 💼

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-2.x-orange.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A backend service for a job board application built with Python and Flask. This API handles user registration, JWT-based authentication, and full CRUD operations for job postings and applications.

---

## Table of Contents

-   [Features](#features-✨)
-   [Technologies Used](#technologies-used-🛠️)
-   [Setup and Installation](#setup-and-installation-🚀)
-   [API Endpoints](#api-endpoints-🔌)
-   [Contributing](#contributing-🤝)
-   [License](#license-📜)

---

## Features ✨

-   🔐 **User Authentication**: Secure user registration and login using JWT access tokens.
-   📋 **Job Management**: Endpoints for creating, viewing, and listing job postings.
-   ✍️ **Application System**: Allows authenticated users to apply for jobs.
-   🛡️ **Authorization**: Secure endpoints ensure that only the creator of a job can view its applications.
-   🔄 **Database Migrations**: Uses Flask-Migrate to manage database schema changes.

---

## Technologies Used 🛠️

-   **Backend**: Python, Flask, Flask-RESTful
-   **Database**: SQLite, SQLAlchemy
-   **Authentication**: Flask-JWT-Extended
-   **Database Migrations**: Flask-Migrate
-   **Testing**: Postman

---

## Setup and Installation 🚀

Follow these steps to get the project running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file** in the root directory and add a secret key:
    ```
    JWT_SECRET_KEY='your-super-secret-key'
    ```

5.  **Initialize and upgrade the database:**
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

6.  **Run the application:**
    ```bash
    python app.py
    ```
    The API will be running at `http://127.0.0.1:5000`.

---

## API Endpoints 🔌

### User Authentication

| Method | Endpoint          | Description              | Protected |
| :----- | :---------------- | :----------------------- | :-------- |
| `POST` | `/register`       | Register a new user.     | No        |
| `POST` | `/login`          | Log in to get an access token. | No        |

### Job Management

| Method | Endpoint          | Description              | Protected |
| :----- | :---------------- | :----------------------- | :-------- |
| `GET`  | `/jobs`           | Get a list of all jobs.  | No        |
| `POST` | `/jobs`           | Create a new job posting. | **Yes** |
| `GET`  | `/job/<int:job_id>` | Get details of a single job. | No        |

### Job Applications

| Method | Endpoint                       | Description                           | Protected |
| :----- | :----------------------------- | :------------------------------------ | :-------- |
| `POST` | `/job/<int:job_id>/apply`      | Submit an application for a job.      | **Yes** |
| `GET`  | `/job/<int:job_id>/applications` | View all applications for a specific job. | **Yes** |

---

## Contributing 🤝

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for more details.
