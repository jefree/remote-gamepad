import socket
import json

if starting:
	SLAVE_IP = "192.168.0.11"
	SLAVE_PORT = 6666
	
	xbox1 = xbox360[0]
	udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
def update():
	global udp
	global xbox1
	global SLAVE_IP
	global SLAVE_PORT
	
	status = getXboxStatus(xbox1)
	data = json.dumps(status)
	
	udp.sendto(data, (SLAVE_IP, SLAVE_PORT))
	
def getXboxStatus(xbox):
	status = {}

	status["a"] = xbox.a
	status["b"] = xbox.b
	status["x"] = xbox.x	
	status["y"] = xbox.y
	
	status["rb"] = xbox.rightShoulder	
	status["rt"] = xbox.rightTrigger
	status["lb"] = xbox.leftShoulder	
	status["lt"] = xbox.leftTrigger
	
	status["up"] = xbox.up
	status["down"] = xbox.down	
	status["right"] = xbox.right
	status["left"] = xbox.left

	status["lt"] = xbox.rightThumb	
	status["rt"] = xbox.leftThumb

	status["rx"] = xbox.rightStickX	
	status["ry"] = xbox.rightStickY
	status["lx"] = xbox.leftStickX	
	status["ly"] = xbox.leftStickY
	
	status["back"] = xbox.back
	status["start"] = xbox.start
	
	return status
	
update()
