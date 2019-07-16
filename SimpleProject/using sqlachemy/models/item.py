from db import db

class ItemModel(db.Model):
    print("createddddddddddddddddddddddddddd") 

    __tablename__ = 'items'

    # DEFINE THE TABLE'S COLUMN
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    
    store = db.relationship('StoreModel')


    print("prinnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn") 

    def __init__(self, name, price, store_id):
        print("----------------init db---------------------") 
        self.name = name
        self.price = price
        store_id= self.store_id

    def json(self):
        return {'name':self.name, 'price':self.price }

    @classmethod
    def find_by_name(cls, name):
       print("333333333333333333333") 
       return cls.query.filter_by(name=name).first()              # this is sam with "SELECT * FROM items WHERE name=name LIMIT 1"

    def save_to_db(self):                                                          # def insert(self):
       db.session.add(self)
       db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

