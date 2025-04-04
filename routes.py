from flask import Blueprint, request, jsonify
from model import Recipe, db

routes = Blueprint('routes', __name__)

@routes.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', 10))
    veg_filter = request.args.get('veg_filter', 'all')  # Get veg/nonveg filter

    if not query:
        return jsonify({"error": "Please provide a search query."}), 400
    
    # Convert query into a list of ingredients
    ingredients_list = [ing.strip() for ing in query.split(",") if ing.strip()]

    if not ingredients_list:
        return jsonify({"error": "Invalid ingredient format."}), 400

    # Query with pagination
    recipe_query = Recipe.query.with_entities(
        Recipe.TranslatedRecipeName, Recipe.image_url, Recipe.Cuisine, 
        Recipe.TotalTimeInMins, Recipe.Ingredient_count, Recipe.URL, Recipe.Cleaned_Ingredients,
        Recipe.Is_veg
    )#.filter(
      #  (Recipe.Cleaned_Ingredients.like(f"%{query}%")) | 
       # (Recipe.Hero_Ing.like(f"%{query}%"))
    #)#.offset(offset).limit(limit).all() for testing purpose

    # Filter by each ingredient (AND logic)
    for ing in ingredients_list:
        recipe_query = recipe_query.filter(
            db.or_(
                Recipe.Cleaned_Ingredients.like(f"%{ing}%"),
                Recipe.Hero_Ing.like(f"%{ing}%")
            )
        )


    #Applying Veg/Nonveg filter
    if veg_filter == "veg":
        recipe_query = recipe_query.filter(Recipe.Is_veg == 1)
    elif veg_filter == "nonveg":
        recipe_query = recipe_query.filter(Recipe.Is_veg == 0)
    
    # Apply pagination
    results = recipe_query.offset(offset).limit(limit).all()

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
            "ingredients": r.Cleaned_Ingredients,
            "Is_veg": "Veg" if r.Is_veg == 1 else "Non-Veg"   
        } for r in results
    ]

    return jsonify({"recipes": recipes})