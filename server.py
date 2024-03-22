import socket
from _thread import *
from player import Player
from zombie import Zombie, Corpse
import pickle


server = "178.79.176.44"
port = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("waiting for a connection, Server Started")


players = [Player(100, 300, 50, 50, (255, 0, 0)), Player(100, 500, 50, 50, (0, 0, 255))]

zombies = [Zombie(1200, 250, "male"), Zombie(1150, 500, "female")]

corpses = []


def add_zombies():
    global zombies
    global corpses
    # dead_zoms = 0
    for zom in zombies:
        if zom.action == "Dead":
            offset = 0
            if zom.type == "female":
                _type_ = "female"
            else:
                offset = 100
                _type_ = "male"
            corpses.append(Corpse(zom.x, zom.y, _type_, zom.direction))
            if len(corpses) >= 3:
                corpses.remove(corpses[0])
            zombies.append(Zombie(1150 + offset, 500 + offset, zom.type))
            zombies.remove(zom)


def threaded_client(_conn, player):
    global currentPlayer
    _conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(_conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                zombies[0].update(players)
                zombies[1].update(players)
                players[0].update(zombies)
                players[1].update(zombies)
                if player == 1:
                    reply = [players[0], zombies[0], zombies[1], corpses]
                else:
                    reply = [players[1], zombies[0], zombies[1], corpses]

                add_zombies()
                # print("Received: ", data)
                # print("Sending : ", reply)

            _conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost Connection")
    conn.close()
    currentPlayer -= 1


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1