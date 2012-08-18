MANAGEPY=foreman run env/bin/python manage.py

update:
	virtualenv env
	env/bin/pip install -r requirements.txt
	$(MANAGEPY) syncdb
	$(MANAGEPY) migrate

run: update
	$(MANAGEPY) runserver 0.0.0.0:8000

deploy:
	git push heroku master
