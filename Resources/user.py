import sqlite3
from flask_restful import Resource,reqparse
from Models.user import UserModel


class Register_User(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username', 
    type=str,
    required=True,
    help='This field cannot be left blank'
        )
    parser.add_argument('password', 
    type=str,
    required=True,
    help='This field cannot be left blank'
        )
        
    
    def post(self):
        data=Register_User.parser.parse_args()
        if UserModel.find_by_user(data['username']):
            return{'message':"username :{} already exists".format(data['username'])}  
        user=UserModel(**data)     
      
        user.save_to_db()
      
        return{'message':"username registered successfully"},201




