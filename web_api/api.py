import time
import BaseHTTPServer
from thread import start_new_thread
import RPi.GPIO as GPIO


HOST_NAME = '0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 80 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()

	def do_GET(s):
		dv,md,rsx=wwe(s.path[1:])
		"""Respond to a GET request."""
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		s.wfile.write("<html><head><title>Response GPIO%s.</title></head>" % dv)
		s.wfile.write("<body><p>Response For GPIO%s</p>" % dv)
		s.wfile.write("<p>Device: GPIO%s</p>" % dv)
		s.wfile.write("<p>Mode: %s</p>" % md)
		s.wfile.write("<p>Response: %s</p>" % rsx)
		s.wfile.write("</body></html>")

def wwe(ss):
	if '.ico' in ss:
		return(' ',' ',' ')
	try:
		dev,mode,val=ss.split('/')
	
		if dev in('17','18','27','22','23','24','25','5','6','13','19','26','21','20','16','12'):
			if mode=='out':
				GPIO.setup(int(dev),GPIO.OUT)
				if val=='on':
					GPIO.output(int(dev),GPIO.HIGH)
					return(str(dev),'OUTPUT','OK')
				else:
					GPIO.output(int(dev),GPIO.LOW)
					return(str(dev),'OUTPUT','OK')
			elif mode=='in':
				GPIO.setup(int(dev),GPIO.IN)
				if val=='q':
					return(str(dev),'INPUT',str(GPIO.input(int(dev))))
				else:
					return(str(dev),'ERROR','Error')
	except Exception as s:
		print s
		return('Error',"Error",'Error')

def Server_Bgn():
	GPIO.setmode(GPIO.BCM)
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

Server_Bgn()