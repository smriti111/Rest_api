
from flask_restful import Resource
from Models.store import StoreModel


class Store(Resource):
    
    def get(self, name):
        item=StoreModel.find_by_name(name)
    
        if item:
            return{'items': item.json() }   #item is an object and we have to return a dictionary
        
        return{'message':'item not found'},404
    
    


    def post(self, name):
        if (StoreModel.find_by_name(name)):
            return {'message':"store '{}'is already present".format(name)},400
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return{'message':'an error occured while insering the item'},500
        return store.json() ,201


        

    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return{'message':'item deleted'},201


class Store_list(Resource):
    def get(self):
     return {'items':list(map(lambda x: x.json(),StoreModel.query.all()))}
