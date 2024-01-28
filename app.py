#!/usr/bin/env python

import flask
import summons
import random

app = flask.Flask(__name__)


@app.route('/')
def index():
    name, title = random.choice(list(summons.summons.items()))

    return flask.render_template('index.html', name=name, title=title)


if __name__ == '__main__':
    app.debug = True
    app.run()
