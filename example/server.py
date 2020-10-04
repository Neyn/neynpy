from neynpy.core.server import Server
from neynpy.core.route import Router
from neynpy.http.response import Response, Serve


def about(request):
    return Response('return from about view', 200)


def main(request):
    print(request.method, request.path)
    return Response('a.html', is_file=True)


def files(request):
    print(request.method, request.path)
    return Serve('/', '/home/ahmad/Downloads')


router = Router()
router.add_handler('/', main)
router.add_handler('/about', about, methods=['POST'])
router.add_handler('/files', files, prefix=True)

_server = Server(ip='127.0.0.1', port='7070', router=router)
_server.run()
