import os
import traceback
import requests
import datetime

def log_event(name, params):
    _write_to_es(name, params, 'events')

def log_error(name, params):
    params['traceback'] = traceback.format_exc()
    _write_to_es(name, params, 'errors')

def _write_to_es(name, params, type):
    params = _curate(params)
    params['name'] = name
    params['app'] = os.environ['APP_NAME'] if 'APP_NAME' in os.environ else None
    params['timestamp'] = datetime.datetime.utcnow().isoformat()
    
    try:
        url = '{}/{}_{}_{}/{}'.format(os.environ['ES_URI'] if 'ES_URI' in os.environ else 'http://127.0.0.1:9200',
                                      os.environ['ES_INDEX_PREFIX'] if 'ES_INDEX_PREFIX' in os.environ else 'prod',
                                      type,
                                      datetime.datetime.utcnow().strftime("%Y_%m"),
                                      "_doc")
        r = requests.post(url, json = params)
        print('Logging to elasticsearch - {}, {}: {}'.format(r.status_code, r.reason, r.text))
    except:
        print('Failed to log {}: {}'.format(type, params))

def _curate(params):
    new_params = {}
    for key in params:
        new_params[key] = str(params[key])
    return new_params
