import pygame
import os


pygame.init()




#__WINDOW AND VARIABLES__##
WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


CYAN = (0, 59, 89)
GREEN = (144, 238, 144)
RED = (255, 0,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100,75


HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('timesnewroman', 100)


FPS = 60
VELOCITY = 5
MAX_BULLETS = 5


BULLET_SPEED = 7

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','Yellow_Spaceship.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','Red_Spaceship.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets','Space.png')), (WIDTH, HEIGHT))

BORDER = pygame.Rect((WIDTH//2)-5, 0, 10, HEIGHT)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2








#__FUNCTIONS__##
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    pygame.display.set_caption("Space Battles")
    WIN.blit(SPACE, (0, 0))

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width()-10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x , red.y))

    for bullet in red_bullets:
            pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.draw.rect(WIN, CYAN, BORDER)
    pygame.display.update()
    
def yellow_movements(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x - VELOCITY > 0: # left
        yellow.x -= VELOCITY
    if key_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < BORDER.x: # right
        yellow.x += VELOCITY
    if key_pressed[pygame.K_w] and yellow.y - VELOCITY > 0: # up
        yellow.y -= VELOCITY
    if key_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT-25:  # down
        yellow.y += VELOCITY


def red_movements(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x + BORDER.width+10 :  # left
        red.x -= VELOCITY
    if key_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH: # right
        red.x += VELOCITY
    if key_pressed[pygame.K_UP] and red.y - VELOCITY > 0:    # up
        red.y -= VELOCITY
    if key_pressed[pygame.K_DOWN] and red.y + VELOCITY + red.height < HEIGHT-25:  # down
        red.y += VELOCITY

def bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_SPEED
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_SPEED
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (
        WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(900, 330, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 330, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width-5, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RSHIFT and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)

                    BULLET_FIRE_SOUND.play()


            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

  
        winner_text = ''
        if red_health <= 0:
            winner_text = 'YELLOW WINS!'

        if yellow_health <= 0:
            winner_text = 'RED WINS!'

        if winner_text != '':
            draw_winner(winner_text)
            break


        key_pressed = pygame.key.get_pressed()

        yellow_movements(key_pressed, yellow)
        red_movements(key_pressed, red)

        bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    yellow_bullets.clear()
    red_bullets.clear()
    main()















#__MAIN__##
if __name__ == "__main__":
    main()