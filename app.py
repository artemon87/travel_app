from flask import Flask
from flask_restful import Api
from app_resources.resources import Calculate


trip_app = Flask(__name__)
trip_app.config.from_object('app_resources.config.DevelopmentConfig')
api = Api(trip_app)
api.add_resource(Calculate, '/v1/calculate')


if __name__ == '__main__':
    trip_app.run(host='0.0.0.0', port=8005)