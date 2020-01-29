from flask import Response


class SearcherApiResponse(Response):
    charset = 'utf-8'
    default_status = 200
    default_mimetype = 'application/json'

    def __init__(self,
                 response=None,
                 status=None,
                 headers=None,
                 mimetype=None,
                 content_type=None,
                 direct_passthrough=False):

        super().__init__(
            response,
            status,
            headers,
            mimetype,
            content_type,
            direct_passthrough
        )
