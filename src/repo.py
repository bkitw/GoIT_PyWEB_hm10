import hashlib
from src.models import User, Contact, Phone, Email


def create_user(login, password):
    User(login=login,
         password=hashlib.md5(password.encode('utf-8')).hexdigest()
         ).save()


def create_contact(name, user):
    Contact(name=name, author=user).save()


def create_phone(contact, phone):
    Contact.objects(id=contact.id).update_one(push__numbers=Phone(number=phone))


def create_email(contact, email):
    Contact.objects(id=contact.id).update_one(push__emails=Email(email=email))


def get_user(login):
    users = User.objects()
    for log in users:
        if log.login == login:
            print(f'Login: {log.login}')
            return log


def get_contacts_by_user(user) -> list[Contact]:
    return Contact.objects(author=user)


def get_contact(user, name):
    return Contact.objects.get(name=name, author=user)


def get_phones_by_contact(name) -> list[Phone]:
    data = Contact.objects.get(name=name).numbers
    phones = []
    for phone in data:
        phones.append(phone.number)
    return phones


def get_emails_by_contact(name) -> list[Email]:
    data = Contact.objects.get(name=name).emails
    emails = []
    for email in data:
        emails.append(email.email)
    return emails


def update_contact(name, new_name, user):
    Contact.objects(name=name, author=user).update_one(name=new_name)


def remove_contact(name, user):
    contact = Contact.objects(name=name, author=user).delete()
    # removing = contact.delete()


def remove_phone(name, phone):
    data = Contact.objects(name=name).update_one(pull__numbers=Phone(number=phone))


def remove_email(name, email):
    data = Contact.objects(name=name).update_one(pull__emails=Email(email=email))
