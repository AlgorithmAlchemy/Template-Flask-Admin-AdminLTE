# Flask-Admin Project with AdminLTE3 Theme

`⭐️ Thanks to everyone who has starred the project — it really means a lot!`

**Read this in other languages:** [Русский (README.md)](README_ru.md)

---

This is a Flask web application template with Flask-Admin integration and the AdminLTE3 theme.

<div style="display: flex; justify-content: space-between; max-width: 820px; margin: 0 auto;">
  <img src="https://github.com/user-attachments/assets/889fd8f1-129a-4d5b-aa67-ee189fded0f1" alt="dd_DeWatermark" width="400" />
  <img src="https://github.com/user-attachments/assets/d4e852e4-8538-48d9-a44c-95f08f29661a" alt="dd_DeWatermark" width="400" />
</div>

## Features

* Flask 2.x
* SQLAlchemy for SQLite database management
* Flask-Admin for model administration
* AdminLTE3 theme integration for a modern UI
* Example `User` model with `id`, `name`, and `email` fields
* Dashboard page with multiple Chart.js visualizations

---

## Project Structure

```
/project-root
├── app.py                 # Main application file
├── templates/             # Jinja2 templates
│   ├── admin_layout.html  # AdminLTE3 dashboard layout
│   └── ...
├── static/                # Static files (CSS, JS, images)
├── data/                  # Data/database directory
│   └── mydatabase.db      # SQLite database (created automatically)
├── requirements.txt       # Dependency list
└── README.md              # Project documentation
```

---

## Installation

1. Clone the repository:

```bash
git clone <repository_URL>
cd project-root
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # Linux/MacOS
venv\Scripts\activate       # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

By default, the server will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Contact

Author: AlgorithmAlchemy
