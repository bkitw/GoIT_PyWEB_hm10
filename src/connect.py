import configparser
import pathlib
from mongoengine import connect

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
configuration = configparser.ConfigParser()
configuration.read(file_config)

username = configuration.get('MongoDB', 'user')
password = configuration.get('MongoDB', 'password')
domain = configuration.get('MongoDB', 'domain')
db_name = configuration.get('MongoDB', 'db_name')

connect(
    host=f"""mongodb+srv://{username}:{password}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True
)
