# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

# Import Other stuff
import os
import markdown
import shelve
import secrets
import json
# Create an instance of Flask
app = Flask(__name__)
api = Api(app)
CORS(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("characters.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g,'_database',None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    """Present some Documentation"""

    # open the README file
    with open(os.path.dirname(app.root_path) + "/README.md","r") as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        #Convert to HTML
        return markdown.markdown(content)

class CharacterList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        characters = []

        for key in keys:
            characters.append(shelf[key])
        return {
            'message': 'Success',   
            'data': characters
        }
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("name",required=True)
        parser.add_argument("stats", required=True)

        args = parser.parse_args()

        shelf = get_db()
        token = secrets.token_urlsafe()
        while token in shelf:
            token = secrets.token_urlsafe()
        args["identifier"] = token
        shelf[token] = args

        return {
            "message": 'Character registered',
            'data': args
        }

class Character(Resource):
    def get(self,identifier):
        shelf = get_db()

        # If the key does not exist in the data store return a 404 error
        if not (identifier in shelf):
            return {'message': "Character not found","data": {}}, 404
        
        return {"message": "Character found", 'data': shelf[identifier]},200

    def delete(self, identifier):
        shelf = get_db()

         # If the key does not exist in the data store return a 404 error
        if not (identifier in shelf):
            return {'message': "Character not found","data": {}}, 404
        
        del shelf[identifier]
        return '', 204

api.add_resource(CharacterList, '/characters')
api.add_resource(Character,"/character/<string:identifier>")