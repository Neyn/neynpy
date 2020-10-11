import neynpy.impl as impl

from neynpy.core.route import Router
from neynpy.http.request import Request
from neynpy.http.response import Response, Serve
from neynpy.utils import exceptions, const


class Server:
    def __init__(self, *args, **kwargs):
        self.validate_kwargs(**kwargs)
        self.server = impl.Server()
        self.server.handler = self.handler
        self.config_server(*args, **kwargs)
        self.router = kwargs.get('router')

    @staticmethod
    def validate_kwargs(**kwargs):
        ip = kwargs.get('ip', '0.0.0.0')
        port = kwargs.get('port', 7070)
        timeout = kwargs.get('timeout', 0)
        router = kwargs.get('router', 0)
        if not isinstance(ip, str):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('ip_type'))
        if not isinstance(port, str) and not isinstance(port, int):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('port_type'))
        if not isinstance(timeout, str) and not isinstance(timeout, int):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('timeout_type'))
        if not isinstance(router, Router):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('router_type'))

    def config_server(self, *args, **kwargs):
        ip = kwargs.get('ip', '0.0.0.0')
        port = int(kwargs.get('port', 7070))
        timeout = int(kwargs.get('timeout', 0))

        config = impl.Config()
        config.address = ip
        config.port = port
        config.timeout = timeout

        self.server.config = config

        # Temporary
        print('neynpy run on: http://{}:{}'.format(ip, port))

    @staticmethod
    def make_request(req):
        return Request().new_request(req)

    @staticmethod
    def make_response(res, req):
        if isinstance(res, Response):
            return Response('').new_response(res=res)
        elif isinstance(res, Serve):
            return res.new_response()(req)

    def handler(self, req):
        response, path = self.router.get_handler(req)
        req.path = path
        response = response(self.make_request(req))
        return self.make_response(response, req)

    def run(self):
        self.server.run()
