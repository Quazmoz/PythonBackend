from flask import Flask
from flask_swagger import swagger

app = Flask(__name__)

@app.route('/swagger')
def generate_swagger_spec():
    swag = swagger(app)
    swag['info']['title'] = 'Your API'
    swag['info']['version'] = '1.0'
    return swag