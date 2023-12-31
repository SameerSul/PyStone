import pygame, sys

# Constants
WIDTH, HEIGHT = 1280, 720
TITLE = "CLASH: A Game by Sameer Suleman"

# pygame initialization shenanigans
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# Player Class
class Player:
    def __init__(self, x, y):
        # Position Coordinates + where to spawn
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (255, 192, 203)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    # Determine speed + direction based on sign of velX and velY
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)


# Player Initialization, spawn in middle
player = Player(WIDTH / 2, HEIGHT / 2)

# Where the magic happens
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # User presses key execute these command(s)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left_pressed = True
            if event.key == pygame.K_d:
                player.right_pressed = True
            if event.key == pygame.K_w:
                player.up_pressed = True
            if event.key == pygame.K_s:
                player.down_pressed = True
        # User lets go of key, execute these command(s)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left_pressed = False
            if event.key == pygame.K_d:
                player.right_pressed = False
            if event.key == pygame.K_w:
                player.up_pressed = False
            if event.key == pygame.K_s:
                player.down_pressed = False

    # Draw
    win.fill((12, 24, 36,))
    player.draw(win)

    # update
    player.update()
    pygame.display.flip()

    clock.tick(120)