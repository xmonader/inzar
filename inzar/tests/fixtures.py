from models import db
from models import *
from faker import Faker

fake = Faker()


def generate_fixtures():
    global db
    db.session.commit()
