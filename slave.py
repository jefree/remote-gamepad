import socket
import json

def setStatus(vjoy, status):

    vjoy.x = status["lx"] * AXIS_CALIBRATOR
    vjoy.y = status["ly"] * AXIS_CALIBRATOR

    vjoy.rx = status["rx"] * AXIS_CALIBRATOR
    vjoy.ry = status["ry"] * AXIS_CALIBRATOR

    for key, value in BUTTON_MAP.iteritems():
            vjoy.setButton(int(key), status[value])

def setStatusByControl(controls, statuses):
    for (control, status) in zip(controls, statuses):
        setStatus(control, status)

def wait_for_server():
    while True:
        data, addr = udp.recvfrom(1024)
        diagnostics.debug("data %s from %s " % (data, addr))

        if (data == CONNECTION_REQUEST):
            diagnostics.debug("connected to %s" % addr[0])
            accept_connection(addr[0])
            run()

def run():
    while True:
        data, addr = udp.recvfrom(1024)
        statuses = json.loads(data)
        setStatusByControl([vjoy1, vjoy2], statuses)

def accept_connection(addr):
    udp.sendto(CONNECTION_ACCEPTED, (addr, PORT))

if starting:

    SLAVE_IP = socket.gethostbyname(socket.gethostname())
    PORT = 6060
    CONNECTION_REQUEST = "REMOTEPADCONNECTIONREQUEST"
    CONNECTION_ACCEPTED = "REMOTEPADCONNECTIONACCEPTED"

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

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((SLAVE_IP, PORT))

    vjoy1 = vJoy[0]
    vjoy2 = vJoy[1]

    diagnostics.debug("listening on %s" % PORT)

    wait_for_server()
