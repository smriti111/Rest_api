from db import db
class StoreModel(db.Model):
    __tablename__='stores'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))
    items=db.relationship('ItemModel',lazy='dynamic')

    def __init__(self,name):    #represents an object and not a dictionary
        self.name=name
     

    def json(self):
        return{'name':self.name,'items':[item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()#select * from table_name where name=? only the first row
     


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
     
