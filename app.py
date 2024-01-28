#!/usr/bin/env python

import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html', name='JustinDe')


if __name__ == '__main__':
    app.debug = True
    app.run()
