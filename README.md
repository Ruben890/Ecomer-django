# Ecomer-django

Ecomer is an e-commerce project built with Django, Tawilind CSS, and JavaScript.

## Screenshots

<img src="./img/imgen-1(1).png" alt="image-1">
<img src="./img/imgen-1(2).png" alt="image-2">

## Installation

### Prerequisites
- Python 3.11
- Django
- Other requirements...

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ruben890/Ecomer-django.git
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    
3. Run the Django projecto:
    ```bash
   python manage.py runserver
4. Compile static files
    ```bash
        python manage.py tailwind start
5. Migrate the database:
    ```bash
    python manage.py migrate

    python manage.py makemigrations
6. Create a superuser (if needed):
    ```bash
    python manage.py createsuperuser
