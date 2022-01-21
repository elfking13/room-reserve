from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY']= 'ROOMRESERVATION1group17kejundaryltommy'

    from .interface import interface
    from .auth import auth
    

    app.register_blueprint(interface, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    

    return app