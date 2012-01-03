=======================================
Concurrency control with django-locking
=======================================

Django has seen great adoption in the content management sphere, especially among the newspaper crowd. One of the trickier things to get right, is to make sure that nobody steps on each others toes while editing and modifying existing content. Newspaper editors might not always be aware of what other editors are up to, and this goes double for distributed teams. When different people work on the same content, the one who saves last will win the day, while the other edits are overwritten.

django-locking provides a system that makes concurrent editing impossible, and informs users of what other users are working on and for how long that content will remain locked. Users can still read locked content, but cannot modify or save it.

django-locking makes sure no two users can edit the same content at the same time, preventing annoying overwrites and lost time. Find the repository and download the code at http://github.com/stdbrouw/django-locking

django-locking has only been tested on Django 1.2 and 1.3, but probably works from 1.0 onwards.

Documentation
-------------
Forked from the Django Locking plugin at stdbrouw/django-locking, this code features the cream of the crop for django-locking combining features from over 4 repos!

New features added to this fork

============================
Changes on change list pages
============================

Unlock content object from change list page by simply clicking on the lock icon
_______________________________________________________________________________


