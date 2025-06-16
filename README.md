
# Проект Flask-Admin с темой AdminLTE3

Это шаблон веб-приложения на Flask с интеграцией Flask-Admin и темой AdminLTE3 для удобной и стильной административной панели.

---![2025-06-16_18-32](https://github.com/user-attachments/assets/889fd8f1-129a-4d5b-aa67-ee189fded0f1)
![2025-06-16_18-32](https://github.com/user-attachments/assets/889fd8f1-129a-4d5b-aa67-ee189fded0f1)
![2025-06-16_18-32_1](https://github.com/user-attachments/assets/d4e852e4-8538-48d9-a44c-95f08f29661a)
![2025-06-16_18-32_1](https://github.com/user-attachments/assets/d4e852e4-8538-48d9-a44c-95f08f29661a)


## Особенности

- Flask 2.x
- SQLAlchemy для работы с базой данных SQLite
- Flask-Admin для управления моделями
- Интеграция темы AdminLTE3 для современного интерфейса
- Пример модели `User` с полями `id`, `name`, `email`
- Вкладка Dashboard с разными типами графиков на Chart.js

---

## Структура проекта

```

/project-root
├── app.py                 # Основной файл приложения
├── templates/             # Шаблоны Jinja2
│   ├── admin\_layout.html  # Шаблон дашборда с AdminLTE3
│   └── ...
├── static/                # Статические файлы (CSS, JS, картинки)
├── data/                  # Папка для данных/баз данных
│   └── mydatabase.db      # SQLite база (создаётся автоматически)
├── requirements.txt       # Список зависимостей
└── README.md              # Документация проекта

````

---

## Установка

1. Клонируйте репозиторий:
```bash
git clone <URL_репозитория>
cd project-root
````

2. Создайте виртуальное окружение и активируйте его:

```bash
python -m venv venv
source venv/bin/activate    # Linux/MacOS
venv\Scripts\activate       # Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

---

## Запуск

```bash
python app.py
```

По умолчанию сервер будет доступен по адресу: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Использование

* Админка доступна по корневому URL (`/admin`)
* В админке можно управлять пользователями (CRUD для модели User)
* Вкладка Dashboard отображает разные типы графиков с помощью Chart.js

---

## Добавление пустых папок в Git

Git не хранит пустые папки, поэтому для их фиксации создайте в них файл `.gitkeep`:

```bash
touch data/.gitkeep
touch static/.gitkeep
```

---

## Зависимости

* Flask
* Flask-SQLAlchemy
* Flask-Admin
* Flask-AdminLTE3 (если используется)

---

## Контакты

Автор: AlgoritmAlchemy
