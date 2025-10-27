# Проект Flask-Admin с темой AdminLTE3

`⭐️ Thanks everyone who has starred the project, it means a lot!`

**Read this in other languages:** [English (README.md)](README.md)

---

Это шаблон веб-приложения на Flask с интеграцией Flask-Admin и темой AdminLTE3


<div style="display: flex; justify-content: space-between; max-width: 820px; margin: 0 auto;">
  <img src="https://github.com/user-attachments/assets/889fd8f1-129a-4d5b-aa67-ee189fded0f1" alt="dd_DeWatermark" width="400" />
  <img src="https://github.com/user-attachments/assets/d4e852e4-8538-48d9-a44c-95f08f29661a" alt="dd_DeWatermark" width="400" />
</div>

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

## Контакты

Автор: AlgoritmAlchemy
