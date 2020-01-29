from flask import Flask
from flask.globals import LocalProxy
from searcher.config import Configuration
from searcher.base import SearcherApiRequest, SearcherApiResponse


class SearcherFlaskApp(Flask):
    request_class = SearcherApiRequest
    response_class = SearcherApiResponse

    def __init__(self, name, strict_slashes=True, **kwargs):
        # Init flask app
        super().__init__(name, **kwargs)
        self.url_map.strict_slashes = strict_slashes


def create_app(config_class=Configuration):
    app = SearcherFlaskApp(__name__)
    app.config.from_object(config_class)
    app.secret_key = app.config.get('API_SECRET_KEY')

    from searcher.api.main import bp as main_bp
    app.register_blueprint(main_bp)

    return LocalProxy(lambda: app)
