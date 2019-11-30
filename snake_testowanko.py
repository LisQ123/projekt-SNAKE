import pygame, random, sys, time

pygame.init()

  # window size
hight = 600
lenght = 600
window = pygame.display.set_mode((hight, lenght))
  # ekran
pygame.display.set_caption('SNAKE made by LisQ')
background = pygame.image.load('tlo.jpg')   # tlo
screen = pygame.display.get_surface()
screen.blit(background, (0, 0))  # tlo
pygame.display.flip()

snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]  #lokalizacja weza

food_pos = [random.randrange(1, (hight//10)) * 10, random.randrange(1, (lenght//10)) * 10]
food_spawn = True   # jedzonko

direction = 'RIGHT'
change_to = direction
score = 0

  # kolorki i czcionka
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 100, 0)
lightgreen = (0, 255, 0)
my_font = pygame.font.SysFont('BROADWAY', 90)


class Move:
    """ Ruch dla weza """
    x = 10
    y = 10
    speed = 1

    def move_right(self):
        self.x = self.x + self.speed

    def move_left(self):
        self.x = self.x - self.speed

    def move_up(self):
        self.y = self.y + self.speed

    def move_down(self):
        self.y = self.y - self.speed

  # koniec gry
def game_over():
    game_over_surface = my_font.render('You have just died!', True, red)
    gave_over_rect = game_over_surface.get_rect()
    screen.fill(black)
    screen.blit(game_over_surface, gave_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


  # punktacja
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (hight/10, 15)
    else:
        score_rect.midtop = (hight/2, lenght/1.25)
    screen.blit(score_surface, score_rect)


def growing():
    pass


# class Food:
#     def foods(self):
#         pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:  # mozliwosc wylaczania gry ESC
            if event.key == pygame.K_ESCAPE:
                running = False
pygame.quit()

