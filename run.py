
from paste.deploy import loadapp
from config.wsgi import application


def app_factory(global_config, **local_conf):
    return application

wsgi_app = loadapp('config:config.ini', relative_to='.')

