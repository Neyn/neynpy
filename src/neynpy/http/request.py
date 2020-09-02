from neynpy.utils import exceptions, const


class Request:
    def __init__(self, *args, **kwargs):
        self.method = None
        self.header = None
        self.path = None

    def new_request(self, req):
        params = {
            'method': req.method,
            'header': req.header,
            'path': req.path
        }
        self.validate_params(**params)
        self.populate_params(**params)
        return self

    @staticmethod
    def validate_params(**kwargs):
        method = kwargs.get('method', '').upper()
        header = kwargs.get('header', None)
        path = kwargs.get('path', None)

        if method not in const.ALLOW_HTTP_METHODS:
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('http_methods'))

        if not isinstance(header, dict):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('header_type'))

        if not isinstance(path, str):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('path_type'))

    def populate_params(self, *args, **kwargs):
        self.method = kwargs.get('method')
        self.header = kwargs.get('header')
        self.path = kwargs.get('path')
