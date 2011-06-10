import numpy as np
import flask
import settings

def json_float(val):
    if np.isnan(val) or np.isinf(val):
        return str(val)
    return val

def add_url_helpers(app):
    
    @app.context_processor
    def override_url_for():
        return dict(url_for=dated_url_for)

    def dated_url_for(endpoint, **values):
        if endpoint == 'static':
            filename = values.get('filename', None)
            return flask.url_for(endpoint, filename=filename)+"?"+str(settings.ASSET_TIME)
        return flask.url_for(endpoint, **values)
