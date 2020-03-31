import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.console.models import Serie
from my_app import api, db

serie = Blueprint('serie', __name__)

parser = reqparse.RequestParser()
parser.add_argument('serie_title', type=str)
parser.add_argument('gender', type=str)
parser.add_argument('total_seasons', type=int)
parser.add_argument('avg_imdb', type=float)
parser.add_argument('status', type=str)

@serie.route("/")
@serie.route("/home")

def home():
    return "Catálogo de Series"

class SerieAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            series = Serie.query.paginate(page, 10).items
        else:
            series = [Series.query.get(id)]
        if not series:
            abort(404)
        res = {}
        for ser in series:
            res[ser.id] = {
                'serie_title' : ser.serie_title,
                'gender' : ser.gender,
                'total_seasons' : ser.total_seasons,
                'avg_imdb' : str(ser.avg_imdb),
                'status' : ser.status
            }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        serie_title = args['serie_title']
        gender = args['gender']
        total_seasons = args['total_seasons']
        avg_imdb = args['avg_imdb']
        status = args['status']

        ser = Serie(serie_title,gender,total_seasons, avg_imdb, status)
        db.session.add(ser)
        db.session.commit()
        res = {}
        res[ser.id] = {
                'serie_title' : ser.serie_title,
                'gender' : ser.gender,
                'total_seasons' : ser.total_seasons,
                'avg_imdb' : str(ser.avg_imdb),
                'status' : ser.status
            }
        return json.dumps(res)

    def delete(self, id):
        con =  Serie.query.get(id)
        db.session.delete(con)
        db.session.commit()
        res = {"id" : id}
        return json.dumps(res)

    def put(self,id):
        con =  Serie.query.get(id)
        args = parser.parse_args()
        serie_title = args['serie_title']
        gender = args['gender']
        total_seasons = args['total_seasons']
        avg_imdb = args['avg_imdb']
        status = args['status']

        con.serie_title = serie_title
        con.gender = gender
        con.total_seasons = total_seasons
        con.avg_imdb = avg_imdb
        con.status = status
        db.session.commit()
        res = {}
        res[con.id] = {
            "serie_title" : con.serie_title,
            "gender" : con.gender,
            "total_seasons" : con.total_seasons,
            "avg_imdb" : str(con.avg_imdb),
            "status" : con.status
        }

        return json.dumps(res)

api.add_resource(
    SerieAPI,
    '/api/serie',
    '/api/serie/<int:id>',
    '/api/serie/<int:id>/<int:page>'
)