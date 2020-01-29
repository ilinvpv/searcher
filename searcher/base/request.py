import random
from flask import Request, current_app, request
from werkzeug import cached_property


class SearcherApiRequest(Request):
    def _get_request_arg(self, name):
        if request.args.get(name, None):
            return request.args[name]
        json_body = request.get_json(silent=True)
        if json_body:
            return json_body.get(name, None)

    def get_header_from_config(self, name, default=None):
        name = name.upper()
        header_name = getattr(current_app.configuration, f'{name}_HEADER', name)
        return self.headers.get(header_name, default)

    @cached_property
    def request_id(self):
        return str(random.randint(0, 999999999))

    @property
    def remote_addr(self):
        return self.headers.get('X-Real-IP', super().remote_addr)

    @cached_property
    def language(self):
        return self.get_header_from_config('Accept-Language')
