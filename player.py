import pygame


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, )
        self.vel = 10
        self.movement = [0, 0]
        self.center = (self.x + self.width/2, self.y + self.height/2)
        self.direction = 7
        self.action = "Idle"
        self.gun_state = "Lowered"
        self.lowered_count = 0
        self.shoot_count = 0
        self.raised_count = 0

    def draw(self, frame, screen, sprites):
        # pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, 50, 50])

        if self.gun_state == "Raised" and self.action != "Shooting":
            screen.blit(sprites.SWAT_shooting[self.direction][16 + self.raised_count],
                        (self.x - 250, self.y - 250))
            self.raised_count += 1
            if self.raised_count == 20:
                self.gun_state = "Lowered"
                self.raised_count = 0
        elif self.action == "Walking":
            screen.blit(sprites.SWAT_walking[self.direction][frame % len(sprites.SWAT_walking[self.direction])],
                        (self.x-250, self.y-250))
        elif self.action == "Idle" and self.gun_state != "Raised":
            screen.blit(sprites.SWAT_idle[self.direction][frame % len(sprites.SWAT_idle[self.direction])],
                        (self.x - 250, self.y - 250))
        elif self.action == "Shooting":
            if self.gun_state == "Lowered":
                screen.blit(sprites.SWAT_shooting[self.direction][self.lowered_count],
                            (self.x - 250, self.y - 250))
                self.lowered_count += 1
                if self.lowered_count == 11:
                    self.gun_state = "Raised"
                    self.lowered_count = 0
            if self.gun_state == "Raised":
                screen.blit(sprites.SWAT_shooting[self.direction][10 + self.shoot_count],
                            (self.x - 250, self.y - 250))
                self.shoot_count += 1
                if self.shoot_count == 6:
                    self.shoot_count = 0
        elif self.action == "Reloading":
            screen.blit(sprites.SWAT_reloading[self.direction][frame % len(sprites.SWAT_reloading[self.direction])],
                        (self.x - 250, self.y - 250))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.movement[0] = -1
        elif keys[pygame.K_d]:
            self.movement[0] = 1
        else:
            self.movement[0] = 0

        if keys[pygame.K_w]:
            self.movement[1] = -1
        elif keys[pygame.K_s]:
            self.movement[1] = 1
        else:
            self.movement[1] = 0

        if self.movement != [0, 0]:
            self.action = "Walking"

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
        else:
            self.action = "Idle"

        if keys[pygame.K_SPACE]:
            self.action = "Shooting"

        if keys[pygame.K_r]:
            self.action = "Reloading"

        if self.action != "Shooting":
            self.x += self.vel * self.movement[0]
            self.y += self.vel * self.movement[1]

    def update(self, _zombies):
        if self.action == "Shooting" and self.gun_state == "Raised":
            self.fire_shot(_zombies)
        self.rect = (self.x, self.y, self.width, self.height)
        self.center = (self.x + self.width / 2, self.y + self.height / 2)

    def fire_shot(self, _zombies):
        x1 = self.x
        y1 = self.y
        zoms_in_line = []
        for zom in _zombies:
            if self.direction == 0:
                if zom.y > y1 and zom.x < x1:
                    zoms_in_line.append(zom)
            if self.direction == 1:
                if zom.y - 100 < y1 < zom.y + 100 and zom.x < x1:
                    zoms_in_line.append(zom)
            if self.direction == 2:
                if zom.y < y1 and zom.x < x1:
                    zoms_in_line.append(zom)
            if self.direction == 3:
                if zom.y < y1 and zom.x - 100 < x1 < zom.x + 100:
                    zoms_in_line.append(zom)
            if self.direction == 4:
                if zom.y < y1 and zom.x > x1:
                    zoms_in_line.append(zom)
            if self.direction == 5:
                if zom.y - 100 < y1 < zom.y + 100 and zom.x > x1:
                    zoms_in_line.append(zom)
            if self.direction == 6:
                if zom.y > y1 and zom.x > x1:
                    zoms_in_line.append(zom)
            if self.direction == 7:
                if zom.y > y1 and zom.x - 100 < x1 < zom.x + 100:
                    zoms_in_line.append(zom)

        if zoms_in_line:
            distance = 1000
            target = zoms_in_line[0]
            for zom in zoms_in_line:
                x2 = zom.x
                y2 = zom.y
                h = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                if h < distance:
                    distance = h
                    target = zom

            target.shot()
