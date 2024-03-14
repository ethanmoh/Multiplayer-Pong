import pygame
from network import Network
from player import Player
pygame.font.init()
import sys

width = 800
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Blitz")

def redrawWindow(win,player, player2, balls, game):
    win.fill((128,128,128))
    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        pygame.display.update()
    elif (game.p0lives == 0) or (game.p1lives == 0):
        # P1 lives
        font = pygame.font.SysFont("comicsans", 20)
        p1_lives_text = font.render("P1 Lives: {}".format(game.p0lives), 1, (0,0,255))
        win.blit(p1_lives_text, (10, 10))

        # P2 lives
        p2_lives_text = font.render("P2 Lives: {}".format(game.p1lives), 1, (255,0,0))
        win.blit(p2_lives_text, (width - p2_lives_text.get_width() - 10, 10))

        # Draw scores
        score_text = font.render("P1: {}    P2: {}".format(game.p0, game.p1), 1, (61,145,64))
        win.blit(score_text, (350, 10))

        balls.draw(win)
        pygame.display.update()
    else:
        win.fill((255,255,255))
        
        # P1 lives
        font = pygame.font.SysFont("comicsans", 20)
        p1_lives_text = font.render("P1 Lives: {}".format(game.p0lives), 1, (0,0,255))
        win.blit(p1_lives_text, (10, 10))

        # P2 lives
        p2_lives_text = font.render("P2 Lives: {}".format(game.p1lives), 1, (255,0,0))
        win.blit(p2_lives_text, (width - p2_lives_text.get_width() - 10, 10))

        # Draw scores
        #font = pygame.font.SysFont("comicsans", 20)
        score_text = font.render("P1: {}    P2: {}".format(game.p0, game.p1), 1, (61,145,64))
        win.blit(score_text, (350, 10))
        
        player.draw(win)
        player2.draw(win)
        balls.draw(win)
        pygame.display.update()


def main():
    pygame.init()
    run = True
    n = Network()
    data1 = n.getP()
    p = data1[0]
    g = data1[1]
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        data = n.send(p)
        p2 = data[0]
        balls = data[1]
        g = data[2]

        if g.close == True:
            run = False
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        p.move()
        redrawWindow(win, p, p2, balls, g)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (220,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()
