from my_app import db

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serie_title = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    total_seasons = db.Column(db.Integer)
    avg_imdb = db.Column(db.Float(asdecimal=True))
    status = db.Column(db.String(8))

    def __init__(self,serie_title,gender,total_seasons, avg_imdb, status):
        self.serie_title = serie_title
        self.gender = gender
        self.total_seasons = total_seasons
        self.avg_imdb = avg_imdb
        self.status = status

    def __repr__(self):
        return 'Serie {0}'.format(self.id)