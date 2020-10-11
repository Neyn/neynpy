import os

from neynpy import impl

from neynpy.utils import const, exceptions


class Response:
    """
    An HTTP response base class
    more todo ...
    """
    def __init__(self, text, status_code=None, header=None, is_file=False):
        if header is None:
            header = {'Content-Type': 'text/html'}
        if status_code is None:
            status_code = const.STATUS_Ok
        self.text = text
        self.status_code = status_code
        self.header = header
        self.is_file = is_file

    @staticmethod
    def validate_response(response):
        if not isinstance(response, Response):
            raise exceptions.ValidationError(message=const.VALIDATION_ERRORS.get('response_type'))

    def new_response(self, res):
        self.validate_response(res)

        _res = impl.Response()
        _res.body = res.text
        _res.status = const.STATUS_CODE.get(res.status_code, const.STATUS_DEFAULT)
        _res.header = res.header
        if res.is_file:
            file_status = _res.open(os.path.join(const.BASE_PATH, res.text))
            if not file_status:
                _res.body = 'file not found'
        return _res

    def serialize_headers(self):
        pass

    def set_cookie(self):
        pass

    def delete_cookie(self):
        pass


class Serve:
    def __init__(self, root):
        self.filer = impl.Filer()
        self.filer.root = root

    def new_response(self):
        return self.filer.handle
