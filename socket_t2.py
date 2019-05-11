import socket
import re
import sys

def check_webserver(address, port, resource):
    #build up HTTP request string
    if not resource.startswith('/'):
        resource = '/' + resource
        
    request_string = "GET {} HTTP/1.1\r\nHost: {}\r\n\r\n".format(resource, address)
    print('HTTP request')
    print('|||{}|||'.format(request_string))
    
    #Create a TCP socket
    s = socket.socket()
    print("Attempting to connect to {} on port {}".format(address, port))
    try:
        s.connect((address, port))
        print("Connected to {} on port {}".format(address, port))
        s.send(request_string)
        #we should only need the first 100 bytes or so
        rsp = s.recv(100)
        print('Received 100 bytes of HTTP response')
        print('|||{}|||'.format(rsp))
    
    except:
        print("Connection to {} on port {} failed".format(address, port))
        return False
    finally:
        # be a good citizen and close your connection
        print('Closing the connection')
        s.close()
    
    lines = rsp.splitlines()
    print('First line of HTTP response: {}'.format(lines[0]))
    try:
        version, status, message = re.split(r'\s+', lines[0], 2)
        print('Version:{}, Status:{}, Message:{}'.format(version, status, message))
    except ValueError:
        print('Failed to split status line')
        return False
    if status in ['200', '300']:
        print('Sucess - status was {}'.format(status))
        return True
    else:
        print('Status was {}'.format(status))
        return False
    
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    
    parser.add_option('-a', '--address', dest='address', default='localhost',help='ADDRESS for server', metavar='ADDRESS')
    parser.add_option('-p', '--port', dest='port', type='int', default=80,help='PORT for server', metavar='PORT')
    parser.add_option('-r', '--resource', dest='resource', default='index.html',help='RESOURCE to check', metavar='RESOURCE')
    
    (options, args) = parser.parse_args()
    print('options:{}, args:{}'.format(options, args))
    check = check_webserver(options.address, options.port, options.resource)
    print('check_webserver returned {}'.format(check))
    sys.exit(not check)
