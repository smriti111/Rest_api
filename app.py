from flask import Flask
from flask_restful import Resource, Api
from security import authenticate,identity

from Resources.user import Register_User
from flask_jwt import JWT
from Resources.item import Item,Item_list
from Resources.store import Store, Store_list
    


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='something long and secure'
api=Api(app)



jwt=JWT(app,authenticate,identity)  #/auth
   
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Store_list, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Item_list, '/items')
api.add_resource(Register_User, '/register')
if __name__ == "__main__":

    app.run(port=5000,debug=True)
