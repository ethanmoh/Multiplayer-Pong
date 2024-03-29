import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 10

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if self.y - self.vel < 0:
                pass
            else:
                self.y -= self.vel

        if keys[pygame.K_DOWN]:
            if self.y + self.vel > 420:
                pass
            else:
                self.y += self.vel
        
        self.update()
        
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)