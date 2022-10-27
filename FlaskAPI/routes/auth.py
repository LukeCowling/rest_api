from flask import Blueprint, render_template, request, redirect



from ..extensions import mongo

from pprint import pprint


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        pprint(request.form)
        

    return render_template('register.html')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        pprint(request.form["username"])


    return render_template('login.html')

@auth.route('/logout', methods=['POST'])
def logout():

    # Remove user from session
    return render_template(redirect("/login"))
