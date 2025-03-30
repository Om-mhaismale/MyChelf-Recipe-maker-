from flask import Blueprint, request, jsonify
from model import Recipe, db

routes = Blueprint('routes', __name__)

@routes.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', 10))

    if not query:
        return jsonify({"error": "Please provide a search query."}), 400

    # Query with pagination
    results = Recipe.query.with_entities(
        Recipe.TranslatedRecipeName, Recipe.image_url, Recipe.Cuisine, 
        Recipe.TotalTimeInMins, Recipe.Ingredient_count, Recipe.URL, Recipe.Cleaned_Ingredients
    ).filter(
        (Recipe.Cleaned_Ingredients.like(f"%{query}%")) | 
        (Recipe.Hero_Ing.like(f"%{query}%"))
    ).offset(offset).limit(limit).all()

    if not results:
        return jsonify({"message": "No more recipes found."}), 404

    recipes = [
        {
            "name": r.TranslatedRecipeName,
            "cuisine": r.Cuisine,
            "time": r.TotalTimeInMins,
            "ingredients_count": r.Ingredient_count,
            "url": r.URL,
            "image_url": r.image_url,
            "ingredients": r.Cleaned_Ingredients  
        } for r in results
    ]

    return jsonify({"recipes": recipes})