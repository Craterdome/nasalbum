nasalbum
=========
Install Python and pip for your environment.

### Setup environment
```bash
cd nasalbum
mkvirtualenv venv  # install env wherever you prefer
venv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
