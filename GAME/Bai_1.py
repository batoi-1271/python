import sys
import pygame
import pygame.locals as pl
from pygame import mixer
mixer.init()
pygame.init()
WIDTH = 1200
HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
font = pygame.font.SysFont("tahoma", 30)

pygame.mixer.music.load(r'D:\Python\GAME\truykich.mp3')
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")

### Tạo surface và vẽ hình chiếc xe ###
car_begin = 0
SIZE_CAR = 500
tocdo = 1
tien_len= True
surface = pygame.Surface((500, 300), pl.SRCALPHA)
pygame.draw.circle(surface, GREEN, (100, 200), 50)
pygame.draw.circle(surface, GREEN, (400, 200), 50)
pygame.draw.polygon(surface, RED,((0, 200), (0, 100), (100, 100), (150, 0), (350, 0), (400, 100), (500, 100), (500, 200)))
### Xác định FPS ###
fps = 60
s = 0
watch = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pl.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pl.KEYUP:
            if event.key == pl.K_LEFT:
                if tocdo >= 1:
                    tocdo -= 1
            elif event.key == pl.K_RIGHT:
                if tocdo >= 0:
                    tocdo += 1
    window.fill(WHITE)
    window.blit(surface, (car_begin, 100))

    dau_oto = car_begin + SIZE_CAR
    if tien_len:
        car_begin += tocdo
    else:
        car_begin -= tocdo
    if dau_oto >= WIDTH:
        tien_len = False
    elif car_begin <= 0:
        tien_len = True

    text = font.render("Toc do: " + str (tocdo), GREEN, RED)
    window.blit(text, (10, 450))
    pygame.display.update()
    watch.tick(fps)
