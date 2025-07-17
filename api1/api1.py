from flask import Flask, jsonify, request
import requests
import os



def create_api1_app():
    app = Flask(__name__)
    app.logger.info("api1 start")

    API2_URL = os.environ.get('API2_URL', 'http://api2:5001/')

    @app.route('/')
    def hello_api1():
        app.logger.info("user send ---> api")
        app.logger.info(f"api1 send request to api2")
        response = requests.get(API2_URL)
        response.raise_for_status() 
        api2_response = response.json()
        app.logger.info(f"api1 get response from api2: {api2_response}")
        return jsonify({"api1:": "hello i am api1", "api2_data": api2_response['message']})

    return app
