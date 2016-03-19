import socket

SLAVE_IP = "192.168.0.11"
SLAVE_PORT = 6666

BUTTON_MAP = {
    0: "lt",
    1: "lb",
    2: "rb",
    3: "rt",

    4: "a",
    5: "b",
    6: "y",
    7: "x",

    8: "up",
    9: "right",
    10: "down",
    11: "left",

    12: "back",
    13: "start",

    14: "rt",
    15: "lt"
}

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((SLAVE_IP, SLAVE_PORT))

print ("listening on", SLAVE_PORT)

while True:
    data, addr = udp.recvfrom(1024)
    print ("data", data)