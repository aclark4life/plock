# https://github.com/aclark4life/python-project
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Alex Clark
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Git
BRANCHES=`git branch -a | grep remote | grep -v HEAD | grep -v master`

# Django
PROJECT = project
APP = app

all: up

clean-pyc:
	find . -name \*.pyc | xargs rm -v

clean-db: clean-postgres
clean-django-migration:
	rm -rf $(PROJECT)/$(APP)/migrations
clean-postgres:
	-dropdb $(PROJECT)-$(APP)
	-createdb $(PROJECT)-$(APP)
clean-sqlite:
	-rm -f db.sqlite3
	-git add db.sqlite3

co:
	-for i in $(branches) ; do \
        git checkout -t $$i ; \
    done

commit:
	git commit -a
commit-update:
	git commit -a -m "Update"

db: migrate su

debug-on-heroku:
	heroku config:set DEBUG=1
debug-off-heroku:
	heroku config:unset DEBUG

flake:
	-flake8 *.py
	-flake8 $(PROJECT)/*.py
	-flake8 $(PROJECT)/$(APP)/*.py

# http://stackoverflow.com/a/26339924
.PHONY: h
help:
	@echo "\nPlease run make with one of the following targets:\n"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F:\
        '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}'\
        | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs | tr ' ' '\n' | awk\
        '{print "    - "$$0}'
	@echo "\n"
install:
	virtualenv .
	bin/pip install -r requirements.txt
lint: yapf flake wc
migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations $(APP)
package-test:
	check-manifest
	pyroma .
push: push-origin
push-heroku:
	git push heroku
push-origin:
	git push
release:
	python setup.py sdist --format=zip upload
releasetest:
	python setup.py sdist --format=zip upload -r test
review:
	open -a "Sublime Text 2" `find $(PROJECT) -name \*.py | grep -v __init__.py`\
        `find $(PROJECT) -name \*.html`
serve:
	python manage.py runserver
shell:
	python manage.py shell
shell-heroku:
	heroku run bash
start-django:
	-mkdir -p $(PROJECT)/$(APP)
	-django-admin startproject $(PROJECT) .
	-django-admin startapp $(APP) $(PROJECT)/$(APP)
start-doc:
	sphinx-quickstart -q -p "Python Project" -a "Alex Clark" -v 0.0.1 doc
static:
	python manage.py collectstatic --noinput
su:
	python manage.py createsuperuser
test:
	python manage.py test
test-readme:
	rst2html.py README.rst > readme.html; open readme.html
update: commit-update
up: commit-update push
upload-test:
	python setup.py sdist --format=gztar,zip upload -r test
upload:
	python setup.py sdist --format=gztar,zip upload
wc:
	wc -l *.py
	wc -l $(PROJECT)/*.py
	wc -l $(PROJECT)/$(APP)/*.py
yapf:
	-yapf -i *.py
	-yapf -i -e $(PROJECT)/urls.py $(PROJECT)/*.py
	-yapf -i $(PROJECT)/$(APP)/*.py
