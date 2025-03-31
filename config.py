import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:1234@localhost/recipe_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
