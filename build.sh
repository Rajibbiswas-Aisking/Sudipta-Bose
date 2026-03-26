#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py create_superuser_auto
```

**`Procfile`** (optional but good practice):
```
web: gunicorn config.wsgi:application
```

Add `gunicorn` and `whitenoise` to your **`requirements.txt`**:
```
gunicorn==21.2.0
whitenoise==6.7.0