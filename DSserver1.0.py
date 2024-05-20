# Import libraries 
import http.server 
import socketserver

# Defining PORT number 
PORT = 1999

# Creating handle 
Handler = http.server.SimpleHTTPRequestHandler 

# Creating TCPServer 
http = socketserver.TCPServer(("", PORT), Handler) 

# Getting logs 
print("SERVER STARTED")
import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print("port:", PORT) 
http.serve_forever()
