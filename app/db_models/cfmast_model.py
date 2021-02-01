from app import db

class cfmast(db.Model):
    __tablename__ = "cfmast"

    id = db.Column(db.Integer,primary_key = True, autoincrement=True)
    name = db.Column(db.String(255), unique = True, nullable=False)

    def __repr__(self):
        return "<cfmast '{}'>".format(self.name)