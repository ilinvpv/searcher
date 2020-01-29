import logging
from collections import Iterable
from inspect import getmembers
from typing import Iterator, Union

import pytest
from flask import url_for


class TestBase:
    endpoint = 'echo'
    fixtures = ('app', 'client', 'db_session', 'caplog')

    debug = False
    logging_levels = (logging.CRITICAL, logging.INFO)

    @pytest.fixture(autouse=True)
    def setup(self, request, app, db_session):
        for name in self._iter_fixture_names():
            setattr(self, name, request.getfixturevalue(name))
        stream_handler = next(filter(
            lambda h: isinstance(h, logging.StreamHandler),
            app.logger.handlers
        ), None)
        if stream_handler:
            stream_handler.setLevel(self.logging_levels[self.debug])

    @property
    def last_logging_message(self) -> str:
        return self.logging_messages[-1] if self.logging_messages else ''

    @property
    def logging_messages(self) -> list:
        if hasattr(self, 'caplog'):
            return [r.message for r in self.caplog.records]
        return []

    def _iter_fixture_names(self) -> Iterator[str]:
        for name, value in getmembers(self):
            if 'fixtures' not in name:
                continue
            if isinstance(value, str):
                value = {value}
            elif not isinstance(value, Iterable):
                continue
            yield from value

    def _send_request(self, endpoint: str = None, json=None, method='get',
                      raw_response=False, **params) -> Union[dict, 'Response']:
        url = url_for(endpoint or self.endpoint, _external=False, **params)

        if method == 'get':
            resp = self.client.get(url)
        elif method == 'put':
            resp = self.client.put(url, json=json or {})
        elif method == 'delete':
            resp = self.client.delete(url)
        elif method == 'post':
            resp = self.client.post(url, json=json or {})

        return resp if raw_response else resp.json

    def get(self, endpoint: str = None, **params) -> dict:
        return self._send_request(endpoint, method='get', **params)

    def post(self, endpoint: str = None, data=None, **params) -> dict:
        return self._send_request(endpoint, method='post', json=data, **params)

    def put(self, endpoint: str = None, data=None, **params) -> dict:
        return self._send_request(endpoint, method='put', json=data, **params)

    def delete(self, endpoint: str = None, **params) -> dict:
        return self._send_request(endpoint, method='delete', **params)
