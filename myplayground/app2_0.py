#!/usr/bin/python3
from flask import Flask, request
from db import states, cities
import uuid


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello World!"


@app.post('/states')
def create_state():
    state_data = request.get_json()
    state_id = uuid.uuid4().hex
    state = {**state_data, "id": state_id}
    states[state_id] = state

    return state


@app.get('/states')
def get_states():
    return {"states": list(states.values())}

@app.post('/city')
def create_city():
    city_data = request.get_json()
    if city_data["id"] not in states:
        return {"Message": "State not found"}, 404
    city_id = uuid.uuid4().hex
    city = {**city_data, "id": city_id}
    cities[city_id] = city

    return city

@app.get('/cities')
def get_cities():
    return {"cities": list(cities.values())}

@app.get('/state/<string:state_id>')
def get_state(state_id):
    try:
        return states[state_id]
    except KeyError:
        return {"Message": "State not found"}, 404

@app.get('/city/<string:city_id>')
def get_city(city_id):
    try:
        return cities[city_id]
    except KeyError:
        return {"Message": "City not found"}, 404

@app.delete('/state/<string:state_id>')
def delete_state(state_id):
    try:
        del states[state_id]
        return {"Message": "State deleted"}
    except KeyError:
        return {"Message": "State not found"}, 404

@app.delete('/city/<string:city_id>')
def delete_city(city_id):
    try:
        del cities[city_id]
        return {"Message": "City deleted"}
    except KeyError:
        return {"Message": "City not found"}, 404

@app.put('/state/<string:state_id>')
def update_state(state_id):
    state_data = request.get_json()
    try:
        state = states[state_id]
        state |= state_data
        return state
    except KeyError:
        return {"Message": "State not found"}, 404

@app.put('/city/<string:city_id>')
def update_city(city_id):
    city_data = request.get_json()
    try:
        city = cities[city_id]
        city |= city_data
        return city
    except KeyError:
        return {"Message": "City not found"}, 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
