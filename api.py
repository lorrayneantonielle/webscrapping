import main
from flask import Flask
app = Flask(__name__)

response = main.j
print(response)

@app.route('/')
def hello_world():
    return response