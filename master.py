import socket
import json

if starting:
  SLAVE_IP = "192.168.0.10"
  SLAVE_PORT = 6005
  
  xbox1 = xbox360[0]
  xbox2 = xbox360[1]
  udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  
def update():
  global udp
  global SLAVE_IP
  global SLAVE_PORT
  
  statuses = getStatusForXboxControls([xbox1, xbox2])
  data = json.dumps(statuses)
  
  udp.sendto(data, (SLAVE_IP, SLAVE_PORT))

def getStatusForXboxControls(controls):
  return [getXboxStatus(control) for control in controls]

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

  status["lth"] = xbox.rightThumb 
  status["rth"] = xbox.leftThumb

  status["rx"] = xbox.rightStickX 
  status["ry"] = xbox.rightStickY
  status["lx"] = xbox.leftStickX  
  status["ly"] = xbox.leftStickY
  
  status["back"] = xbox.back
  status["start"] = xbox.start
  
  return status
  
update()
