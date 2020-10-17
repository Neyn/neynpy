from neynpy.core import route
from neynpy.http.response import Response
from neynpy.utils import const


def test_add_handler():
    path = '/'

    def view():
        return Response('ok')

    router = route.Router()

    router.add_handler(path, view)
    assert len(router.routes) == 1
    assert router.routes.get(path) == {'handler': view, 'methods': const.ALLOWED_HTTP_METHODS}
