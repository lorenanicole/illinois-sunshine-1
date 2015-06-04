from flask import Flask, render_template
from sunshine.views import views
from sunshine.api import api
from sunshine.models import bcrypt
from sunshine.auth import auth, login_manager

def create_app():
    app = Flask(__name__)
    config = '{0}.app_config'.format(__name__)
    app.config.from_object(config)
    app.register_blueprint(views)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(auth)

    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    
    return app