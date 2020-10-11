from neynpy.http.response import Response
from neynpy.utils import const, exceptions


class Router:
    """
    Router class will add some handler and manage them
    After a while will support methods control also
    Serving files and etc
    """
    def __init__(self):
        self.routes = {}
        self.prefix_routes = {}

    @staticmethod
    def clean_path(path):
        if not path.endswith('/'):
            return path + '/'
        return path

    @staticmethod
    def clean_methods(methods):
        if not methods:
            methods = const.ALLOWED_HTTP_METHODS
        if not isinstance(methods, list):
            raise exceptions.ValidationError(const.VALIDATION_ERRORS.get('methods_type'))
        return [item.upper() for item in methods]

    def add_handler(self, path, handler, methods=None, prefix=False):
        """
        :param prefix: if route has to serve files
        :param path: the path of routing
        :param handler: the handler function of the path
        :param methods: specify the methods of this handler
        :return:
        """
        methods = self.clean_methods(methods)
        path = self.clean_path(path)

        if prefix:
            self.prefix_routes[path] = {'handler': handler, 'methods': methods}
        else:
            self.routes[path] = {'handler': handler, 'methods': methods}

    def _get_handler(self, req):
        path = req.path
        method = req.method
        path = self.clean_path(path)
        route = self.routes.get(path, None)
        if not route:
            for key, value in self.prefix_routes.items():
                if path.startswith(key):
                    path = path.replace(key, '/')[:-1]
                    route = value
        if not route:
            return self.default_404, path

        if method in route.get('methods', []):
            return route.get('handler'), path
        return self.default_405, path

    def get_handler(self, req):
        """
        get_handler return the handler function of input path
        :param req: the request of impl
        :return: handler function or None
        """

        return self._get_handler(req)

    @staticmethod
    def default_404(req):
        """
        The default 404 page if no path found
        :return: Response('not found', 404)
        """
        return Response('Not Found', const.STATUS_NotFound)

    @staticmethod
    def default_405(req):
        """
        The default 405 page if method not allowed
        :return: Response('Method Not Allowed', 405)
        """
        return Response('Method Not Allowed', const.STATUS_MethodNotAllowed)
