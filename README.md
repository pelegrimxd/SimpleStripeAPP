# Simple Stripe Django App

Простое приложение для обработки платежей через Stripe с админ-панелью на Django.

## Демо

Приложение доступно онлайн по адресу: [https://simple-stripe.ru](https://simple-stripe.ru)

**Данные для входа в админку:**
- Логин: `admin`
- Пароль: `admin`

**Тестовый номер карты для stripe:**
- Номер карты: `4242 4242 4242 4242`

## Локальная установка

### Требования
- Python 3.8+
- PostgreSQL
- Stripe API ключи (можно получить на [stripe.com](https://stripe.com))
- pip

### Инструкция по установке

1. Клонируйте репозиторий:
```bash
git clone https://github.com/pelegrimxd/SimpleStripeAPP.git
cd SimpleStripeAPP
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или 
venv\Scripts\activate  # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` на основе `.env.example` и настройте подключение к PostgreSQL:
```ini
DB_NAME=simple_stripe
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

5. Настройте Stripe API ключи в `.env`:
```ini
STRIPE_PUBLIC_KEY=your_stripe_publishable_key
STRIPE_SECRET_KEY=your_stripe_secret_key
```

6. Примените миграции:
```bash
python manage.py migrate
```

7. Создайте суперпользователя (админа):
```bash
python manage.py createsuperuser
```
(укажите логин `admin` и пароль `admin` или свои данные)

8. (Опционально) Заполните базу тестовыми данными:
```bash
python manage.py loaddata fixtures.json
```

9. Запустите сервер разработки:
```bash
python manage.py runserver
```

Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

## Доступ в админку

После запуска вы можете войти в админ-панель:
- URL: `/admin`
- Логин: `admin`
- Пароль: `admin`
