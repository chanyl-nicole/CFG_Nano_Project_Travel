from flask import Flask

app = Flask(__name__)

#our endpoint/routes go in here


if __name__ == '__main__':
    app.run(debug=True, port=5001)