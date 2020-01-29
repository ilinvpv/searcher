from flask import Blueprint
from covador import opt
from covador.flask import query_string

from searcher.serializers import ResultSchema


bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST', ], endpoint='main')
@query_string(q=opt(str, ''))
def main(q):
    fake_response = [
        {"title": "Most suitable title", "summary": "Short description 1"},
        {"title": "Less suitable title", "summary": "Short description 2"},
    ]
    return ResultSchema(many=True).dumps(fake_response)
