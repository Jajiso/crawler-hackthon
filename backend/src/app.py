from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://https://data.mongodb-api.com/app/data-qjjza/endpoint/data/beta'

mongo = PyMongo(app)

@app.route('/companies', methods=['POST'])
if __name__ == "__main__"
    app.run(debug=True)