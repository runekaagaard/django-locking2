""" locking.forms

Forms class for the django-locking project.

"""
from django import forms
from django.contrib.contenttypes.models import ContentType

from locking.models import Lock

class LockingForm(forms.ModelForm):
    """
    Clean the form to enforce orm locking before saving the object.  This will only work if you set lock_type to 'hard' in the locking.models file.
    """

    def clean(self):
        self.cleaned_data = super(LockingForm, self).clean()
        try:
            content_type = ContentType.objects.get_for_model(self.obj)
            lock = Lock.objects.get(entry_id=self.obj.id, app=content_type.app_label, model=content_type.model)
        except:
            return self.cleaned_data
        if lock.is_locked:
            if lock.locked_by != self.request.user and lock.lock_type == 'hard':
                raise forms.ValidationError('You cannot save this object because it is locked by user %s for roughly %s more minute(s).' % (lock.locked_by.username, lock.lock_seconds_remaining/60))
        return self.cleaned_data