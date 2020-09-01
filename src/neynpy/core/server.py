from neynpy.neynpy import impl
from neynpy.utils import exceptions, const


class Server:
    def __init__(self, *args, **kwargs):
        self.validate_kwargs(**kwargs)
        self.server = impl.Server()
        self.dummy = 10
        self.server.handler = self.handler
        self.config_server(*args, **kwargs)

    @staticmethod
    def validate_kwargs(**kwargs):
        ip = kwargs.get('ip', '0.0.0.0')
        port = kwargs.get('port', 9090)
        timeout = kwargs.get('timeout', 0)
        if not isinstance(ip, str):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('ip_type'))
        if not isinstance(port, str) and not isinstance(port, int):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('port_type'))
        if not isinstance(timeout, str) and not isinstance(timeout, int):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('timeout_type'))

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

    def handler(self, req):
        # print(self.dummy)
        # print(req.header)
        # print(req.path)

        res = impl.Response()
        res.body = "Hello World, NeynPy"
        return res

    def run(self):
        self.server.run()
