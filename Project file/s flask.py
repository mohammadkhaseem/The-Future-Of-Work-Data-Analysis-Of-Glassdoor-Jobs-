from flask import Flask, render_template, request


financial = Flask(__name__) # initializng the flask app


@financial.route('/')
def helloworld():
    return render_template("index.html")

if __name__ == '__main__':
    financial.run(debug = False, port = 5000)