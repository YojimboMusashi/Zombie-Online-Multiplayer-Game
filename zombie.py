import pygame


class Zombie:
    def __init__(self, x, y, _type):
        self.x = x
        self.y = y
        self.movement = [0, 0]
        self.direction = 5
        self.type = _type
        self.vel = 5
        self.health = 100
        if self.type == "female":
            self.dead_sprite_count = 32
        else:
            self.dead_sprite_count = 43
            self.vel -= 1

        self.dying_sprite_count = 0

        self.action = "Running"
        self.hit_sprite_count = 0

    def draw(self, frame, screen, sprites):
        if self.action == "Running":
            if self.type == "female":
                sprite = sprites.Zombie_female_running
            else:
                sprite = sprites.Zombie_male_running
            screen.blit(sprite[self.direction][frame % len(sprite[self.direction])],
                        (self.x - 250, self.y - 250))
        if self.action == "hit":
            if self.type == "female":
                sprite = sprites.Zombie_female_hit
            else:
                sprite = sprites.Zombie_male_hit
            screen.blit(sprite[self.direction][self.hit_sprite_count],
                        (self.x - 250, self.y - 250))
        if self.action == "Walking":
            if self.type == "female":
                sprite = sprites.Zombie_female_walking
            else:
                sprite = sprites.Zombie_male_walking
            screen.blit(sprite[self.direction][frame % len(sprite[self.direction])],
                        (self.x - 250, self.y - 250))
        if self.action == "Dying":
            if self.type == "female":
                sprite = sprites.Zombie_female_dead
            else:
                sprite = sprites.Zombie_male_dead
            screen.blit(sprite[self.direction][self.dying_sprite_count],
                        (self.x - 250, self.y - 250))
        if self.action == "Dead":
            if self.type == "female":
                sprite = sprites.Zombie_female_dead
            else:
                sprite = sprites.Zombie_male_dead
            screen.blit(sprite[self.direction][-1],
                        (self.x - 250, self.y - 250))

        self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        health_bar_length = self.health * 1.5
        red_colour = 255 - self.health * 2
        if red_colour > 255:
            red_colour = 255
        green_colour = 55 + self.health * 2
        if green_colour < 0:
            green_colour = 0
        pygame.draw.rect(screen, (red_colour, green_colour, 0), [self.x - 75, self.y - 100, health_bar_length, 10])
        pygame.draw.rect(screen, (255, 255, 255), [self.x - 75, self.y - 100, 150, 10], 1)

    def update(self, _players):
        if self.action != "Dead" and self.action != "Dying":
            self.track_player(_players)
            self.x += self.vel * self.movement[0]
            self.y += self.vel * self.movement[1]
        if self.action == "hit":
            self.hit_sprite_count += 1
            if self.hit_sprite_count == 9:
                self.hit_sprite_count = 0
                if self.health > 50:
                    self.action = "Running"
                    self.vel = 5
                elif self.health > 0:
                    self.action = "Walking"
                    self.vel = 2
                else:
                    self.action = "Dying"
                    self.vel = 0
        if self.action == "Dying":
            if self.dying_sprite_count < self.dead_sprite_count - 1:
                self.dying_sprite_count += 1
            else:
                self.action = "Dead"

    def track_player(self, _players):
        x1 = self.x
        y1 = self.y
        distance = 1000
        target = _players[0]
        for player in _players:
            x2 = player.x
            y2 = player.y
            h = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if h < distance:
                distance = h
                target = player

        if target.x < x1 - 20:
            self.movement[0] = -1
        elif target.x > x1 + 20:
            self.movement[0] = 1
        else:
            self.movement[0] = 0

        if target.y < y1 - 20:
            self.movement[1] = -1
        elif target.y > y1 + 20:
            self.movement[1] = 1
        else:
            self.movement[1] = 0

        if self.movement == [-1, 1]:
            self.direction = 0
        elif self.movement == [-1, 0]:
            self.direction = 1
        elif self.movement == [-1, -1]:
            self.direction = 2
        elif self.movement == [0, -1]:
            self.direction = 3
        elif self.movement == [1, -1]:
            self.direction = 4
        elif self.movement == [1, 0]:
            self.direction = 5
        elif self.movement == [1, 1]:
            self.direction = 6
        elif self.movement == [0, 1]:
            self.direction = 7

    def shot(self):
        self.health -= 1
        self.action = "hit"
        self.vel = -2


class Corpse:
    def __init__(self,x,y, _type, direction):
        self.x = x
        self.y = y
        self.type = _type
        self.direction = direction

    def draw(self, screen, sprites):
        if self.type == "female":
            sprite = sprites.Zombie_female_dead
        else:
            sprite = sprites.Zombie_male_dead
        screen.blit(sprite[self.direction][-1],
                    (self.x - 250, self.y - 250))


