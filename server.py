import socket
from _thread import *
from player import Player
import pickle
from ball import Ball
import pygame
from game import Game

server = ''
serversoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = socket.gethostname(server)  
try:
    serversoc.bind((server,5555))          
except socket.error as e:
    str(e)   

serversoc.listen(2)

print("Waiting for a connection, Server Started")

global players
global ball
players = [Player(40, 250, 5, 80, (0,0,255)), Player(740, 250, 5, 80, (255,0,0))]
ball = Ball(800, 500)

def update_ball():
    print("Updating the ball")
    if ball.x + ball.radius > players[1].x and players[1].y < ball.y < players[1].y + players[1].height:
        print("Updating the ball for player 2")
        ball.speed_x = -abs(ball.speed_x)
        games.p1 += 1
        ball.update_color()
        print("COLOR")
        print("P1", games.p1)
        if(games.p1 % 10 == 0):
            if(ball.speed_x > 0):
                ball.speed_x +=1
            else:
                ball.speed_x = ball.speed_x - 1
            print("EXECUTED")
    if ball.x - ball.radius < players[0].x + players[0].width and players[0].y < ball.y < players[0].y + players[0].height:
        print("Updating the ball for player 1")
        ball.speed_x = abs(ball.speed_x)
        games.p0 += 1
        ball.update_color()
        print("COLOR")
        print("P0", games.p0)
        if(games.p0 % 10 == 0):
            if(ball.speed_x > 0):
                ball.speed_x +=1
            else:
                ball.speed_x = ball.speed_x - 1
            print("EXECUTED")
    if ball.x - ball.radius < 0:
        games.p0lives = games.p0lives -1
        ball.reset()
    if ball.x + ball.radius > ball.screen_width + 15:
        games.p1lives = games.p1lives -1
        ball.reset()
    ball.move()

def threaded_client(conn, player):
    global currentPlayer
    global players
    global ball
    reply1 = []
    reply1.append(players[player])
    reply1.append(games)
    conn.send(pickle.dumps(reply1))
    reply = []
    while True:
        try:
            data = pickle.loads(conn.recv(2048*3))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply.append(players[0])
                else:
                    reply.append(players[1])
                
                reply.append(ball)
                reply.append(games)

                print("Received: ", data)
                print("Sending : ", reply)
                print("Speed: ", ball.speed_x)
                if games.connected() and games.p0lives > 0 and games.p1lives > 0:
                    update_ball()

            conn.sendall(pickle.dumps(reply))
            reply = []
        except:
            break

    print("Lost connection")
    games.close = True
    games.ready = False
    games.p0 = 0
    games.p1 = 0
    games.p0lives = 10
    games.p1lives = 10
    currentPlayer = 0
    players = [Player(40, 250, 5, 80, (0,0,255)), Player(740, 250, 5, 80, (255,0,0))]
    ball = Ball(800, 500)
    conn.close()

global currentPlayer
currentPlayer = 0
games = Game()

while True:
    games.close = False
    conn, addr = serversoc.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    if currentPlayer == 2:
        games.ready = True