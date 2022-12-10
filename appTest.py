from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@ app.route('/', methods=['GET'])
def home():
    message = "Hello from this part of the digital world"
    return message


app.run()
