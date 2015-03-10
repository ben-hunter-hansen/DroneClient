import socket
import threading

class ArduinoClient:
	def __init__(self,network_info):
		self.connection = network_info
		self.socket = None
		self.recv_event = None

	def apply_on_recv(self,f):
		self.recv_event = f

	def send(self,command):
		if command is None:
			raise Exception("Undefined command in ArduinoClient.send()!")
		else:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			try:
				sent = self.socket.sendto(command,self.connection)
				reply = None
				while reply is None:
					reply, server = self.socket.recvfrom(1024)
				self.recv_event(reply)
			finally:
				self.socket.close()


