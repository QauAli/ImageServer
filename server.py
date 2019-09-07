
from flask import Flask
from flask_restful import Api
from applicant import Applicant, Images

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

api.add_resource(Applicant,'/new')
api.add_resource(Images,'/images/1.png')

if __name__ == '__main__':
    app.run( host='0.0.0.0')
    