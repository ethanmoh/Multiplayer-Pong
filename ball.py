import pygame
import random

class Ball:
    def __init__(self, screen_width, screen_height):
        self.radius = 5
        self.color = (0, 255, 0),
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.speed_x = 1  # Initial speed in the x direction
        self.speed_y = 1  # Initial speed in the y direction

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Check for collisions with walls
        #if self.x - self.radius < 0 or self.x + self.radius > self.screen_width + 15:
            #self.reset()

        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen_height:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def reset(self):
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2
        self.speed_x *= -1  # Invert the direction of the ball horizontally
        self.speed_y *= -1  # Invert the direction of the ball vertically

    def get_info(self):
        return (self.x, self.y, self.speed_x, self.speed_y)
    
    def update_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))