#!/usr/bin/python3
"""Start Flask web application"""

from flask import Flask, request

app = Flask(__name__)


states = [{"name": "Kenya", "cities": [{"name": "Nairobi"}]}]

@app.route('/', strict_slashes=False)
def hello():
    """
    Routing to root, strict_slashes ensure
    the URL works whether it ends with or without the /
    """
    return "Hello World!"


@app.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def get_or_create_states():
    if request.method == 'POST':
        # retrieve json content of our request
        request_data = request.get_json()
        # create new dictionary for our state
        new_state = {"name": request_data["name"], "cities": []}
        for state in states:
            if state["name"] == new_state["name"]:
                return {"error": f"{state['name']} already exists!"}
        states.append(new_state)
        return new_state, 201
    else:
        return {"states": states}


@app.post('/state/<string:name>/city')
def create_city(name):
    request_data = request.get_json()
    for state in states:
        if state["name"] == name:
            new_city = {"name": request_data["name"]}
            state["cities"].append(new_city)
            return new_city, 201
    return {"Message": f"The State {state['name']} not found!"}, 404


@app.get('/state/<string:name>/city')
def get_city_in_state(name):
    for state in states:
        if state["name"] == name:
            return {"cities": state["cities"]}
    return {"Message": f"The State {state['name']} not found!"}, 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
