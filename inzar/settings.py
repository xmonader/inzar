import os

PRODUCTION = False
DBDIR = os.path.join(os.getcwd(), "db")
DBPATHDEV = os.path.join(os.getcwd(), "db", "development.db")
DBPATHPROD = os.path.join(os.getcwd(), "db", "production.db")
BOOTSTRAPWITHFIXTURES = os.getenv("BOOTSTRAPWITHFIXTURES", False)
RESETDB = os.getenv("RESETDB", False)
DBPATH = DBPATHDEV
BACKEND = "sqlite3"

if PRODUCTION is True:
    DBPATH = DBPATHPROD

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(DBPATH)
SQLALCHEMY_ECHO = True
SQLALCHEMY_RECORD_QUERIES = True

SECRET_KEY = "#!@#!@$!@ADASDASD02-3-112-9842*/$$%"

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))