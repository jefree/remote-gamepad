import socket
import json

def setStatus(xoutput, status):
    xoutput.rx = status['rx']
    xoutput.ry = status]'ry']

    xoutput.lx = status['lx']
    xoutput.ly = status['ly']

    xoutput.Y = status['y']
    xoutput.B = status['b']
    xoutput.A = status['a']
    xoutput.X = status['x']

    xoutput.L1 = status['lb']
    xoutput.R1 = status['rb']
    xoutput.L3 = status['lth']
    xoutput.R3 = status['rth']

    xoutput.L2 = 0 if status['lt'] else xoutput.TriggerMin
    xoutput.R2 = 0 if status['rt'] else xoutput.TriggerMin

    xoutput.Up = status['up']
    xoutput.Right = status['right']
    xoutput.Down = status['down']
    xoutput.Left = status['left']

    xoutput.Back = status['back']
    xoutput.Start = status['start']

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
        setStatusByControl([xoutput1, xoutput2], statuses)

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

    xoutput1 = xoutput[0]
    xoutput2 = xoutput[1]

    diagnostics.debug("listening on %s" % PORT)

    wait_for_server()
