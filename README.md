rogueojiiofwales
================

DjangoDash Awesomesauce


How-To
------

* Clone the repo.
* Add a git remote called ``heroku`` pointing at ``git@heroku.com:insertcreativenamehere.git``.
* Create a file called .env and add two values: ``DATABASE_URL=sqlite://localhost/local.db`` and ``DEBUG=True``.
* Create a GitHub app on https://github.com/settings/applications setting both urls to http://localhost:8000/.
* Add ``GITHUB_APP_SECRET`` and ``GITHUB_APP_ID`` to your .env file using the credentials from github.
* Run ``make run``.
* Open http://localhost:8000
* Hack.


Run local commands
------------------

``foreman run env/bin/python manage.py ...``

Run remote commands
-------------------

``heroku run python manage.py ...``

Deploy
------

``make deploy``
