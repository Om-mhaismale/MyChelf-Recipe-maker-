import mysql.connector
import pandas as pd

# MySQL Database Connection
db_config = {
    'host': 'localhost',  
    'user': 'root',
    'password': 'IllidanMagma44!',
    'database': 'recipe_db'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

df = pd.read_csv("cleaned_recipe.csv")  

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO recipes 
        (TranslatedRecipeName, TranslatedIngredients, TotalTimeInMins, Cuisine, 
         TranslatedInstructions, URL, Cleaned_Ingredients, image_url, Ingredient_count, Hero_Ing, Veg_Nonveg, Is_Veg) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("✅ CSV data imported successfully into MySQL!")
