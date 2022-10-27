from flask import Blueprint, jsonify, render_template, request


from ..extensions import mongo

from pprint import pprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    user_collection = list(mongo.db.users.find())
    # print(list(mongo.db.list_collection_names()))
    player_collection = list(mongo.db.players.find())
    return render_template('home.html', players = player_collection)

@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        pprint(request.form["username"])


    return render_template('login.html')

@main.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        pprint(request.form)
        

    return render_template('register.html')