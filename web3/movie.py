from mongoengine import Document, StringField, IntField, BooleanField

class Movie(Document):
    title = StringField()
    image = StringField()
    year = IntField()
    user = StringField()
    password = StringField()
    