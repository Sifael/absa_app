web: python -m spacy download en_core_web_sm && python -m nltk.downloader all && python manage.py migrate && python manage.py collectstatic --no-input && gunicorn absa.wsgi
