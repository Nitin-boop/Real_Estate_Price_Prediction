import json
import pickle
import numpy as np

__locations = None
__model = None
__columns = None

def get_estimated_price(location,sqft,bath,bhk) :
    try :
        _loc = __columns.index(location.lower())
    except :
        _loc = -1
    x = np.zeros(len(__columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if _loc :
        x[_loc] = 1

    return (round(__model.predict([x])[0],2))

def get_location_names() :
    return __locations

def load_saved_artifacts() :
    print('Loading artifacts')
    global __columns
    global __locations
    global __model

    with open("./artifacts/columns.json",'r') as f :
        __columns = json.load(f)['data_columns']
        __locations = __columns[3:]

    with open("./artifacts/bangalore_model.pickle",'rb') as f :
        __model = pickle.load(f)
    print('Loaded successfully')

if __name__ == "__main__" :
    load_saved_artifacts()
