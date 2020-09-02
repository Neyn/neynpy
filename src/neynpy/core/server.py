from neynpy.http.response import Response
from neynpy.http.request import Request
from neynpy.neynpy import impl
from neynpy.utils import exceptions, const
from neynpy.core.route import Router


class Server:
    def __init__(self, *args, **kwargs):
        self.validate_kwargs(**kwargs)
        self.server = impl.Server()
        self.dummy = 10
        self.server.handler = self.handler
        self.config_server(*args, **kwargs)
        self.router = kwargs.get('router')

    @staticmethod
    def validate_kwargs(**kwargs):
        ip = kwargs.get('ip', '0.0.0.0')
        port = kwargs.get('port', 9090)
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

    @staticmethod
    def validate_response(response):
        if not isinstance(response, Response):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('response_type'))

    def config_server(self, *args, **kwargs):
        ip = kwargs.get('ip', '0.0.0.0')
        port = int(kwargs.get('port', 9090))
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

    def make_response(self, response):
        self.validate_response(response)

        res = impl.Response()
        res.body = response.text
        # res.status = response.status_code
        res.header = response.header
        return res

    def handler(self, req):
        response = self.router.get_handler(req.path)(self.make_request(req))
        return self.make_response(response)

    def run(self):
        self.server.run()
