import pygame
from network import Network
from sprites import Sprites

pygame.init()


screen_w = 1600
screen_h = 800

screen = pygame.display.set_mode((screen_w, screen_h))
sprites = Sprites(screen)

pygame.display.set_caption("Client")


def redraw_window(frame, _screen, player, player2, zom1, zom2, corpses):
    _screen.fill((128, 128, 128))

    for corpse in corpses:
        corpse.draw(_screen, sprites)
    zom1.draw(frame, _screen, sprites)
    zom2.draw(frame, _screen, sprites)
    player.draw(frame, _screen, sprites)
    player2.draw(frame, _screen, sprites)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.get_p()
    clock = pygame.time.Clock()

    frame = 0
    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redraw_window(frame, screen, p, p2[0], p2[1], p2[2], p2[3])
        frame += 1


main()
