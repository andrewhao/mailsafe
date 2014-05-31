# App Engine Datastore model, "webapp/main.py"
from django.db import models
from google.appengine.ext import db
import uuid

class UUIDProperty(db.StringProperty) :
    
    def __init__(self, *args, **kwargs):
        db.StringProperty.__init__(self, *args, **kwargs)
    
    def pre_save(self, model_instance, add):
        if add :
            value = str(uuid.uuid4())
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(db.StringProperty, self).pre_save(model_instance, add)

class Author(db.Model):
    name = db.TextProperty()

class Supporter(db.Model):
    name = db.TextProperty()
    email = db.TextProperty()
    phone = db.TextProperty()
    date_added = db.DateTimeProperty(auto_now_add=True)

class Content(db.Model):
    blob = db.BlobProperty()
    text = db.TextProperty()

class Link(db.Model):
    link = UUIDProperty()
    supporter_id = db.IntegerProperty()
    content_id = db.IntegerProperty()
    compromised = db.BooleanProperty()
