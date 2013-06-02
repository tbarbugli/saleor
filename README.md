Saleor
======

Avast ye landlubbers! Saleor be a Satchless store ye can fork.


Heroku notes
------------

heroku config:add BUILDPACK_URL=git://github.com/jiaaro/heroku-buildpack-django.git
heroku config:set PATH=bin:node_modules/.bin:/app/bin:/usr/local/bin:/usr/bin:/bin