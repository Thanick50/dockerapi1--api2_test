from flask import Flask, jsonify

def create_api2_app():
    app = Flask(__name__)
    app.logger.info("api2 start")

    @app.route('/')
    def hello_api2():
        app.logger.info("api2 get request from api1")
        return jsonify({"message": "hello i am api2!!!"})

    return app