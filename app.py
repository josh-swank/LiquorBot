import bot
from flask import Flask


pyBot = bot.Bot()
slack = pyBot.client

app = Flask(__name__)


@app.route("/install", methods=["GET"])
def pre_install():
    pass


@app.route("/thanks", methods=["GET", "POST"])
def thanks():
    pass


@app.route("/listening", methods=["GET", "POST"])
def hears():
    pass


if __name__ == '__main__':
    app.run(debug=True)
