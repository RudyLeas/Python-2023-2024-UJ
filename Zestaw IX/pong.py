import pygame
import random


pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
player_paddle = pygame.Rect(WIDTH - 2 * PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(0, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# ball
BALL_SIZE = 15
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed = [5 * random.choice((1, -1)), 5 * random.choice((1, -1))]

# score
player_score = 0
opponent_score = 0
#mozna uruchomic gre bez czcionki komentujac ta linijke i odkomentowujac ponizsza
font = pygame.font.Font("font.ttf", 20)
#font = pygame.font.Font(None, 36)


def choose_game_mode():
    mode_selected = False

    while not mode_selected:
        title_text = font.render("Wybierz tryb klawiszami:", True, WHITE)
        WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        player_vs_player_text = font.render("1. Gra dwóch graczy", True, WHITE)
        player_vs_computer_text = font.render("2. Gra przeciwko komputerowi", True, WHITE)

        WIN.blit(player_vs_player_text, (WIDTH // 2 - player_vs_player_text.get_width() // 2, 200))
        WIN.blit(player_vs_computer_text, (WIDTH // 2 - player_vs_computer_text.get_width() // 2, 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "player_vs_player"
                elif event.key == pygame.K_2:
                    return "player_vs_computer"


# Funkcja rysująca paletki, piłkę i wyniki
def draw_elements():
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, player_paddle)
    pygame.draw.rect(WIN, WHITE, opponent_paddle)
    pygame.draw.ellipse(WIN, WHITE, ball)
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    WIN.blit(player_text, (WIDTH - 50, 20))
    WIN.blit(opponent_text, (30, 20))


def player1_move(keys):
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= 5
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += 5

def opponent_move():
    if opponent_paddle.centery < ball.centery:
        opponent_paddle.y += 3
    if opponent_paddle.centery > ball.centery:
        opponent_paddle.y -= 3


def player2_move(keys):
    if keys[pygame.K_w] and opponent_paddle.top > 0:
        opponent_paddle.y -= 5
    if keys[pygame.K_s] and opponent_paddle.bottom < HEIGHT:
        opponent_paddle.y += 5


def main():
    clock = pygame.time.Clock()
    global player_score, opponent_score
    game_mode = choose_game_mode()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        player1_move(keys)

        if game_mode == "player_vs_computer":
            opponent_move()
        elif game_mode == "player_vs_player":
            player2_move(keys)
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]
        if ball.colliderect(player_paddle):
            ball_speed[0] *= -1
        if ball.colliderect(opponent_paddle):
            ball_speed[0] *= -1
        if ball.left <= 0:
            player_score += 1
            reset_ball()
        if ball.right >= WIDTH:
            opponent_score += 1
            reset_ball()
        if player_score == 11 or opponent_score == 11:
            print("Koniec gry!")
            pygame.quit()
            exit()

        draw_elements()
        pygame.display.flip()
        clock.tick(60)


def reset_ball():
    global ball_speed
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed = [5 * random.choice((1, -1)), 5 * random.choice((1, -1))]


if __name__ == "__main__":
    main()
