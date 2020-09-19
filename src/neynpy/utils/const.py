import os

from neynpy import impl

VALIDATION_ERRORS = {
    'ip_type': 'ip must be string, default: "0.0.0.0"',
    'port_type': 'port can be int and string, default: 9090',
    'timeout_type': 'timeout can be int and string, default: 0',
    'router_type': 'router must be instance of "neynpy.core.route.Router"',
    'response_type': 'response must be instance of "neynpy.http.response.Response"',
    'http_methods': 'method not supported',
    'header_type': 'header must be dictionary',
    'path_type': 'path must be string',
    'methods_type': 'methods must be a list of strings, example: ["GET", "POST"]',
}

# This will be complete
ALLOWED_HTTP_METHODS = ['GET', 'HEAD', 'POST', 'DELETE', 'PUT', 'PATCH', 'CONNECT', 'OPTIONS', 'TRACE']

STATUS_Continue = 100
STATUS_SwitchingProtocols = 101
STATUS_Processing = 102
STATUS_Ok = 200
STATUS_Created = 201
STATUS_Accepted = 202
STATUS_NonAuthoritativeInformation = 203
STATUS_NoContent = 204
STATUS_ResetContent = 205
STATUS_PartialContent = 206
STATUS_MultiStatus = 207
STATUS_AlreadyReported = 208
STATUS_IMUsed = 226
STATUS_MultipleChoices = 300
STATUS_MovedPermanently = 301
STATUS_Found = 302
STATUS_SeeOther = 303
STATUS_NotModified = 304
STATUS_UseProxy = 305
STATUS_TemporaryRedirect = 307
STATUS_PermanentRedirect = 308
STATUS_BadRequest = 400
STATUS_Unauthorized = 401
STATUS_PaymentRequired = 402
STATUS_Forbidden = 403
STATUS_NotFound = 404
STATUS_MethodNotAllowed = 405
STATUS_NotAcceptable = 406
STATUS_ProxyAuthenticationRequired = 407
STATUS_RequestTimeout = 408
STATUS_Conflict = 409
STATUS_Gone = 410
STATUS_LengthRequired = 411
STATUS_PreconditionFailed = 412
STATUS_PayloadTooLarge = 413
STATUS_RequestURITooLong = 414
STATUS_UnsupportedMediaType = 415
STATUS_RequestedRangeNotSatisfiable = 416
STATUS_ExpectationFailed = 417
STATUS_ImATeapot = 418
# STATUS_MisdirectedRequest = 419
STATUS_UnprocessableEntity = 422
STATUS_Locked = 423
STATUS_FailedDependency = 424
STATUS_UpgradeRequired = 426
STATUS_PreconditionRequired = 428
STATUS_TooManyRequests = 429
STATUS_RequestHeaderFieldsTooLarge = 431
STATUS_ConnectionClosedWithoutResponse = 441
STATUS_UnavailableForLegalReasons = 451
STATUS_ClientClosedRequest = 499
STATUS_InternalServerError = 500
STATUS_NotImplemented = 501
STATUS_BadGateway = 502
STATUS_ServiceUnavailable = 503
STATUS_GatewayTimeout = 504
STATUS_HTTPVersionNotSupported = 505
STATUS_VariantAlsoNegotiates = 506
STATUS_InsufficientStorage = 507
STATUS_LoopDetected = 508
STATUS_NotExtended = 510
STATUS_NetworkAuthenticationRequired = 511
STATUS_NetworkConnectTimeoutError = 598
# TODO: add more status

status = impl.Response().Status
STATUS_DEFAULT = status.OK

STATUS_CODE = {
    STATUS_Ok: status.OK,
    STATUS_Created: status.Created,
    STATUS_NotFound: status.NotFound,
    STATUS_Continue: status.Continue,
    STATUS_SwitchingProtocols: status.SwitchingProtocols,
    STATUS_Processing: status.Processing,
    STATUS_Accepted: status.Accepted,
    STATUS_NonAuthoritativeInformation: status.NonAuthoritativeInformation,
    STATUS_NoContent: status.NoContent,
    STATUS_ResetContent: status.ResetContent,
    STATUS_PartialContent: status.PartialContent,
    STATUS_MultiStatus: status.MultiStatus,
    STATUS_AlreadyReported: status.AlreadyReported,
    STATUS_IMUsed: status.IMUsed,
    STATUS_MultipleChoices: status.MultipleChoices,
    STATUS_MovedPermanently: status.MovedPermanently,
    STATUS_Found: status.Found,
    STATUS_SeeOther: status.SeeOther,
    STATUS_NotModified: status.NotModified,
    STATUS_UseProxy: status.UseProxy,
    STATUS_TemporaryRedirect: status.TemporaryRedirect,
    STATUS_PermanentRedirect: status.PermanentRedirect,
    STATUS_BadRequest: status.BadRequest,
    STATUS_Unauthorized: status.Unauthorized,
    STATUS_PaymentRequired: status.PaymentRequired,
    STATUS_ProxyAuthenticationRequired: status.ProxyAuthenticationRequired,
    STATUS_MethodNotAllowed: status.MethodNotAllowed,
    STATUS_NotAcceptable: status.NotAcceptable,
    STATUS_RequestTimeout: status.RequestTimeout,
    STATUS_Conflict: status.Conflict,
    STATUS_Gone: status.Gone,
    STATUS_LengthRequired: status.LengthRequired,
    STATUS_PreconditionFailed: status.PreconditionFailed,
    STATUS_PayloadTooLarge: status.PayloadTooLarge,
    STATUS_RequestURITooLong: status.RequestURITooLong,
    STATUS_UnsupportedMediaType: status.UnsupportedMediaType,
    STATUS_RequestedRangeNotSatisfiable: status.RequestedRangeNotSatisfiable,
    STATUS_ExpectationFailed: status.ExpectationFailed,
    STATUS_ImATeapot: status.ImATeapot,
    STATUS_UnprocessableEntity: status.UnprocessableEntity,
    STATUS_Locked: status.Locked,
    STATUS_FailedDependency: status.FailedDependency,
    STATUS_UpgradeRequired: status.UpgradeRequired,
    STATUS_PreconditionRequired: status.PreconditionRequired,
    STATUS_TooManyRequests: status.TooManyRequests,
    STATUS_RequestHeaderFieldsTooLarge: status.RequestHeaderFieldsTooLarge,
    STATUS_ConnectionClosedWithoutResponse: status.ConnectionClosedWithoutResponse,
    STATUS_UnavailableForLegalReasons: status.UnavailableForLegalReasons,
    STATUS_ClientClosedRequest: status.ClientClosedRequest,
    STATUS_InternalServerError: status.InternalServerError,
    STATUS_NotImplemented: status.NotImplemented,
    STATUS_BadGateway: status.BadGateway,
    STATUS_ServiceUnavailable: status.ServiceUnavailable,
    STATUS_GatewayTimeout: status.GatewayTimeout,
    STATUS_HTTPVersionNotSupported: status.HTTPVersionNotSupported,
    STATUS_VariantAlsoNegotiates: status.VariantAlsoNegotiates,
    STATUS_InsufficientStorage: status.InsufficientStorage,
    STATUS_LoopDetected: status.LoopDetected,
    STATUS_NotExtended: status.NotExtended,
    STATUS_NetworkAuthenticationRequired: status.NetworkAuthenticationRequired,
    STATUS_NetworkConnectTimeoutError: status.NetworkConnectTimeoutError,
}

BASE_PATH = os.getcwd() + '/'
