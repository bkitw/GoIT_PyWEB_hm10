from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import EmbeddedDocumentField, ListField, StringField, ReferenceField


class Phone(EmbeddedDocument):
    number = StringField()


class Email(EmbeddedDocument):
    email = StringField()


class User(Document):
    login = StringField()
    password = StringField()
    meta = {'allow_inheritance': True}


class Contact(Document):
    name = StringField()
    numbers = ListField(EmbeddedDocumentField(Phone))
    emails = ListField(EmbeddedDocumentField(Email))
    meta = {'allow_inheritance': True}
    author = ReferenceField(User, reverse_delete_rule=True)
