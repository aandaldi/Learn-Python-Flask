# MODELS.PY
# set up db inside the __init__.py under myproject folder

from myproject import db

class Puppies(db.Model):
    #
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primay_key=True)
    name = db.Column(db.Text)
    # using puppies, because table name is puppies
    owner = db.relationship('Owner', db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
    def __repr__(self):
        if self.owner:
            return f"Puppy Name is {self.name} and Owner is {self.owner.name}"
        else
            return "not any puppy"


class Owner(db.Model):
    #
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primay_key=True)
    name = db.Column(db.Text)
    # using puppies, because table name is puppies
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name {self.name}"


