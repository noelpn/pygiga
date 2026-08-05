from pygiga.api.grpc import GRPCServer

if __name__ == '__main__':
    server = GRPCServer()
    print('Server info:', server.info())
