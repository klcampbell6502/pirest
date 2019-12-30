from flask import Flask
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

class ScreenOff(Resource):
    def get(self):
        os.system("vcgencmd display_power 0")
        
class ScreenOn(Resource):
    def get(self):
        os.system("vcgencmd display_power 1")
        
api.add_resource(ScreenOff,'/screen/off')
api.add_resource(ScreenOn,'/screen/on')

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')
