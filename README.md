nasalbum
=========

### Setup Django environment
Install Python and pip for your environment.
```bash
git clone git@github.com:Craterdome/nasalbum.git
cd nasalbum
mkvirtualenv venv  # install env wherever you prefer
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser # fill this out
python manage.py import_images --path=<PROJECT_PATH>\images
python manage.py runserver
```

### Testing Django
http://localhost:8000/

http://localhost:8000/swagger/
```bash
python manage.py test
```

## Setup Vue App

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run all tests
npm test
```
