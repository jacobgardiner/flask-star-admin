# -*- encoding: utf-8 -*-


from apps import db

class Characters(db.Model):
        
    __tablename__ = 'Characters'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    owner_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=True)
    character_id = db.Column(db.Integer, unique=True)
    access_token = db.Column(db.String(64))
    refresh_token = db.Column(db.String(64))
    token_expiry = db.Column(db.String(64)) # This might need converting to DateTime https://docs.sqlalchemy.org/en/20/core/types.html
    scopes = db.Column(db.String(64)) # This might be an array. JSON type? https://docs.sqlalchemy.org/en/20/core/types.html

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)


    def __repr__(self):
        return str(self.name)