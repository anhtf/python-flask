from flask import Flask
from flask_restful import Api, Resource
import json
app =   Flask(__name__)

api =   Api(app)

class returnjson(Resource):
    def get(self):
        data={
            "Name": "anhtdh@viettel.com.vn", 
            "Subject": "Embedded Software"
        }
        return data

api.add_resource(returnjson,'/returnjson')


if __name__=='__main__':
    app.run(debug=True)