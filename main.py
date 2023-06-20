import pygame as pg
import sys
import time
import random

pg.font.init()
pg.init()

NB_COL = 30  # Nombre de colonnes
NB_ROW = 30  # Nombre de lignes
CELL_SIZE = 20  # Taille de la cellule

# La scène de jeu, c'est la fenêtre principale
game_screen = pg.display.set_mode((600, 800))
pg.display.set_caption("Snake Game")  # Titre de la fenêtre
timer = pg.time.Clock()  # Définition du Timer
info_game_surface = pg.Surface((600, 200))

text_font_title = pg.font.SysFont("monospace", 30, True)
text_font_score = pg.font.SysFont("monospace", 30, True)
title_text = text_font_title.render("Snake Game", True, (0, 0, 0))

# Loading image and resizing
opening = pg.image.load('Images/opening.png')
opening = pg.transform.scale(opening, (600, 800))


def game_opening():
    game_screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(2)


game_opening()


def game_paused():
    paused = True
    text_font_pause = pg.font.SysFont("monospace", 30, True)
    paused_text = text_font_pause.render("Game Paused", True, (255, 255, 255))
    continue_text = text_font_pause.render(
        "Appuyer ECHAP pour continuer", True, (255, 0, 0))
    pause_image = pg.image.load('Images/clin_oeil.png')
    pause_image = pg.transform.scale(pause_image, (80, 80))
    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    paused = False

        game_screen.fill(pg.Color("black"))
        game_screen.blit(paused_text, (200, 300))
        game_screen.blit(continue_text, (40, 350))
        game_screen.blit(pause_image, (250, 400))
        pg.display.update()


def notice_game():
    game_notice_bool = True
    while game_notice_bool:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    game_notice_bool = False

        game_screen.fill(pg.Color("lightblue"))
        text_font_notice = pg.font.SysFont("monospace", 25, True)
        notice1_text = text_font_notice.render(
            "Le but du jeu est de diriger un serpent", True, (0, 0, 0))
        notice2_text = text_font_notice.render(
            "pour manger des aliments sans heurter", True, (0, 0, 0))
        notice3_text = text_font_notice.render(
            "les bords ou le corps du serpent.", True, (0, 0, 0))
        notice4_text = text_font_notice.render(
            "Chaque fois que le serpent mange une", True, (0, 0, 0))
        notice5_text = text_font_notice.render(
            "pomme, il grandit.", True, (0, 0, 0))
        notice6_text = text_font_notice.render(
            "Les règles du jeu incluent :", True, (0, 0, 0))
        notice7_text = text_font_notice.render(
            "-> Diriger le serpent à travers un", True, (0, 0, 0))
        notice8_text = text_font_notice.render(
            "terrain en évitant les bords et le", True, (0, 0, 0))
        notice9_text = text_font_notice.render(
            "corps du serpent.", True, (0, 0, 0))
        notice10_text = text_font_notice.render(
            "-> Manger des aliments pour faire", True, (0, 0, 0))
        notice11_text = text_font_notice.render(
            "grandir le serpent.", True, (0, 0, 0))
        notice12_text = text_font_notice.render(
            "-> Le jeu se termine lorsque le", True, (0, 0, 0))
        notice13_text = text_font_notice.render(
            "serpent heurte un bord de la grille", True, (0, 0, 0))
        notice14_text = text_font_notice.render(
            "ou son propre corps.", True, (0, 0, 0))
        notice15_text = text_font_notice.render(
            "+ Appuyez ENTRER pour commencer.", True, (0, 0, 0))
        notice16_text = text_font_notice.render(
            "+ Appuyez ESPACE pour mettre pause.", True, (0, 0, 0))
        notice17_text = text_font_notice.render(
            "+ Appuyez ECHAP pour continuer.", True, (0, 0, 0))
        game_screen.blit(notice1_text, (10, 30))
        game_screen.blit(notice2_text, (10, 70))
        game_screen.blit(notice3_text, (10, 110))
        game_screen.blit(notice4_text, (10, 150))
        game_screen.blit(notice5_text, (10, 190))
        game_screen.blit(notice6_text, (10, 260))
        game_screen.blit(notice7_text, (15, 300))
        game_screen.blit(notice8_text, (10, 340))
        game_screen.blit(notice9_text, (10, 380))
        game_screen.blit(notice10_text, (15, 420))
        game_screen.blit(notice11_text, (10, 460))
        game_screen.blit(notice12_text, (15, 500))
        game_screen.blit(notice13_text, (10, 540))
        game_screen.blit(notice14_text, (10, 580))
        game_screen.blit(notice15_text, (10, 650))
        game_screen.blit(notice16_text, (10, 690))
        game_screen.blit(notice17_text, (10, 730))
        pg.display.update()


notice_game()


def draw_grid():
    block_image = pg.image.load('Images/block.png')
    block_image = pg.transform.scale(block_image, (CELL_SIZE, CELL_SIZE))

    for index in range(0, NB_COL):
        game_screen.blit(block_image, (index * CELL_SIZE, 0 * CELL_SIZE))

    for index in range(0, NB_COL):
        game_screen.blit(
            block_image,
            (index * CELL_SIZE,
             (NB_COL - 1) * CELL_SIZE))

    for index in range(0, NB_COL):
        game_screen.blit(block_image, (0 * CELL_SIZE, index * CELL_SIZE))

    for index in range(0, NB_COL):
        game_screen.blit(
            block_image,
            ((NB_COL - 1) * CELL_SIZE,
             index * CELL_SIZE))


class Block:  # Représenter une cellule de la grille de jeu
    def __init__(self, col_position, row_position):
        self.col = col_position
        self.row = row_position
        
class Obstacle:
    def __init__(self):
        self.obstacle_block = [
            Block(1, 8), Block(2, 8), Block(3, 8), Block(4, 8), Block(5, 8),
            Block(6, 8), Block(7, 8), Block(8, 8), Block(9, 8), Block(10, 8),
            Block(11, 8), Block(20, 1), Block(20, 2), Block(20, 3),
            Block(20, 4), Block(20, 5), Block(20, 6), Block(20, 7),
            Block(20, 8), Block(20, 9), Block(20, 10), Block(9, 28),
            Block(9, 28), Block(9, 27), Block(9, 26), Block(9, 25),
            Block(9, 24), Block(9, 23), Block(9, 22), Block(9, 21),
            Block(9, 20), Block(9, 19), Block(28, 21), Block(27, 21),
            Block(26, 21), Block(25, 21), Block(24, 21), Block(23, 21),
            Block(22, 21), Block(21, 21), Block(20, 21), Block(19, 21),
            Block(18, 21)]
        
    def draw_obstacle(self):
        brique_image = pg.image.load('Images/brique.png')
        brique_image = pg.transform.scale(brique_image, (CELL_SIZE, CELL_SIZE))

        for block in self.obstacle_block:
            game_screen.blit(
                brique_image,
                (block.col * CELL_SIZE,
                 block.row * CELL_SIZE))
        
            
class snake_food:
    def __init__(self):
        col = random.randint(1, NB_COL - 2)
        row = random.randint(1, NB_ROW - 2)
        self.block_food = Block(col, row)

    def draw_snake_food(self):
        food_img = pg.image.load('Images/snake_food.png')
        food_img = pg.transform.scale(food_img, (CELL_SIZE, CELL_SIZE))
        game_screen.blit(
            food_img,
            (self.block_food.col *
             CELL_SIZE,
             self.block_food.row *
             CELL_SIZE))
        
        
class Snake:
    def __init__(self):
        self.body = [Block(2, 6), Block(3, 6), Block(4, 6)]
        self.direction = "RIGHT"

    def draw_snake(self):
        right_head_snake = pg.image.load('Images/head_right.png')
        right_head_snake = pg.transform.scale(
            right_head_snake, (CELL_SIZE, CELL_SIZE))
        left_head_snake = pg.image.load('Images/head_left.png')
        left_head_snake = pg.transform.scale(
            left_head_snake, (CELL_SIZE, CELL_SIZE))
        up_head_snake = pg.image.load('Images/head_up.png')
        up_head_snake = pg.transform.scale(
            up_head_snake, (CELL_SIZE, CELL_SIZE))
        down_head_snake = pg.image.load('Images/head_down.png')
        down_head_snake = pg.transform.scale(
            down_head_snake, (CELL_SIZE, CELL_SIZE))

        vertical_body_snake = pg.image.load('Images/body_vertical.png')
        vertical_body_snake = pg.transform.scale(
            vertical_body_snake, (CELL_SIZE, CELL_SIZE))
        horizontal_body_snake = pg.image.load('Images/body_horizontal.png')
        horizontal_body_snake = pg.transform.scale(
            horizontal_body_snake, (CELL_SIZE, CELL_SIZE))

        right_body_snake = pg.image.load('Images/body_bl.png')
        right_body_snake = pg.transform.scale(
            right_body_snake, (CELL_SIZE, CELL_SIZE))
        left_body_snake = pg.image.load('Images/body_br.png')
        left_body_snake = pg.transform.scale(
            left_body_snake, (CELL_SIZE, CELL_SIZE))
        up_body_snake = pg.image.load('Images/body_tl.png')
        up_body_snake = pg.transform.scale(
            up_body_snake, (CELL_SIZE, CELL_SIZE))
        down_body_snake = pg.image.load('Images/body_tr.png')
        down_body_snake = pg.transform.scale(
            down_body_snake, (CELL_SIZE, CELL_SIZE))

        right_tail_snake = pg.image.load('Images/tail_right.png')
        right_tail_snake = pg.transform.scale(
            right_tail_snake, (CELL_SIZE, CELL_SIZE))
        left_tail_snake = pg.image.load('Images/tail_left.png')
        left_tail_snake = pg.transform.scale(
            left_tail_snake, (CELL_SIZE, CELL_SIZE))
        up_tail_snake = pg.image.load('Images/tail_up.png')
        up_tail_snake = pg.transform.scale(
            up_tail_snake, (CELL_SIZE, CELL_SIZE))
        down_tail_snake = pg.image.load('Images/tail_down.png')
        down_tail_snake = pg.transform.scale(
            down_tail_snake, (CELL_SIZE, CELL_SIZE))

        for index, block in enumerate(self.body):
            if index == 0:
                nxt_block = self.body[index + 1]

                if block.row == nxt_block.row and block.col < nxt_block.col:
                    game_screen.blit(
                        left_tail_snake, (block.col * CELL_SIZE, block.row *
                                          CELL_SIZE))
                elif block.row == nxt_block.row and block.col > nxt_block.col:
                    game_screen.blit(
                        right_tail_snake, (block.col * CELL_SIZE, block.row *
                                           CELL_SIZE))
                elif block.col == nxt_block.col and block.row < nxt_block.row:
                    game_screen.blit(
                        up_tail_snake, (block.col * CELL_SIZE, block.row *
                                        CELL_SIZE))
                elif block.col == nxt_block.col and block.row > nxt_block.row:
                    game_screen.blit(
                        down_tail_snake, (block.col * CELL_SIZE, block.row *
                                          CELL_SIZE))
            elif index == len(self.body) - 1:
                if self.direction == "RIGHT":
                    game_screen.blit(
                        right_head_snake, (block.col * CELL_SIZE, block.row *
                                           CELL_SIZE))
                elif self.direction == "LEFT":
                    game_screen.blit(
                        left_head_snake, (block.col * CELL_SIZE, block.row *
                                          CELL_SIZE))
                elif self.direction == "TOP":
                    game_screen.blit(
                        up_head_snake, (block.col * CELL_SIZE, block.row * 
                                        CELL_SIZE))
                else:
                    game_screen.blit(
                        down_head_snake, (block.col * CELL_SIZE, block.row *
                                          CELL_SIZE))
            else:
                previous_block = self.body[index - 1]
                next_block = self.body[index + 1]

                if previous_block.col == next_block.col:
                    game_screen.blit(
                        vertical_body_snake,
                        (block.col * CELL_SIZE,
                         block.row * CELL_SIZE))
                elif previous_block.row == next_block.row:
                    game_screen.blit(
                        horizontal_body_snake,
                        (block.col * CELL_SIZE,
                         block.row * CELL_SIZE))
                else:
                    if (previous_block.row == block.row and previous_block.row < next_block.row) and (previous_block.col < block.col and block.col == next_block.col):
                        game_screen.blit(right_body_snake, (block.col * CELL_SIZE, block.row * CELL_SIZE))
                    elif (previous_block.row == block.row and previous_block.row > next_block.row) and (previous_block.col < block.col and block.col == next_block.col):
                        game_screen.blit(up_body_snake, (block.col * CELL_SIZE, block.row * CELL_SIZE))
                    elif (previous_block.row < block.row and previous_block.row < next_block.row) and (previous_block.col == block.col and block.col < next_block.col):
                        game_screen.blit(down_body_snake, (block.col * CELL_SIZE, block.row * CELL_SIZE))
                    elif (previous_block.row < block.row and previous_block.row < next_block.row) and (previous_block.col == block.col and block.col > next_block.col):
                        game_screen.blit(up_body_snake, (block.col * CELL_SIZE, block.row * CELL_SIZE))
                    elif (previous_block.row == block.row and previous_block.row < next_block.row) and (previous_block.col > block.col and block.col == next_block.col):
                        game_screen.blit(left_body_snake, (block.col * CELL_SIZE, block.row * CELL_SIZE))
                    elif (previous_block.row == block.row and previous_block.row > next_block.row) and (previous_block.col > block.col and block.col == next_block.col):
                        game_screen.blit(down_body_snake, (block.col * CELL_SIZE, block.row * CELL_SIZE))
                    elif (previous_block.row > block.row and previous_block.row > next_block.row) and (previous_block.col == block.col and block.col < next_block.col):
                        game_screen.blit(left_body_snake, (block.col * CELL_SIZE, block.row * CELL_SIZE))
                    elif (previous_block.row > block.row and previous_block.row > next_block.row) and (previous_block.col == block.col and block.col > next_block.col):
                        game_screen.blit(right_body_snake, (block.col * CELL_SIZE, block.row * CELL_SIZE))
            
    def move_snake(self):
        nb_snake_block = len(self.body)
        old_head = self.body[nb_snake_block - 1]
        
        if self.direction == "RIGHT":
            new_head = Block(old_head.col + 1, old_head.row)
        elif self.direction == "LEFT":
            new_head = Block(old_head.col - 1, old_head.row)
        elif self.direction == "TOP":
            new_head = Block(old_head.col, old_head.row - 1)
        else:
            new_head = Block(old_head.col, old_head.row + 1)
        
        self.body.append(new_head)
        
        
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = snake_food()
        self.obstacle = Obstacle()
        self.auto_generate_food()
        self.score = 0
        self.level = 100
        self.game_sound = pg.mixer.Sound('Sons/game_sound.mp3')

    def update_snake_moves(self):
        self.snake.move_snake()
        self.check_collision_snake_food()
        self.game_over()

    def draw_game_elements(self):
        self.snake.draw_snake()
        self.food.draw_snake_food()
        self.obstacle.draw_obstacle()

    def check_collision_snake_food(self):
        snake_length = len(self.snake.body)
        snake_head_block = self.snake.body[snake_length - 1]
        food_block = self.food.block_food
        if snake_head_block.col == food_block.col and snake_head_block.row == food_block.row:
            self.auto_generate_food()
            self.score += 2
            crunch_sound = pg.mixer.Sound('Sons/crunch.wav')
            crunch_sound.play()
            if self.score == 10:
                self.level = 80
            elif self.score == 20:
                self.level = 60
            elif self.score == 30:
                self.level = 40
        else:
            self.snake.body.pop(0)

    def auto_generate_food(self):
        generate = True
        while generate:
            count = 0
            for block in self.snake.body:
                if block.col == self.food.block_food.col and block.row == self.food.block_food.row:
                    count += 1
            if count == 0:
                generate = False
            else:
                self.food = snake_food()

            for block in self.obstacle.obstacle_block:
                if block.col == self.food.block_food.col and block.row == self.food.block_food.row:
                    count += 1
            if count == 0:
                generate = False
            else:
                self.food = snake_food()

    def save_scores(self):
        file_score = open(
            r"C:\Users\henri_t4z\Documents\HETIC\MON_PARCOURS_HETIC\MD4\SEMESTRE_1\COMPUTER_SCIENCE_BASICS\HENRI_OTHNIEL_GOHI_PROJET_SNAKE\scores.txt",
            "a")
        file_score.write(str(self.score) + "\n")
        file_score.close()

    def high_score(self):
        high_score_list = []

        with open(r"C:\Users\henri_t4z\Documents\HETIC\MON_PARCOURS_HETIC\MD4\SEMESTRE_1\COMPUTER_SCIENCE_BASICS\HENRI_OTHNIEL_GOHI_PROJET_SNAKE\scores.txt", "r") as f:
            content = f.read()
            for i in content.split("\n"):
                if i != '':
                    high_score_list.append(int(i))

        return max(high_score_list)

    def game_over(self):
        text_font_game_over = pg.font.SysFont("monospace", 30, True)
        game_over_text = text_font_game_over.render(
            "Game Over !", True, (200, 0, 0))
        snake_length = len(self.snake.body)
        snake_head = self.snake.body[snake_length - 1]

        if (snake_head.col not in range(1, NB_COL - 1)
            ) or snake_head.row not in range(1, NB_ROW - 1):
            game_screen.blit(game_over_text, (200, 730))
            pg.display.update()

            Game.save_scores(self)

            game_over_sound = pg.mixer.Sound('Sons/game_over.wav')
            self.game_sound.stop()
            game_over_sound.play()
            time.sleep(3)
            notice_game()
            begin()

        for block in self.snake.body[0:snake_length - 1]:
            if block.col == snake_head.col and block.row == snake_head.row:
                game_over_sound = pg.mixer.Sound('Sons/game_over.wav')
                game_over_sound.play()
                self.game_sound.stop()
                game_screen.blit(game_over_text, (200, 730))

                Game.save_scores(self)

                pg.display.update()
                time.sleep(3)
                notice_game()
                begin()

        for block in self.obstacle.obstacle_block:
            if block.col == snake_head.col and block.row == snake_head.row:
                game_over_sound = pg.mixer.Sound('Sons/game_over.wav')
                game_over_sound.play()
                self.game_sound.stop()
                game_screen.blit(game_over_text, (200, 730))

                Game.save_scores(self)

                pg.display.update()
                time.sleep(3)
                notice_game()
                begin()


def begin():
    game_start = True

    game = Game()
    game.game_sound.play()
    SCREEN_UPDATE = pg.USEREVENT
    pg.time.set_timer(SCREEN_UPDATE, game.level)

    while game_start:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                pg.time.set_timer(SCREEN_UPDATE, game.level)
                game.update_snake_moves()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    if game.snake.direction != "DOWN":
                        game.snake.direction = "TOP"
                if event.key == pg.K_DOWN:
                    if game.snake.direction != "TOP":
                        game.snake.direction = "DOWN"
                if event.key == pg.K_RIGHT:
                    if game.snake.direction != "LEFT":
                        game.snake.direction = "RIGHT"
                if event.key == pg.K_LEFT:
                    if game.snake.direction != "RIGHT":
                        game.snake.direction = "LEFT"
                if event.key == pg.K_SPACE:
                    game_start = False
                    game_paused()
                    game_start = True
                    pg.display.update()

        fond_ecran = pg.image.load('Images/fond_ecran.jpg')
        fond_ecran = pg.transform.scale(fond_ecran, (600, 800))
        game_screen.blit(fond_ecran, (0, 0))
        draw_grid()
        game.draw_game_elements()
        info_game_surface.fill(pg.Color("lightblue"))
        game_screen.blit(info_game_surface, (0, 600))
        game_screen.blit(title_text, (200, 610))
        score_text = text_font_score.render(
            "Score : {}".format(str(game.score)), True, (0, 0, 0))
        game_screen.blit(score_text, (220, 650))

        high_score = game.high_score()

        high_score_text = text_font_score.render(
            "Meilleur score : {}".format(
                str(high_score)), True, (0, 0, 0))
        game_screen.blit(high_score_text, (120, 690))

        pg.display.update()
        timer.tick(60)


begin()