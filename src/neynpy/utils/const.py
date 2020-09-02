VALIDATION_ERRORS = {
    'ip_type': 'ip must be string, default: "0.0.0.0"',
    'port_type': 'port can be int and string, default: 9090',
    'timeout_type': 'timeout can be int and string, default: 0',
    'router_type': 'router must be instance of "neynpy.core.route.Router"',
    'response_type': 'response must be instance of "neynpy.http.response.Response"',
    'http_methods': 'At this level you can only use GET, POST, PUT, PATCH, DELETE',
    'header_type': 'header must be dictionary',
    'path_type': 'path must be string',
}

# This will be complete
ALLOW_HTTP_METHODS = ['GET', 'POST', 'DELETE', 'PUT', 'PATCH']
