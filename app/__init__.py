from flask import Flask
from .extensions import db, migrate
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes.main import main_bp

        from .routes.chapters import chapters_bp
        from .routes.characters import characters_bp
        from .routes.creatures import creatures_bp
        from .routes.events import events_bp
        from .routes.factions import factions_bp
        from .routes.items import items_bp
        from .routes.locations import locations_bp
        from .routes.plots import plots_bp
        from .routes.relationships import relationships_bp
        from .routes.systems import systems_bp
        from .routes.worlds import worlds_bp

        app.register_blueprint(main_bp)

        app.register_blueprint(characters_bp)
        app.register_blueprint(chapters_bp)
        app.register_blueprint(creatures_bp)
        app.register_blueprint(events_bp)
        app.register_blueprint(factions_bp)
        app.register_blueprint(items_bp)
        app.register_blueprint(locations_bp)
        app.register_blueprint(plots_bp)
        app.register_blueprint(relationships_bp)
        app.register_blueprint(systems_bp)
        app.register_blueprint(worlds_bp)

        db.create_all()

    return app
