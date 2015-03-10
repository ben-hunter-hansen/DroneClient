class Network:
	@staticmethod
	def Arduino():
		return ('192.168.1.21',10000)

class Resource:
	@staticmethod
	def Icons():
		return ['res/wheel.png','res/battery.png','res/network.png']

class Color:
	@staticmethod
	def Red():
		return (250,0,0)

	@staticmethod
	def Blue():
		return (0,0,250)

class Movement:
	@staticmethod
	def Forward():
		return 'forward'

	@staticmethod
	def Left():
		return 'left'

	@staticmethod
	def Right():
		return 'right'

	@staticmethod
	def Reverse():
		return 'reverse'

	@staticmethod
	def Stop():
		return 'stop'

	@staticmethod
	def All():
		return [Movement.Forward(),Movement.Left(),Movement.Right(),Movement.Reverse(),Movement.Stop()]


class Shapes:
	@staticmethod
	def ArrowUp():
		return [[75,475],[100,425],[125,475]]

	@staticmethod
	def ArrowLeft():
		return [[25,500],[75,475],[75,525]]

	@staticmethod
	def ArrowRight():
		return [[125,475],[175,500],[125,525]]
		
	@staticmethod
	def ArrowDown():
		return [[75,525],[100,575],[125,525]]

	@staticmethod
	def Square():
		return [[75,525],[75,475],[125,475],[125,525]]

	@staticmethod
	def Controls():
		return [Shapes.ArrowUp(),Shapes.ArrowLeft(),Shapes.ArrowRight(),Shapes.ArrowDown(),Shapes.Square()]


class DrawUtils:
	@staticmethod
	def RenderIcons(screen,icons, xy, increment):
		x, y = xy
		for icon in icons:
			screen.blit(icon,(x,y))
			x += increment


	@staticmethod
	def RenderControls(screen,color,shapes,thickness,callback):
		for shape in shapes:
			callback(screen,color,shape,thickness)