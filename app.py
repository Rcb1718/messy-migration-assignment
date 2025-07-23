from flask import Flask
from db import db, init_db
from routes.user_routes import user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_db(app)

app.register_blueprint(user_bp)

@app.route('/')
def health():
    return {'message': 'Healthy'}, 200

if __name__ == '__main__':
    app.run(debug=True)