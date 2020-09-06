from neynpy import impl

VALIDATION_ERRORS = {
    'ip_type': 'ip must be string, default: "0.0.0.0"',
    'port_type': 'port can be int and string, default: 9090',
    'timeout_type': 'timeout can be int and string, default: 0',
    'router_type': 'router must be instance of "neynpy.core.route.Router"',
    'response_type': 'response must be instance of "neynpy.http.response.Response"',
    'http_methods': 'At this level you can only use GET, POST, PUT, PATCH, DELETE',
    'header_type': 'header must be dictionary',
    'path_type': 'path must be string',
    'methods_type': 'methods must be a list of strings, example: ["GET", "POST"]',
}

# This will be complete
ALLOW_HTTP_METHODS = ['GET', 'POST', 'DELETE', 'PUT', 'PATCH']


STATUS_OK = 200
STATUS_CREATED = 201
STATUS_NOT_FOUND = 404
STATUS_METHOD_NOT_AVAILABLE = 405
# TODO: add more status

status = impl.Response().Status
STATUS_DEFAULT = status.OK

STATUS_CODE = {
    STATUS_OK: status.OK,
    STATUS_CREATED: status.Created,
    STATUS_NOT_FOUND: status.NotFound,
    STATUS_METHOD_NOT_AVAILABLE: status.MethodNotAllowed,
}
