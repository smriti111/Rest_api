import sqlite3
from flask import Flask
from flask_restful import reqparse,Resource
from flask_jwt import  jwt_required
from Models.item import ItemModel


class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price', 
    type=float,
    required=True,
    help='This field cannot be left blank'
        )
    parser.add_argument('store_id', 
    type=int,
    required=True,
    help='Store Id cannot be left blank'
        )

    @jwt_required()
    def get(self, name):
        item=ItemModel.find_by_name(name)
    
        if item:
            return item.json()   #item is an object and we have to return a dictionary
        
        return{'message':'item not found'},404
    
    


    def post(self, name):
        if (ItemModel.find_by_name(name)):
            return {'message':"item '{}'is already present".format(name)},400
        data=Item.parser.parse_args()
        item=ItemModel(name,data['price'],data['store_id'])
        try:
            item.save_to_db()
        except:
            return{'message':'an error occured while insering the item'},500
        return {'item':item.json() },201


        

    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return{'message':'item deleted'},201
        
    
    def put(self,name):
        data=Item.parser.parse_args()
        item=ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])   #**data
    

        else:
           item.price=data['price']
        item.save_to_db()

        return item.json()
    






class Item_list(Resource):
    def get(self):
     return {'items':list(map(lambda x: x.json(),ItemModel.query.all()))}
