# encoding: utf-8

from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType

from locking.models import Lock
from locking import logger

def user_may_change_model(fn):
    def view(request, app, model, *vargs, **kwargs):
        may_change = '%s.change_%s' % (app, model)
        if not request.user.has_perm(may_change):
            return HttpResponse(status=401)
        else:
            return fn(request, app, model, *vargs, **kwargs)
            
    return view

def is_lockable(fn):
    def view(request, app, model, *vargs, **kwargs):
    	return fn(request, app, model, *vargs, **kwargs)
    return view

def log(view):
    def decorated_view(*vargs, **kwargs):
        response = view(*vargs, **kwargs)
        logger.debug("Sending a request: \n\t%s" % (response.content))
        return response
    
    return decorated_view