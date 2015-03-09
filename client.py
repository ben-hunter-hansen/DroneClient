import socket

class ArduinoClient:
	def __init__(self, conn_info):
		self.connection_info = conn_info
		self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def is_alive(self):
		return self.send('test')

	def move(self,direction):
		if direction is not None:
			return self.send(direction)
		else:
			return None

	def send(self, command):
		response = None

		try:
			sent = self.serv_sock.sendto(command,self.connection_info)
			data, server = self.serv_sock.recvfrom(4096)
			response = data
		except Exception, e:
			print str(e)
		finally:
			return response