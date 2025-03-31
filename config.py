import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("postgres://neondb_owner:npg_mdL80gpntTaF@ep-square-term-a1703bo7-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require")  # Load from environment variable
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
