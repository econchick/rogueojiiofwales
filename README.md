rogueojiiofwales
================

DjangoDash Awesomesauce


How-To
------

* Clone the repo.
* Add a git remote called ``heroku`` pointing at ``git@heroku.com:insertcreativenamehere.git``.
* Create a file called .env and add: ``DATABASE_URL=sqlite://localhost/local.db``, ``SECRET_KEY=<some secret key>`` and ``DEBUG=True``.
* Run ``make run``.
* Open http://localhost:8000
* Hack.

**NEVER** commit your .env file!

Run local commands
------------------

``foreman run env/bin/python manage.py ...``

Run remote commands
-------------------

``heroku run python manage.py ...``

Deploy
------

``make deploy``
