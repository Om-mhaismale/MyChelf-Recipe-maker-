# MyChelf - Recipe Maker Web App

"MyChelf" is a recipe maker web app, if you are feeling alone and cooked sometimes then consider this app!

## Setting Up MyChelf Locally

Follow these steps to set up MyChelf on your local development environment:

1. **Install Virtual Environment:**
   ```
   pip install virtualenv
   ```

2. **Create a Virtual Environment:**
   ```
   virtualenv env
   ```

3. **Activate the Virtual Environment:**
   - On Windows (PowerShell):
     ```
     .\env\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```
     source env/bin/activate
     ```

4. **Install Flask and Dependencies:**
   ```
   pip install flask
   pip install flask-sqlalchemy
   ```

5. **Run the Application:**
   ```
   python app.py
   ```

Once you have completed these steps successfully, you can access MyChelf by navigating to http://localhost:5000 in your web browser.

## Features

- **Recipe Creation:** Easily create and save your own recipes.
- **Recipe Discovery:** Discover new recipes based on ingredients and preferences.
- **User Profiles:** Create a personalized profile to save and share your favorite recipes.

## Technologies Used

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **Jinja2**
- **HTML/CSS**
- **JavaScript**

## Contributing

Contributions are welcome! If you'd like to contribute to MyChelf, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
