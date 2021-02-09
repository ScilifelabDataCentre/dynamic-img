import flask
from flask_caching import Cache
from flask_cors import CORS

import Covid_portal_vis.Wordcloud.livewordcloud as lwc

app = flask.Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cors = CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/img/wordcloud_publications.png')
@cache.cached(timeout=10800)
def gen_wordcloud():
    img = lwc.gen_wordcloud()
    img.seek(0)
    return flask.send_file(img, mimetype='image/png')
