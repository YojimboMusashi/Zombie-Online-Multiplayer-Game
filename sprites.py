import pygame

pygame.font.init()


class Sprites:
    def __init__(self, screen):
        self.screen = screen
        font = pygame.font.SysFont("Calibri", 48)
        loading_text = font.render("Loading Male Zombies", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 0, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_dead1 = []
        ver = "01"
        for img in range(43):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_dead1.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_dead1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_dead1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 1, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_dead2 = []
        ver = "02"
        for img in range(43):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_dead2.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_dead2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_dead2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 2, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_dead3 = []
        ver = "03"
        for img in range(43):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_dead3.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_dead3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_dead3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 3, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_dead4 = []
        ver = "04"
        for img in range(43):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_dead4.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_dead4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_dead4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 4, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_dead5 = []
        ver = "05"
        for img in range(43):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_dead5.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_dead5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_dead5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 5, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_dead6 = []
        ver = "06"
        for img in range(43):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_dead6.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_dead6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_dead6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 6, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_dead7 = []
        ver = "07"
        for img in range(43):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_dead7.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_dead7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_dead7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 7, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_dead8 = []
        ver = "08"
        for img in range(43):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_dead8.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_dead8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_dead8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 8, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_hit1 = []
        ver = "01"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_hit1.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_hit1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_hit1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 9, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_hit2 = []
        ver = "02"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_hit2.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_hit2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_hit2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 10, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_hit3 = []
        ver = "03"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_hit3.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_hit3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_hit3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 11, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_hit4 = []
        ver = "04"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_hit4.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_hit4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_hit4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 12, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_hit5 = []
        ver = "05"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_hit5.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_hit5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_hit5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 13, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_hit6 = []
        ver = "06"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_hit6.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_hit6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_hit6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 14, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_hit7 = []
        ver = "07"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_hit7.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_hit7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_hit7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 15, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_hit8 = []
        ver = "08"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_hit8.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_hit8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_hit8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 16, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_run1 = []
        ver = "01"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_run1.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_run1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_run1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 17, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_run2 = []
        ver = "02"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_run2.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_run2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_run2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 18, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_run3 = []
        ver = "03"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_run3.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_run3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_run3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 19, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_run4 = []
        ver = "04"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_run4.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_run4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_run4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 20, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_run5 = []
        ver = "05"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_run5.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_run5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_run5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 21, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_run6 = []
        ver = "06"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_run6.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_run6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_run6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 22, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_run7 = []
        ver = "07"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_run7.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_run7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_run7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 23, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_run8 = []
        ver = "08"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_run8.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_run8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_run8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 24, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_walk1 = []
        ver = "01"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_walk1.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_walk1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_walk1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 25, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_walk2 = []
        ver = "02"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_walk2.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_walk2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_walk2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 26, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_walk3 = []
        ver = "03"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_walk3.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_walk3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_walk3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 27, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_walk4 = []
        ver = "04"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_walk4.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_walk4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_walk4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 28, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_walk5 = []
        ver = "05"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_walk5.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_walk5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_walk5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 29, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_walk6 = []
        ver = "06"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_walk6.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_walk6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_walk6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 30, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_walk7 = []
        ver = "07"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_walk7.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_walk7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_walk7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 31, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_walk8 = []
        ver = "08"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_male_walk8.append(
                pygame.image.load(
                    "Zombie_male/zombie_male_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_male_walk8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_male_walk8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 32, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_male_dead = [self.Zombie_male_dead1, self.Zombie_male_dead2,
                                 self.Zombie_male_dead3, self.Zombie_male_dead4,
                                 self.Zombie_male_dead5, self.Zombie_male_dead6,
                                 self.Zombie_male_dead7, self.Zombie_male_dead8]
        self.Zombie_male_hit = [self.Zombie_male_hit1, self.Zombie_male_hit2,
                                self.Zombie_male_hit3, self.Zombie_male_hit4,
                                self.Zombie_male_hit5, self.Zombie_male_hit6,
                                self.Zombie_male_hit7, self.Zombie_male_hit8]
        self.Zombie_male_running = [self.Zombie_male_run1, self.Zombie_male_run2,
                                    self.Zombie_male_run3, self.Zombie_male_run4,
                                    self.Zombie_male_run5, self.Zombie_male_run6,
                                    self.Zombie_male_run7, self.Zombie_male_run8]
        self.Zombie_male_walking = [self.Zombie_male_walk1, self.Zombie_male_walk2,
                                    self.Zombie_male_walk3, self.Zombie_male_walk4,
                                    self.Zombie_male_walk5, self.Zombie_male_walk6,
                                    self.Zombie_male_walk7, self.Zombie_male_walk8]

        self.Zombie_female_dead1 = []
        ver = "01"
        for img in range(32):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_dead1.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_dead1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text = font.render("Loading Female Zombies", True, (255, 255, 255))
        loading_text2 = font.render("Zombie_female_dead1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 33, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_dead2 = []
        ver = "02"
        for img in range(32):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_dead2.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_dead2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_dead2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 34, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_dead3 = []
        ver = "03"
        for img in range(32):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_dead3.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_dead3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_dead3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 35, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_dead4 = []
        ver = "04"
        for img in range(32):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_dead4.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_dead4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_dead4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 36, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_dead5 = []
        ver = "05"
        for img in range(32):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_dead5.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_dead5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_dead5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 37, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_dead6 = []
        ver = "06"
        for img in range(32):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_dead6.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_dead6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_dead6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 38, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_dead7 = []
        ver = "07"
        for img in range(32):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_dead7.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_dead7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_dead7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 39, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_dead8 = []
        ver = "08"
        for img in range(32):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_dead8.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_dead_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_dead8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_dead8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 40, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_hit1 = []
        ver = "01"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_hit1.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_hit1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_hit1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 41, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_hit2 = []
        ver = "02"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_hit2.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_hit2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_hit2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 42, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_hit3 = []
        ver = "03"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_hit3.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_hit3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_hit3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 43, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_hit4 = []
        ver = "04"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_hit4.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_hit4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_hit4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 44, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_hit5 = []
        ver = "05"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_hit5.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_hit5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_hit5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 45, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_hit6 = []
        ver = "06"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_hit6.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_hit6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_hit6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 46, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_hit7 = []
        ver = "07"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_hit7.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_hit7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_hit7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 47, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_hit8 = []
        ver = "08"
        for img in range(9):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_hit8.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_hit_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_hit8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_hit8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 48, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_run1 = []
        ver = "01"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_run1.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_run1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_run1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 49, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_run2 = []
        ver = "02"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_run2.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_run2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_run2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 50, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_run3 = []
        ver = "03"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_run3.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_run3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_run3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 51, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_run4 = []
        ver = "04"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_run4.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_run4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_run4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 52, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_run5 = []
        ver = "05"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_run5.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_run5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_run5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 53, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_run6 = []
        ver = "06"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_run6.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_run6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_run6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 54, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_run7 = []
        ver = "07"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_run7.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_run7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_run7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 55, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_run8 = []
        ver = "08"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_run8.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_run_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_run8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_run8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 56, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_walk1 = []
        ver = "01"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_walk1.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_walk1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_walk1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 57, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_walk2 = []
        ver = "02"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_walk2.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_walk2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_walk2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 58, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_walk3 = []
        ver = "03"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_walk3.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_walk3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_walk3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 59, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_walk4 = []
        ver = "04"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_walk4.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_walk4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_walk4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 60, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_walk5 = []
        ver = "05"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_walk5.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_walk5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_walk5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 61, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_walk6 = []
        ver = "06"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_walk6.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_walk6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_walk6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 62, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_walk7 = []
        ver = "07"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_walk7.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_walk7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_walk7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 63, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_walk8 = []
        ver = "08"
        for img in range(35):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.Zombie_female_walk8.append(
                pygame.image.load(
                    "Zombie_female/zombie_female_walk_v" + str(ver) + "_" + str(
                        num) + ".png"))

        print("Zombie_female_walk8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("Zombie_female_walk8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 64, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.Zombie_female_dead = [self.Zombie_female_dead1, self.Zombie_female_dead2,
                                   self.Zombie_female_dead3, self.Zombie_female_dead4,
                                   self.Zombie_female_dead5, self.Zombie_female_dead6,
                                   self.Zombie_female_dead7, self.Zombie_female_dead8]
        self.Zombie_female_hit = [self.Zombie_female_hit1, self.Zombie_female_hit2,
                                  self.Zombie_female_hit3, self.Zombie_female_hit4,
                                  self.Zombie_female_hit5, self.Zombie_female_hit6,
                                  self.Zombie_female_hit7, self.Zombie_female_hit8]
        self.Zombie_female_running = [self.Zombie_female_run1, self.Zombie_female_run2,
                                      self.Zombie_female_run3, self.Zombie_female_run4,
                                      self.Zombie_female_run5, self.Zombie_female_run6,
                                      self.Zombie_female_run7, self.Zombie_female_run8]
        self.Zombie_female_walking = [self.Zombie_female_walk1, self.Zombie_female_walk2,
                                      self.Zombie_female_walk3, self.Zombie_female_walk4,
                                      self.Zombie_female_walk5, self.Zombie_female_walk6,
                                      self.Zombie_female_walk7, self.Zombie_female_walk8]

        self.SWAT_idle1 = []
        ver = "01"
        for img in range(75):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_idle1.append(pygame.image.load("SWAT_soldier/swat_idle_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_idle1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text = font.render("Loading SWAT team", True, (255, 255, 255))
        loading_text2 = font.render("SWAT_idle1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 65, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_idle2 = []
        ver = "02"
        for img in range(75):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_idle2.append(pygame.image.load("SWAT_soldier/swat_idle_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_idle2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_idle2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 66, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_idle3 = []
        ver = "03"
        for img in range(75):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_idle3.append(pygame.image.load("SWAT_soldier/swat_idle_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_idle3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_idle3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 67, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_idle4 = []
        ver = "04"
        for img in range(75):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_idle4.append(pygame.image.load("SWAT_soldier/swat_idle_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_idle4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_idle4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 68, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_idle5 = []
        ver = "05"
        for img in range(75):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_idle5.append(pygame.image.load("SWAT_soldier/swat_idle_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_idle5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_idle5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 69, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_idle6 = []
        ver = "06"
        for img in range(75):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_idle6.append(pygame.image.load("SWAT_soldier/swat_idle_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_idle6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_idle6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 70, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_idle7 = []
        ver = "07"
        for img in range(75):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_idle7.append(pygame.image.load("SWAT_soldier/swat_idle_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_idle7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_idle7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 71, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_idle8 = []
        ver = "08"
        for img in range(75):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_idle8.append(pygame.image.load("SWAT_soldier/swat_idle_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_idle8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_idle8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 72, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_recharge1 = []
        ver = "01"
        for img in range(30):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_recharge1.append(
                pygame.image.load("SWAT_soldier/swat_recharge_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_recharge1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_recharge1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 73, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_recharge2 = []
        ver = "02"
        for img in range(30):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_recharge2.append(
                pygame.image.load("SWAT_soldier/swat_recharge_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_recharge2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_recharge2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 74, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_recharge3 = []
        ver = "03"
        for img in range(30):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_recharge3.append(
                pygame.image.load("SWAT_soldier/swat_recharge_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_recharge3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_recharge3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 75, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_recharge4 = []
        ver = "04"
        for img in range(30):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_recharge4.append(
                pygame.image.load("SWAT_soldier/swat_recharge_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_recharge4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_recharge4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 76, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_recharge5 = []
        ver = "05"
        for img in range(30):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_recharge5.append(
                pygame.image.load("SWAT_soldier/swat_recharge_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_recharge5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_recharge5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 77, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_recharge6 = []
        ver = "06"
        for img in range(30):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_recharge6.append(
                pygame.image.load("SWAT_soldier/swat_recharge_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_recharge6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_recharge6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 78, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_recharge7 = []
        ver = "07"
        for img in range(30):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_recharge7.append(
                pygame.image.load("SWAT_soldier/swat_recharge_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_recharge7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_recharge7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 79, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_recharge8 = []
        ver = "08"
        for img in range(30):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_recharge8.append(
                pygame.image.load("SWAT_soldier/swat_recharge_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_recharge8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_recharge8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 80, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_shooting1 = []
        ver = "01"
        for img in range(36):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_shooting1.append(
                pygame.image.load("SWAT_soldier/swat_shooting_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_shooting1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_shooting1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 81, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_shooting2 = []
        ver = "02"
        for img in range(36):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_shooting2.append(
                pygame.image.load("SWAT_soldier/swat_shooting_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_shooting2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_shooting2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 82, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_shooting3 = []
        ver = "03"
        for img in range(36):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_shooting3.append(
                pygame.image.load("SWAT_soldier/swat_shooting_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_shooting3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_shooting3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 83, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_shooting4 = []
        ver = "04"
        for img in range(36):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_shooting4.append(
                pygame.image.load("SWAT_soldier/swat_shooting_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_shooting4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_shooting4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 84, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_shooting5 = []
        ver = "05"
        for img in range(36):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_shooting5.append(
                pygame.image.load("SWAT_soldier/swat_shooting_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_shooting5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_shooting5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 85, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_shooting6 = []
        ver = "06"
        for img in range(36):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_shooting6.append(
                pygame.image.load("SWAT_soldier/swat_shooting_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_shooting6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_shooting6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 86, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_shooting7 = []
        ver = "07"
        for img in range(36):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_shooting7.append(
                pygame.image.load("SWAT_soldier/swat_shooting_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_shooting7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_shooting7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 87, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_shooting8 = []
        ver = "08"
        for img in range(36):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_shooting8.append(
                pygame.image.load("SWAT_soldier/swat_shooting_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_shooting8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_shooting8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 88, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_walking1 = []
        ver = "01"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_walking1.append(
                pygame.image.load("SWAT_soldier/swat_walk_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_walking1 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_walking1 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 89, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_walking2 = []
        ver = "02"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_walking2.append(
                pygame.image.load("SWAT_soldier/swat_walk_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_walking2 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_walking2 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 90, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_walking3 = []
        ver = "03"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_walking3.append(
                pygame.image.load("SWAT_soldier/swat_walk_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_walking3 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_walking3 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 91, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_walking4 = []
        ver = "04"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_walking4.append(
                pygame.image.load("SWAT_soldier/swat_walk_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_walking4 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_walking4 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 92, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_walking5 = []
        ver = "05"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_walking5.append(
                pygame.image.load("SWAT_soldier/swat_walk_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_walking5 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_walking5 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 93, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_walking6 = []
        ver = "06"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_walking6.append(
                pygame.image.load("SWAT_soldier/swat_walk_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_walking6 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_walking6 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 94, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_walking7 = []
        ver = "07"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_walking7.append(
                pygame.image.load("SWAT_soldier/swat_walk_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_walking7 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_walking7 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 95, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_walking8 = []
        ver = "08"
        for img in range(25):
            if len(str(img)) < 2:
                num = "0" + str(img)
            else:
                num = str(img)
            self.SWAT_walking8.append(
                pygame.image.load("SWAT_soldier/swat_walk_v" + str(ver) + "_" + str(num) + ".png"))

        print("SWAT_walking8 loaded")
        self.screen.fill((0, 0, 0))
        loading_text2 = font.render("SWAT_walking8 loaded", True, (255, 255, 255))
        self.screen.blit(loading_text, (600, 400))
        self.screen.blit(loading_text2, (600, 440))
        pygame.draw.rect(screen, (0, 0, 150), [100, 700, (1400 / 96) * 96, 50])
        pygame.draw.rect(screen, (255, 255, 255), [100, 700, 1400, 50], 2)
        pygame.display.flip()

        self.SWAT_idle = [self.SWAT_idle1, self.SWAT_idle2, self.SWAT_idle3, self.SWAT_idle4,
                          self.SWAT_idle5, self.SWAT_idle6, self.SWAT_idle7, self.SWAT_idle8]
        self.SWAT_reloading = [self.SWAT_recharge1, self.SWAT_recharge2, self.SWAT_recharge3, self.SWAT_recharge4,
                               self.SWAT_recharge5, self.SWAT_recharge6, self.SWAT_recharge7, self.SWAT_recharge8]
        self.SWAT_shooting = [self.SWAT_shooting1, self.SWAT_shooting2, self.SWAT_shooting3, self.SWAT_shooting4,
                              self.SWAT_shooting5, self.SWAT_shooting6, self.SWAT_shooting7, self.SWAT_shooting8]
        self.SWAT_walking = [self.SWAT_walking1, self.SWAT_walking2, self.SWAT_walking3, self.SWAT_walking4,
                             self.SWAT_walking5, self.SWAT_walking6, self.SWAT_walking7, self.SWAT_walking8]
