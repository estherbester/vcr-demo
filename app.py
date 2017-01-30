import logging
import os
import sqlite3
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
DB = 'db.db'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, DB), SECRET_KEY='lolcatsrs0funny101!l', USERNAME='admin', PASSWORD='password1',
))


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


SUCCESS = 'w00t!'

@app.route('/users', methods=['POST'])
def get_user():
    logger.info('Log: Request made for user {}'.format(request.form['username']))
    return SUCCESS


@app.route('/results')
def show():
    """ just to show db """
    db = get_db()
    cur = db.execute('select id, title, text from entries order by id desc')
    entries = cur.fetchall()
    output = '<html><body><pre>ID    URL      Contents<br />'
    template_string = '{idx} |   {url}   |  {contents}<br />'
    for entry in entries:
        output += template_string.format(idx=entry[0],url=entry[1], contents=entry[2])
    output += '</pre>'
    return output


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run()