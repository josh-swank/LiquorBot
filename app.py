# TODO: Logging


import bot
from flask import Flask


pyBot = bot.Bot()
slack = pyBot.client

app = Flask(__name__)


@app.route("/install", methods=["GET"])
def pre_install():
    raise NotImplementedError()


@app.route("/thanks", methods=["GET", "POST"])
def thanks():
    raise NotImplementedError()


@app.route("/listening", methods=["GET", "POST"])
def hears():
    raise NotImplementedError()


if __name__ == '__main__':
    app.run(debug=True)
