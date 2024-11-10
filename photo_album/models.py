from photo_album.app import db

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Photo {self.title}>'