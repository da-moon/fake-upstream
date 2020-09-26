
from .. import __version__


SWAGGER_CONFIG = {
    'title': 'nginx upstream backend service',
    'description':
        'Webserver used as nginx upstream backend to help with observing how proxy_pass module affects requests . Use this service at your own risk.',
    'version': __version__,
    'hide_top_bar': True,
    'uiversion': 3
}
