import bot
from flask import Flask


pyBot = bot.Bot()
slack = pyBot.client


app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
