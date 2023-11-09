from flask import Flask
from flask_queue import flask_queue
from controller import hello_controller,run_controller,test_controller,create_Controller

app = Flask(__name__)

@app.route("/")
def hello_world():
    flask_queue(hello_controller())
    return hello_controller()
    
@app.route('/test')
def test():
    flask_queue(test_controller())
    return test_controller()

@app.route('/run')
def test_run():
    flask_queue(run_controller())
    return run_controller()

@app.route('/create',methods = ['POST'])
def create():
    flask_queue(create_Controller())
    return create_Controller()