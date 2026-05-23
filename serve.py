import os, sys
os.chdir('/Users/niinayoshinori/Downloads/emergency_suite_1')
sys.argv = ['serve']
from http.server import HTTPServer, SimpleHTTPRequestHandler
HTTPServer(('', 5500), SimpleHTTPRequestHandler).serve_forever()
