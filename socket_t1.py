import socket
import re
import sys

def check_server(address, port):
    #Create a TCP socket
    s = socket.socket()
    print("Attempting to connect to {} on port {}".format(address, port))
    try:
        s.connect((address, port))
        print("Connected to {} on port {}".format(address, port))
        return True
    except:
        print("Connection to {} on port {} failed".format(address, port))
        return False
    
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    
    parser.add_option('-a', '--address', dest='address', default='localhost',help='ADDRESS for server', metavar='ADDRESS')
    parser.add_option('-p', '--port', dest='port', type='int', default=80,help='PORT for server', metavar='PORT')
    (options, args) = parser.parse_args()
    print('option:{}:::{}'.format(options, args))
    check = check_server(options.address, options.port)
    print('check_server returned {}'.format(check))
    sys.exit(not check)
