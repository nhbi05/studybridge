# Study Bridge

**Study Bridge** is an open-source platform for University students to access and share academic resources, interact with peers, and enhance their learning experience. This repository hosts the codebase for the project, with a focus on both backend and frontend development.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technical Stack](#technical-stack)
4. [Setup Instructions](#setup-instructions)
   - [Backend (Django)](#backend-django)
   - [Frontend (React)](#frontend-react)
   - [Setup Instructions with Docker](#setup-instructions-with-docker)
5. [Contribution Guidelines](#contribution-guidelines)
6. [Focus for Frontend Contributors](#focus-for-frontend-contributors)
7. [Future Enhancements](#future-enhancements)

---

## Project Overview

MUK Study Bridge aims to:

- Provide a centralized hub for sharing lecture notes, handouts, and past papers.
- Offer interactive tutorials and tools for peer-to-peer learning.
- Facilitate discussions and real-time group studies.

The project is open source, and contributors are encouraged to join and improve it.

---

## Features

1. **Resource Sharing**: Upload/download notes, past papers, and tutorials.
2. **Interactive Tutorials**: Live and recorded tutorials categorized by subject.
3. **Discussion Forums**: Collaborative problem-solving and knowledge sharing.
4. **Personalized Dashboard**: Track saved resources, tutorials, and activity.
5. **Study Schedules**: Share and manage study timetables.
6. **Gamification System**: Reward contributors with badges and leaderboards.

---

## Technical Stack

### Frontend:

- **React.js**: Component-based development for dynamic UI.
- **HTML/CSS/JavaScript**: Core web technologies.
- **Bootstrap** or **Tailwind CSS**: Styling and responsiveness.

### Backend:

- **Django**: Python-based backend framework.
- **PostgreSQL**: Database for storing user data and resources.

---

## Setup Instructions

Follow these steps to set up the project on your local machine:

### Backend (Django):

1. Clone the repository:
   ```bash
   git clone https://github.com/nhbi05/studybridge.git
   cd studybridge/backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend (React):

1. Navigate to the frontend folder:
   ```bash
   cd muk-study-bridge/frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
4. Access the app on `http://localhost:3000`.

### Setup Instructions with Docker:

1. Ensure Docker is installed:
   ```bash
   docker --version
   docker-compose --version
   ```
2. Create the necessary project directories:
   ```bash
   mkdir muk-study-bridge
   cd muk-study-bridge
   mkdir backend
   touch Dockerfile docker-compose.yml
   ```
3. Create the Dockerfile in the `backend` folder:
   ```Dockerfile
   FROM python:3.10

   # Set environment variables
   ENV PYTHONDONTWRITEBYTECODE 1
   ENV PYTHONUNBUFFERED 1

   # Set the working directory
   WORKDIR /app

   # Install dependencies
   COPY requirements.txt /app/
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy project files
   COPY . /app/
   ```
4. Create `docker-compose.yml` in the root directory:
   ```yaml
   services:
     db:
       image: postgres:13
       container_name: muk_db
       volumes:
         - postgres_data:/var/lib/postgresql/data/
       environment:
         POSTGRES_DB: study_bridge
         POSTGRES_USER: admin
         POSTGRES_PASSWORD: adminpassword
       ports:
         - "5432:5432"

     web:
       build: ./backend
       container_name: muk_web
       command: >
         sh -c "python manage.py migrate &&
                python manage.py runserver 0.0.0.0:8000"
       volumes:
         - ./backend:/app
       ports:
         - "8000:8000"
       depends_on:
         - db
       environment:
         - DEBUG=1
         - DB_NAME=study_bridge
         - DB_USER=admin
         - DB_PASSWORD=adminpassword
         - DB_HOST=db
         - DB_PORT=5432

   volumes:
     postgres_data:
   ```
5. Start the containers:
   ```bash
   docker-compose up --build
   ```
6. Access the web container:
   ```bash
   docker exec -it muk_web bash
   ```
7. Inside the container, initialize Django:
   ```bash
   django-admin startproject muk_study_bridge .
   ```
8. Modify `settings.py` to use PostgreSQL and apply migrations:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
9. Restart the containers:
   ```bash
   docker-compose down
   docker-compose up
   ```
---

## Contribution Guidelines

We welcome contributions to MUK Study Bridge! Here’s how to get started:

1. **Fork** the repository.
2. **Clone** the forked repo:
   ```bash
   git clone https://github.com/nhbi05/studybridge.git
   ```
3. Create a new branch for your feature:
   ```bash
   git checkout -b feature-branch-name
   ```
4. Make changes, test thoroughly, and commit:
   ```bash
   git add .
   git commit -m "Add description of your feature"
   ```
5. Push the changes to your fork:
   ```bash
   git push origin feature-branch-name
   ```
6. Submit a **Pull Request** to the `main` branch.

---

## Focus for Frontend Contributors

### Tasks to Begin With:

- Build reusable React components such as:
  - Navbar, Footer, Cards, Buttons
  - Resource Upload/Download Components
- Design key pages:
  - Home Page
  - Resource Page
  - Discussion Forum Page
  - Login/Signup Page
- Implement responsiveness using **Bootstrap** or **Tailwind CSS**.
- Integrate APIs provided by the backend for dynamic content rendering.

### Code Standards:

- Use **React functional components** and hooks.
- Follow clean code practices:
  - Format code with **Prettier**.
  - Lint with **ESLint**.
- Ensure modularity: Break code into smaller components.
- Test your changes before submitting a Pull Request.

---

## Future Enhancements

- **AI-Based Recommendations**: Suggest resources and tutorials based on user activity.
- **Mobile App**: Develop Android and iOS apps for better accessibility.
- **Analytics Dashboard**: Provide insights for admins and tutors.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any questions or suggestions, feel free to reach out:

- **Email**: [nhousnahishaq@gmail.com](mailto\:nhousnahishaq@gmail.com)
- **GitHub**: [nhbi05](https://github.com/nhbi05)

---

Happy Contributing! 🚀

