from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins" : "*"
    }
})

@app.route('/get_locations')
def get_locations() :
    response = jsonify({
        'locations' : util.get_location_names()
    })

    return response

@app.route('/get_price',methods=['POST'])
def get_price() :
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price' : util.get_estimated_price(location,total_sqft,bath,bhk)
    })

    return response


if __name__ == "__main__" :
    print('Real_Estate_Price_Prediction')
    util.load_saved_artifacts()
    app.run()