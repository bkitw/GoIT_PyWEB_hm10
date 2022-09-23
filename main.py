import argparse
import sys
from src.repo import create_user, get_user, create_contact, get_contact, create_phone, \
    get_contacts_by_user, update_contact, remove_contact, create_email, get_phones_by_contact, \
    get_emails_by_contact, remove_phone, remove_email
import hashlib
from src.models import User, Contact, Phone, Email
from src.connect import connect

parser = argparse.ArgumentParser(description='Personal assistant APP')
parser.add_argument('--action', help='Commands: create_contact, create_phone, create_email,\n'
                                     'get_user, get_contacts_by_user, get_phones_by_contact, get_emails_by_contact,\n'
                                     'update_contact,\n'
                                     'remove_contact, remove_phone, remove_email.')
# parser.add_argument('--id', help='Value of primary key of the contact.')
parser.add_argument('--name', help='Value of "name"-field in the collection "Contacts".')
parser.add_argument('--login', help='Value of "login"-field in the collection "Users".')
parser.add_argument('--new_name', help='Value of "name"-field of specifically contact that you want to insert '
                                       'instead of old one.')
parser.add_argument('--phone', help='Value of "number"-field in the table "Phones".')
parser.add_argument('--email', help='Value of "email"-field in the table "Emails".')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
name = my_arg.get('name')
# _id = my_arg.get('id')
login = my_arg.get('login')
new_name = my_arg.get('new_name')
phone = my_arg.get('phone')
email = my_arg.get('email')


def main(user):
    global phone, email
    match action:
        # creating cases
        case 'create_contact':
            create_contact(name=name, user=user)
            print(f'Contact with name "{name}" successfully created!')
        case 'create_phone':
            create_phone(contact=get_contact(user=user, name=name), phone=phone)
            print(f'Contact with name "{name}" successfully got the number -- {phone}!')
        case 'create_email':
            create_email(contact=get_contact(user=user, name=name), email=email)
            print(f'Contact with name "{name}" successfully got the email -- {email}!')
        # updating cases
        case 'update_contact':
            update_contact(name=name, new_name=new_name, user=user)
            print(f'Contacts name "{name}" was successfully changed to "{new_name}"')
        # removing (deleting) cases
        case 'remove_contact':
            remove_contact(name=name, user=user)
            print(f'Contact "{name}" was successfully removed.')
        case 'remove_phone':
            remove_phone(name=name, phone=phone)
            print(f'Phone {phone} from contact {name} was successfully removed!')
        case 'remove_email':
            remove_email(name=name, email=email)
            print(f'Email {email} from contact {name} was successfully removed!')
        # reading cases
        case 'list':
            for contact in get_contacts_by_user(user):
                print(contact.name, [number.number for number in contact.numbers])
        case 'get_emails_by_contact':
            data = get_emails_by_contact(name)
            print(name, data)
        case 'get_phones_by_contact':
            data = get_phones_by_contact(name=name)
            print(name, data)


if __name__ == '__main__':
    user = get_user(login)
    if user:
        password = hashlib.md5(input('Password: ').encode('utf-8')).hexdigest()
        if password == user['password']:
            main(user)
        else:
            print('Wrong password!')
            sys.exit()
    else:
        print('This user does not exists!\nWould you like to create a new one?')
        password = input('Create your password --> ')
        create_user(login, password)
        print(f'New user with nickname {login} created!')
        sys.exit()
