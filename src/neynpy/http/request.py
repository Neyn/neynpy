from neynpy.utils import exceptions, const


class Request:
    """
    Request class to match all binding request
    To python version and also add some other high level item
    """
    def __init__(self, *args, **kwargs):
        self.method = None
        self.header = None
        self.path = None
        self.body = None
        self.address = None
        self.address_port = None
        self.major = None
        self.minor = None

    def new_request(self, req):
        params = {
            'method': req.method,
            'header': req.header,
            'path': req.path,
            'body': req.body,
            'address': req.address,
            'major': req.major,
            'address_port': req.port,
            'minor': req.minor,
        }
        self.validate_params(**params)
        self.populate_params(**params)
        return self

    @staticmethod
    def validate_params(**kwargs):
        method = kwargs.get('method', '').upper()
        header = kwargs.get('header', None)
        path = kwargs.get('path', None)

        if method not in const.ALLOWED_HTTP_METHODS:
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('http_methods'))

        if not isinstance(header, dict):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('header_type'))

        if not isinstance(path, str):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('path_type'))

    def populate_params(self, *args, **kwargs):
        self.method = kwargs.get('method')
        self.header = kwargs.get('header')
        self.path = kwargs.get('path')
