from flask import Flask, render_template, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

value = []

@app.route('/',  methods=['GET', 'POST'])
def index():
    print('reqyest')

    return {"" : ""}





if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)