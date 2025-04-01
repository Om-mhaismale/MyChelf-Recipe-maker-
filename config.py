import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:IllidanMagma44!@localhost/recipe_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
