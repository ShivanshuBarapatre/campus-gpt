from routes.user import user_bp
from flask import Flask
from flask_cors import CORS
from config import db
from routes.chat import chat_bp
from routes.leaderboard import leaderboard_bp

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campusgpt.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(chat_bp)
app.register_blueprint(user_bp)
app.register_blueprint(leaderboard_bp)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "CAMPUS GPT backend running"}

if __name__ == "__main__":
    app.run(debug=True)
