# TODO: Logging


import bot
from flask import Flask, make_response, render_template, request
import json
import re


pyBot = bot.Bot()
app = Flask(__name__)

word_pattern = re.compile("\\b[a-z]+(?:qu|[^aeiou])[eo]r\\b")


def _handle_event(event_type, slack_event):
    if event_type == 'message' and slack_event['event'].get('text'):
        user_id = slack_event['event'].get('user')
        message = slack_event['event'].get('text')
        matches = re.findall(word_pattern, message)

        if len(matches) > 0:
            response_text = "%s?! I HARDLY EVEN KNOW 'ER!" % matches[0].upper()
            pyBot.post_message(slack_event['event'].get('channel'), response_text)
            return make_response("Message response posted", 200)

    message = "Unable to handle event %s" % event_type
    return make_response(message, 200, {'X-Slack-No-Retry': 1})


@app.route("/install", methods=["GET"])
def pre_install():
    client_id = pyBot.oauth['client_id']
    scope = pyBot.oauth['scope']
    return render_template("install.html", client_id=client_id, scope=scope)


@app.route("/thanks", methods=["GET", "POST"])
def thanks():
    code_arg = request.args.get('code')
    pyBot.auth(code_arg)
    return render_template("thanks.html")


@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)

    # Slack URL Verification
    if 'challenge' in slack_event:
        return make_response(slack_event['challenge'],
                200, {'content_type': 'application/json'})

    # Slack Token Verification
    if pyBot.verification != slack_event.get('token'):
        message = "Invalid Slack verification token: %s\npyBot has: %s\n\n" \
                % (slack_event['token'], pyBot.verification)
        make_response(message, 403, {'X-Slack-No-Retry': 1})
    
    # Process Incoming Events from Slack
    if 'event' in slack_event:
        event_type = slack_event['event']['type']
        return _handle_event(event_type, slack_event)

    return make_response("No event in Slack request",
            404, {'X-Slack-No-Retry': 1})


if __name__ == '__main__':
    app.run(debug=True)
