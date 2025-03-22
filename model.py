from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TranslatedRecipeName = db.Column(db.String(255), nullable=False)
    TranslatedIngredients = db.Column(db.Text, nullable=False)
    TotalTimeInMins = db.Column(db.Integer)
    Cuisine = db.Column(db.String(100))
    TranslatedInstructions = db.Column(db.Text)
    URL = db.Column(db.String(255))
    Cleaned_Ingredients = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    Ingredient_count = db.Column(db.Integer)
    Hero_Ing = db.Column(db.String(255))
