from db import db


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column()


# https://www.youtube.com/watch?v=zMhmZ_ePGiM&t=6s