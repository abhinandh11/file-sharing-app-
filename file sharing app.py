# import necessary modules
for implementing the HTTP web servers
import http.server
# provides access to the BSD socket interface
import socket
# a framework for network servers
import socketserver
# to display a web-based documents to users 
import webbrowser
# to generate qrcode
import pyqrcode
from pyqrcode import QRCode 
# convert to png format
import png
# to access operating system control
import os

# assigning the appropriate port value 
port = 8010
# this finds the name of the computer user
os.environ['USERPROFILE']
# changing the directory to access the files desktop
# with the help of os module
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive')
os.chdir(desktop)
# creating a http request
Handler = http.server.SimpleHTTPRequsetHandler
# returns , host name of the system under
# which python interpreter is executed
 hostname = socket.gethostname()

 # finding the IP address of the pc 
 s = socket .socket(socket.AF_INET,socket.SOCK_DGRAM)
 s.connect(("8.8.8.8", 80))
 IP ="http://" + s.getsockname()[0] +":" + str(PORT)
 link = IP
 
 #Creating the HTTP request and serving the 
 #folder in the PORT 8010, and the pyqrcode is generated 

 #continuous stream of data between client and server 
 with socketserver.TCPServer ((" ", PORT), Handler) as httpd:
    print("serving at port ", PORT)
    print(" type this in your browser", IP)
    print("or use the QRCode ")
    httpd.server_forever()
