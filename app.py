"""
Endpoints for generating dynamic images, e.g. plots.
"""
import logging

import flask
from flask_caching import Cache
from flask_cors import CORS

import livewordcloud as lwc

app = flask.Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cors = CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/wordcloud_<field>.png')
@cache.cached(timeout=86400)
def gen_wordcloud(field):
    if field in ('title', 'abstract'):
        img = lwc.gen_wordcloud(field)
    else:
        return flask.Response(status=404)
    img.seek(0)
    return flask.send_file(img, mimetype='image/png')


@app.route('/heartbeat')
def heartbeat():
    return flask.Response(status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
else:
    # Assume this means it's handled by gunicorn
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
