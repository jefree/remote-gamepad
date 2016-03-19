import socket
import json

SLAVE_IP = "192.168.0.12"
SLAVE_PORT = 6003

AXIS_CALIBRATOR = 17000

BUTTON_MAP = {
    "0": "lt",
    "1": "lb",
    "2": "rb",
    "3": "rt",

    "4": "a",
    "5": "b",
    "6": "y",
    "7": "x",

    "8": "up",
    "9": "right",
    "10": "down",
    "11": "left",

    "12": "back",
    "13": "start",

    "14": "rth",
    "15": "lth"
}

def setStatus(vjoy, data):
    status = json.loads(data)
    
    vjoy.x = status["lx"] * AXIS_CALIBRATOR
    vjoy.y = status["ly"] * AXIS_CALIBRATOR
    
    vjoy.rx = status["rx"] * AXIS_CALIBRATOR
    vjoy.ry = status["ry"] * AXIS_CALIBRATOR
    
    diagnostics.watch(vjoy.x)

    for key, value in BUTTON_MAP.iteritems():
        vjoy.setButton(int(key), status[value])

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((SLAVE_IP, SLAVE_PORT))

print ("listening on", SLAVE_PORT)

while True:
    data, addr = udp.recvfrom(1024)

    vjoy1 = vJoy[0]
    setStatus(vjoy1, data)
