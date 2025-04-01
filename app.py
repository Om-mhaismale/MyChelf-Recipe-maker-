from flask import Flask, render_template
from config import Config
from model import db
from routes import routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(routes)

@app.route('/')
def home():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
