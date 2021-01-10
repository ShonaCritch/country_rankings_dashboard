from rankingsdashboard.app import db

# db.drop_all()
db.create_all()

def create_app(cfg=None):
    app = Flask(__name__)
    from api.views import api
    app.register_blueprint(api)
    return app