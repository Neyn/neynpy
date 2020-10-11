#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "neyn/neyn.h"

using namespace Neyn;
namespace py = pybind11;

struct Filer_ : Filer
{
    using Handler = std::function<Response(const Request &request)>;

    Handler _error;

    Filer_()
    {
        base = "/";
        error = [this](Request &request, Response &response) { response = _error(request); };

        _error = [](const Request &) {
            Response response;
            response.status = Status::NotFound;
            return response;
        };
    }

    Response handle(const Request &request)
    {
        Response response;
        Filer::operator()(const_cast<Request &>(request), response);
        return response;
    }
};

struct Server_ : Server
{
    using Handler = std::function<Response(const Request &request)>;

    Handler _handler;

    Server_()
    {
        handler = [this](Request &request, Response &response) { response = _handler(request); };
    }
};

PYBIND11_MODULE(impl, m)
{
    // py::module m = _m.def_submodule("impl");
    py::class_<Filer_> filer(m, "Filer");
    py::class_<Config> config(m, "Config");
    py::class_<Server_> server(m, "Server");
    py::class_<Request> request(m, "Request");
    py::class_<Response> response(m, "Response");

    m.attr("Major") = NEYN_VERSION_MAJOR;
    m.attr("Minor") = NEYN_VERSION_MINOR;
    m.attr("Patch") = NEYN_VERSION_PATCH;

    py::enum_<Error>(server, "Error")
        .value("None", Error::None)
        .value("GeneralError", Error::GeneralError)
        .value("SocketError", Error::SocketError)
        .value("SocketCreate", Error::SocketCreate)
        .value("SocketListen", Error::SocketListen)
        .value("SocketAccept", Error::SocketAccept)
        .value("SetReuse", Error::SetReuse)
        .value("SetNonblock", Error::SetNonblock)
        .value("SetAddress", Error::SetAddress)
        .value("EpollCreate", Error::EpollCreate)
        .value("EpollAdd", Error::EpollAdd)
        .value("EpollWait", Error::EpollWait)
        .value("TimerCreate", Error::TimerCreate)
        .value("ThreadCreate", Error::ThreadCreate)
        .value("WrongParameter", Error::WrongParameter);

    py::enum_<Status>(response, "Status")
        .value("Continue", Status::Continue)
        .value("SwitchingProtocols", Status::SwitchingProtocols)
        .value("Processing", Status::Processing)
        .value("OK", Status::OK)
        .value("Created", Status::Created)
        .value("Accepted", Status::Accepted)
        .value("NonAuthoritativeInformation", Status::NonAuthoritativeInformation)
        .value("NoContent", Status::NoContent)
        .value("ResetContent", Status::ResetContent)
        .value("PartialContent", Status::PartialContent)
        .value("MultiStatus", Status::MultiStatus)
        .value("AlreadyReported", Status::AlreadyReported)
        .value("IMUsed", Status::IMUsed)
        .value("MultipleChoices", Status::MultipleChoices)
        .value("MovedPermanently", Status::MovedPermanently)
        .value("Found", Status::Found)
        .value("SeeOther", Status::SeeOther)
        .value("NotModified", Status::NotModified)
        .value("UseProxy", Status::UseProxy)
        .value("TemporaryRedirect", Status::TemporaryRedirect)
        .value("PermanentRedirect", Status::PermanentRedirect)
        .value("BadRequest", Status::BadRequest)
        .value("Unauthorized", Status::Unauthorized)
        .value("PaymentRequired", Status::PaymentRequired)
        .value("Forbidden", Status::Forbidden)
        .value("NotFound", Status::NotFound)
        .value("MethodNotAllowed", Status::MethodNotAllowed)
        .value("NotAcceptable", Status::NotAcceptable)
        .value("ProxyAuthenticationRequired", Status::ProxyAuthenticationRequired)
        .value("RequestTimeout", Status::RequestTimeout)
        .value("Conflict", Status::Conflict)
        .value("Gone", Status::Gone)
        .value("LengthRequired", Status::LengthRequired)
        .value("PreconditionFailed", Status::PreconditionFailed)
        .value("PayloadTooLarge", Status::PayloadTooLarge)
        .value("RequestURITooLong", Status::RequestURITooLong)
        .value("UnsupportedMediaType", Status::UnsupportedMediaType)
        .value("RequestedRangeNotSatisfiable", Status::RequestedRangeNotSatisfiable)
        .value("ExpectationFailed", Status::ExpectationFailed)
        .value("ImATeapot", Status::ImATeapot)
        .value("MisdirectedRequest", Status::MisdirectedRequest)
        .value("UnprocessableEntity", Status::UnprocessableEntity)
        .value("Locked", Status::Locked)
        .value("FailedDependency", Status::FailedDependency)
        .value("UpgradeRequired", Status::UpgradeRequired)
        .value("PreconditionRequired", Status::PreconditionRequired)
        .value("TooManyRequests", Status::TooManyRequests)
        .value("RequestHeaderFieldsTooLarge", Status::RequestHeaderFieldsTooLarge)
        .value("ConnectionClosedWithoutResponse", Status::ConnectionClosedWithoutResponse)
        .value("UnavailableForLegalReasons", Status::UnavailableForLegalReasons)
        .value("ClientClosedRequest", Status::ClientClosedRequest)
        .value("InternalServerError", Status::InternalServerError)
        .value("NotImplemented", Status::NotImplemented)
        .value("BadGateway", Status::BadGateway)
        .value("ServiceUnavailable", Status::ServiceUnavailable)
        .value("GatewayTimeout", Status::GatewayTimeout)
        .value("HTTPVersionNotSupported", Status::HTTPVersionNotSupported)
        .value("VariantAlsoNegotiates", Status::VariantAlsoNegotiates)
        .value("InsufficientStorage", Status::InsufficientStorage)
        .value("LoopDetected", Status::LoopDetected)
        .value("NotExtended", Status::NotExtended)
        .value("NetworkAuthenticationRequired", Status::NetworkAuthenticationRequired)
        .value("NetworkConnectTimeoutError", Status::NetworkConnectTimeoutError);

    py::enum_<Address>(config, "Address")  //
        .value("IPV4", Address::IPV4)
        .value("IPV6", Address::IPV6);

    filer.def(py::init<>())
        .def_readwrite("root", &Filer_::root)
        .def_readwrite("error", &Filer_::_error)
        .def("handle", &Filer_::handle);

    request.def(py::init<>())
        .def_readwrite("address", &Request::address)
        .def_readwrite("port", &Request::port)
        .def_readwrite("major", &Request::major)
        .def_readwrite("minor", &Request::minor)
        .def_readwrite("method", &Request::method)
        .def_readwrite("path", &Request::path)
        .def_readwrite("body", &Request::body)
        .def_readwrite("header", &Request::header);

    response.def(py::init<>())
        .def_readwrite("status", &Response::status)
        .def_readwrite("body", &Response::body)
        .def_readwrite("header", &Response::header)
        .def("open", &Response::open);

    config.def(py::init<>())
        .def_readwrite("port", &Config::port)
        .def_readwrite("ipvn", &Config::ipvn)
        .def_readwrite("address", &Config::address)
        .def_readwrite("timeout", &Config::timeout)
        .def_readwrite("limit", &Config::limit);
    // .def_readwrite("threads", &Config::threads);

    server.def(py::init<>())
        .def_readwrite("config", &Server_::config)
        .def_readwrite("handler", &Server_::_handler)
        .def("run", &Server_::single);
}
