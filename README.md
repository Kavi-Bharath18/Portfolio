# Professional Django Portfolio – Kavi Bharath

Pages included: **Home, About, Projects, Skills, Resume, Contact**.

## Quickstart

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata portfolio/fixtures/sample_skills.json  # preload skills
python manage.py runserver
```

Open: http://127.0.0.1:8000/

### Add projects & resume
- Add projects via the Django admin: `python manage.py createsuperuser` then visit `/admin/`.
- Upload your resume (PDF) later; currently the **Resume** page links to your GitHub as a placeholder.

## Deploy notes
- For Heroku-like platforms add:
  - `Procfile` with: `web: gunicorn myportfolio.wsgi:application`
  - `runtime.txt` (e.g., `python-3.12.3`)
- Set env vars: `SECRET_KEY`, `DEBUG=0`, `ALLOWED_HOSTS=yourdomain.com`
- Run `python manage.py collectstatic --noinput` on deploy.
