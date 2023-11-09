from flask import request
import logging

def hello_controller():
    return "<p>Hello, World!</p>"

def test_controller():
    return "<p> Test </p>"

def run_controller():
    return "<p> Run </p>"

def create_Controller():
    jsonData = request.get_json()
    return f"<p> {jsonData} </p>"