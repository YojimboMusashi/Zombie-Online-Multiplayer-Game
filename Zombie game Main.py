import pygame
import sys
from sprites import Sprites
from player import Player
from zombie import Zombie

screen_w = 1600
screen_h = 800

screen = pygame.display.set_mode((screen_w, screen_h))

sprites = Sprites(screen)


class Corpse:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite

    def draw(self):
        screen.blit(self.sprite, (self.x - 250, self.y - 250))


corpses = []

zom1 = Zombie(1200, 250, "male")
zom2 = Zombie(1150, 500, "female")

zombies = [zom1, zom2]
# zombies = []


player1 = Player(100, 100, 50, 50, (0, 0, 0))
player2 = Player(500, 500, 50, 50, (0, 0, 0))

# players = [player1, player2]
players = [player1]


def update_logic():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.KEYDOWN:
            pass

    player1.move()

    for zom in zombies:
        zom.update(players)

    for player in players:
        player.update(zombies)

    add_zombies()


def add_zombies():
    global zombies
    # dead_zoms = 0
    for zom in zombies:
        if zom.action == "Dead":
            offset = 0
            if zom.type == "female":
                sprite = sprites.Zombie_female_dead
            else:
                offset = 100
                sprite = sprites.Zombie_male_dead
            corpses.append(Corpse(zom.x, zom.y, sprite[zom.direction][-1]))
            zombies.append(Zombie(1150 + offset, 500 + offset, zom.type))
            zombies.remove(zom)


def update_display(frame):
    screen.fill((125, 125, 125))
    for corpse in corpses:
        corpse.draw()
    if len(corpses) > 2:
        corpses.remove(corpses[0])
    for zom in zombies:
        zom.draw(frame, screen, sprites)
    for player in players:
        player.draw(frame, screen, sprites)
    pygame.display.flip()


def run():
    clock = pygame.time.Clock()
    frame = 0
    while True:
        clock.tick(60)
        update_logic()
        update_display(frame)
        frame += 1


run()
