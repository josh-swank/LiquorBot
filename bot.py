from slackclient import SlackClient


class Bot(object):
    def __init__(self):
        super(Bot, self).__init__()
        self.name = "liquorbot"

        self.client = SlackClient("")
