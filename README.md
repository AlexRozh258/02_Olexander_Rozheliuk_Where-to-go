# My Favorite Places (Django Project)

Цей проєкт створений для демонстрації роботи з Django.  
Сайт дозволяє зберігати улюблені місця (ресторани, парки, розваги) та випадковим чином обирати, куди піти сьогодні.

---

##  Як запустити проєкт

1. Клонувати репозиторій:
git clone https://github.com/username/my_favorite_places.git
cd my_favorite_places

2. Створити віртуальне оточення (Python 3.12)
python -m venv venv

3. Активація:
Windows PowerShell:
venv\Scripts\activate

WSL / Linux / Mac:
source venv/bin/activate

4. Встановити залежності
pip install -r requirements.txt

5. Виконати міграції
python manage.py migrate

6. Запустити сервер
python manage.py runserver

7. Відкрити у браузері:
http://127.0.0.1:8000/

8. Функціонал:
Список улюблених місць

Рейтинги з відображенням зірочками

Випадковий вибір місця ("Куди піти сьогодні?")

Форма для додавання нових місць

Окремі сторінки для кожного місця

9. Використані технології:
Python 3.12

Django 5.2.6

HTML + CSS

