import neynpy

print(neynpy.impl.Major)
print(neynpy.impl.Minor)
print(neynpy.impl.Patch)


class MyServer:
    def __init__(self):
        self.dummy = 10
        self.server = neynpy.impl.Server()
        self.server.handler = self.handler

    def handler(self, req):
        print(self.dummy)
        print(req.header)

        res = neynpy.impl.Response()
        res.body = "Hello"
        return res

    def run(self):
        C = neynpy.impl.Config()
        C.address = "0.0.0.0"
        C.port = 9090
        C.timeout = 0
        self.server.config = C
        self.server.run()


S = MyServer()
print('Server run on http://0.0.0.0:9090')
print(S.run())
