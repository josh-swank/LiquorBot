# TODO: Logging


import bot
from flask import Flask, render_template


pyBot = bot.Bot()
slack = pyBot.client

app = Flask(__name__)


@app.route("/install", methods=["GET"])
def pre_install():
    client_id = pyBot.oauth['client_id']
    scope = pyBot.oauth['scope']
    return render_template("install.html", client_id=client_id, scope=scope)


@app.route("/thanks", methods=["GET", "POST"])
def thanks():
    raise NotImplementedError()


@app.route("/listening", methods=["GET", "POST"])
def hears():
    raise NotImplementedError()


if __name__ == '__main__':
    app.run(debug=True)
