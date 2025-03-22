from flask import Blueprint, request, jsonify
from model import Recipe, db

routes = Blueprint('routes', __name__)

@routes.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()
    sort_option = request.args.get('sort', '')
    cuisine_filter = request.args.get('cuisine', '')
    hero_filter = request.args.get('hero', '')
    
    if not query:
        return jsonify({"error": "Please provide a search query."}), 400

    # Base Query with Index Optimization
    results = Recipe.query.with_entities(
        Recipe.TranslatedRecipeName, Recipe.image_url, Recipe.Cuisine, Recipe.TotalTimeInMins, Recipe.Ingredient_count, Recipe.URL
    ).filter(
        (Recipe.TranslatedRecipeName.like(f"%{query}%")) |
        (Recipe.Cleaned_Ingredients.like(f"%{query}%"))
    )

    # Apply Filters
    if cuisine_filter:
        results = results.filter(Recipe.Cuisine == cuisine_filter)
    if hero_filter:
        results = results.filter(Recipe.Hero_Ing == hero_filter)

    # Apply Sorting
    sort_mapping = {
        "alpha": Recipe.TranslatedRecipeName,
        "time_asc": Recipe.TotalTimeInMins,
        "time_desc": Recipe.TotalTimeInMins.desc(),
        "ing_asc": Recipe.Ingredient_count,
        "ing_desc": Recipe.Ingredient_count.desc()
    }
    if sort_option in sort_mapping:
        results = results.order_by(sort_mapping[sort_option])

    # 🚀 Limit Results for Faster Response
    results = results.limit(20).all()

    if not results:
        return jsonify({"message": "No recipes found."}), 404

    # Reduce Response Size
    recipes = [
        {
            "name": r.TranslatedRecipeName,
            "cuisine": r.Cuisine,
            "time": r.TotalTimeInMins,
            "ingredients_count": r.Ingredient_count,
            "url": r.URL,
            "image_url": r.image_url
        } for r in results
    ]

    return jsonify({"recipes": recipes})
