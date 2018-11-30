from mongoengine import Document, StringField, IntField, BooleanField

class User(Document):
    user = StringField()
    password = StringField()