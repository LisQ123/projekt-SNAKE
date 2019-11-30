import pygame
import sys
import random
import time

pygame.init()


class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"

    def changedirto(self, dir):
        """ zasady skrecania """
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        elif dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        elif dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        elif dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, foodpos):
        """ poruszanie sie """
        if self.direction == "RIGHT":
            self.position[0] = self.position[0] + 10
        elif self.direction == "LEFT":
            self.position[0] = self.position[0] - 10
        elif self.direction == "UP":
            self.position[1] = self.position[1] - 10
        elif self.direction == "DOWN":
            self.position[1] = self.position[1] + 10
        self.body.insert(0, list(self.position))

        if self.position == foodpos:
            return 1
        else:
            self.body.pop()
            return 0

    def move_right(self):
        self.position[0] = self.position[0] + 10

    def move_left(self):
        self.position[0] = self.position[0] - 10

    def move_up(self):
        self.position[0] = self.position[1] - 10

    def move_down(self):
        self.position[0] = self.position[1] + 10

    def checkcollision(self):
        """ kolizje """
        if self.position[0] > 490 or self.position[0] < 10:
            return 1
        elif self.position[1] > 500 or self.position[1] < 10:
            return 1
        for bodypart in self.body[1:]:
            if self.position == bodypart:
                return 1
        return 0

    def getheadposition(self):
        return self.position

    def getbody(self):
        return self.body


class Foodspawn:
    """ jedzonko """
    def __init__(self):
        self.position = [random.randint(4, 46) * 10, random.randint(4, 46) * 10]
        self.isfoodonscreen = True

    def spawnfood(self):
        """ losowa lokalizacja jedzenia """
        if not self.isfoodonscreen:
            self.position = [random.randrange(4, 46) * 10, random.randrange(4, 46) * 10]
            self.isfoodonscreen = True
        return self.position

    def setfoodonscreen(self, b):
        self.isfoodonscreen = b


window = pygame.display.set_mode((500 + 20, 500 + 20))
pygame.display.set_caption('SNAKE made by LisQ')
fps = pygame.time.Clock()

score = 0

snake = Snake()
foodspawner = Foodspawn()


# konniec
def gameover():
    font = pygame.font.SysFont('BROADWAY', 20)
    score_text = font.render('Gameover! You earned ' + str(score) + ' points!', 4, (255, 0, 0))
    window.blit(score_text, (100, 250))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


 # 'serce' gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT]:
            snake.changedirto('RIGHT')
        elif pressed[pygame.K_LEFT]:
            snake.changedirto('LEFT')
        elif pressed[pygame.K_UP]:
            snake.changedirto('UP')
        elif pressed[pygame.K_DOWN]:
            snake.changedirto('DOWN')
        elif pressed[pygame.K_ESCAPE]:
            gameover()

    foodpos = foodspawner.spawnfood()
    if snake.move(foodpos) == 1:
        score += 1
        foodspawner.setfoodonscreen(False)

    window.fill(pygame.Color(255, 182, 193))
    for x in range(0, 510, 10):
        pygame.draw.rect(window, (85, 26, 139), [x, 0, 10, 10])
        pygame.draw.rect(window, (85, 26, 139), [x, 510, 10, 10])

    for x in range(0, 510, 10):
        pygame.draw.rect(window, (85, 26, 139), [0, x, 10, 10])
        pygame.draw.rect(window, (85, 26, 139), [510, x, 10, 10])

    for pos in snake.getbody():
        pygame.draw.rect(window, pygame.Color(0, 100, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, pygame.Color(220, 20, 60), pygame.Rect(foodpos[0], foodpos[1], 10, 10))

    if snake.checkcollision() == 1:
        gameover()

    pygame.display.set_caption('Snake | Score: ' + str(score))
    pygame.display.flip()
    fps.tick(20)
