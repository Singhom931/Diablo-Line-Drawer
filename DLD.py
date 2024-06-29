import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 480
blockSize = 60  # Set the size of the grid block

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        drawLine(screen, 8, 6, 1, 5,)  # input X1, Y1, X2, Y2
        drawGrid(screen)
        pygame.display.update()
        clock.tick(60)

def drawGrid(screen):
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

def plotPoint(screen, x, y):
    plot = pygame.Rect((x - 1) * blockSize, (y - 1) * blockSize, blockSize, blockSize)
    pygame.draw.rect(screen, RED, plot)

def drawLine(screen, x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        plotPoint(screen, x1, y1)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

main()
