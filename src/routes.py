from flask import jsonify, request
from src import app, db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from src import utils
from src.models import User, Courses

@app.route('/')
def index():  # put application's code here
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return jsonify({"message": "welcome"})


@app.route('/register', methods=['POST'])
def register():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    data = request.get_json()
    if request.method == 'POST':
        password_hash = generate_password_hash(data["password"])
        user = User(username=data["username"],
                    password=password_hash,
                    name=data["name"],
                    email=data["email"],
                    )
        if User.query.filter_by(username=data["username"]).first():
            return jsonify({"message": "This username is taken! Try Using other username."}), 401
        if User.query.filter_by(email=data["email"]).first():
            return jsonify({"message": "Email address already in use !"}), 401
        

        db.session.add(user)
        db.session.commit()

        token = jwt.encode({"public_id": user.id}, app.config["SECRET_KEY"])
        return jsonify({"message": "User Created Successfully", "token": token.decode("utf-8")}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if request.method == 'POST':
        if not data.get('username'):
            return jsonify({"message": "Username is missing !"}), 401
        if not data.get('password'):
            return jsonify({"message": "Password is missing !"}), 401
        user = User.query.filter_by(username=data['username']).first()
        if not user:
            return jsonify({"message": "Incorrect Username or Password !"}), 404
        if not check_password_hash(user.password, data['password']):
            return jsonify({"message": "Incorrect Username or Password !"}), 404
        token = jwt.encode({"public_id": user.id}, app.config["SECRET_KEY"])
        return jsonify({"message": "Logged in successfully", "token": token.decode("utf-8")})



@app.route('/admin', methods=['GET', 'POST'])
@utils.token_required
def admin(current_user):
    return jsonify({"message": f"welcome {current_user.name}"})


@app.route('/add_course', methods=['GET', 'POST'])
@utils.token_required
def add_course():
    return jsonify({"message": "welcome"})
