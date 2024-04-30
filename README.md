# EDS6397 Project Setup Guide

This guide provides detailed instructions on how to set up the EDS6397 project on your local machine. The project is built using Django, a high-level Python web framework.

## Prerequisites

Before you begin, ensure you have Python installed on your system. Python 3.6 or newer is required. You can download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).

## Installation Steps

### 1. Clone the Repository
First, clone the repository to your local machine using the following command:
```bash
git clone https://github.com/Po4991212/EDS6397.git
cd EDS6397
```

### 2. Set up a Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other Python projects. If you don't have `virtualenv` installed, you can install it using pip:

```bash
pip install virtualenv
```

Then, create and activate a virtual environment:

```bash
# For Windows command prompt
virtualenv venv ## command line will create a virtual environment named venv
cd venv/Scripts ## change directory to activate virtual environment
activate ## run activate script to activate virtual environment
# For Git Bash
source venv/bin/activate # On Windows use venv\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

This project uses Django's default SQLite database. Initialize the database with the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

To access the admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the superuser account.

### 6. Run the Server

Finally, you can run the development server:

```bash
python manage.py runserver
```

The server will start at http://127.0.0.1:8000/. You can now access the application in your web browser.

### Basic git commands
## Pulling changes from a remote repository (suggested before you work on the project)

```bash
git pull REMOTE-NAME BRANCH-NAME
# Grabs online updates and merges them with your local work
```

## Pushing commits to a remote repository

```bash
git push REMOTE-NAME BRANCH-NAME
```

