from flask import Flask

app =  Flask(__name__)


@app.route('/')
def home():
    return f"This is the flask app!!!"


if __name__ == '__main__':
    app.run(debug=True)