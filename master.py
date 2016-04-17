import socket
import json
import threading
import time
import datetime

CONNECTION_REQUEST = "REMOTEPADCONNECTIONREQUEST"
CONNECTION_ACCEPTED = "REMOTEPADCONNECTIONACCEPTED"
MASTER_IP = socket.gethostbyname(socket.gethostname())
SLAVE_IP = ""
PORT = 6009

slave_founded = False

xbox1 = xbox360[0]
xbox2 = xbox360[1]

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((MASTER_IP, PORT))
  
def look_for_slave():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('', 0))
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

	while not slave_founded:
		diagnostics.debug("trying find slave on %s" % PORT)
		s.sendto(CONNECTION_REQUEST, ('<broadcast>', PORT))
		time.sleep(5)

def wait_for_slave():
	global slave_founded, SLAVE_IP
	
	while True:
		data, addr = udp.recvfrom(1024)
		
		if (data == CONNECTION_ACCEPTED):
			diagnostics.debug("slave founded")
			slave_founded = True
			SLAVE_IP = addr[0]
			break
	
	run()

def run():
 	while True:
		update()
		time.sleep(0.015)
  
def update():
  statuses = getStatusForXboxControls([xbox1, xbox2])
  data = json.dumps(statuses)
  
  udp.sendto(data, (SLAVE_IP, PORT))

def getStatusForXboxControls(controls):
  return [getXboxStatus(control) for control in controls]

def getXboxStatus(xbox):
  status = {}

  status["a"] = xbox.a
  status["b"] = xbox.b
  status["x"] = xbox.x  
  status["y"] = xbox.y
  
  diagnostics.debug(status["a"])
  
  status["rb"] = xbox.rightShoulder 
  status["rt"] = xbox.rightTrigger
  status["lb"] = xbox.leftShoulder  
  status["lt"] = xbox.leftTrigger
  
  status["up"] = xbox.up
  status["down"] = xbox.down  
  status["right"] = xbox.right
  status["left"] = xbox.left

  status["lth"] = xbox.rightThumb 
  status["rth"] = xbox.leftThumb

  status["rx"] = xbox.rightStickX 
  status["ry"] = xbox.rightStickY
  status["lx"] = xbox.leftStickX  
  status["ly"] = xbox.leftStickY
  
  status["back"] = xbox.back
  status["start"] = xbox.start
  
  diagnostics.debug(datetime.datetime.now())
  
  return status

if starting:

  t1 = threading.Thread(target=look_for_slave)
  t2 = threading.Thread(target=wait_for_slave)
	
  t1.setDaemon(True)
  t2.setDaemon(True)
	
  t1.start()
  t2.start()

def pront():
	diagnostics.debug("hola")

pront()
