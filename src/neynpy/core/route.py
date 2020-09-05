from neynpy.http.response import Response
from neynpy.utils import const


class Router:
    """
    Router class will add some handler and manage them
    After a while will support methods control also
    Serving files and etc
    """
    def __init__(self):
        self.routes = {}

    @staticmethod
    def clean_path(path):
        if not path.endswith('/'):
            return path + '/'
        return path

    def add_handler(self, path, handler):
        """
        :param path: the path of routing
        :param handler: the handler function of the path
        :return:
        """
        path = self.clean_path(path)
        self.routes[path] = handler

    def get_handler(self, path):
        """
        get_handler return the handler function of input path
        :param path: the path to be returned
        :return: handler function or None
        """
        path = self.clean_path(path)
        return self.routes.get(path, self.default_404)

    @staticmethod
    def default_404(req):
        """
        The default 404 page if no path found
        :return: Response('not found', 404)
        """
        return Response('not found', const.STATUS_NOT_FOUND)
