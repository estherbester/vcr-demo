import logging
import os
import requests
from flask import Flask, g, request


EXTERNAL_SERVICE_URL = 'http://localhost:5000/users'


def create_user(request):

    data = get_user_data_from_service(request.username)

    do_some_stuff_with_data(request, data)    

    return 'w00t!'


def get_user_data_from_service(username):
    params = {'username': username}
    result = requests.post(EXTERNAL_SERVICE_URL, data=params)
    return result.content


def do_some_stuff_with_data(username, data):
    pass


class Request(object):
    def __init__(self, username=None, profile=None, **kwargs):
        self.username = username
        self.profile = profile 





# the rest is just for the demo

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


SUCCESS = 'w00t!'

@app.route('/users', methods=['POST'])
def get_user():
    logger.info('Log: Request made for user {}'.format(request.form['username']))
    return SUCCESS

if __name__ == "__main__":
    app.run()