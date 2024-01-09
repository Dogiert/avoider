import random

import pygame
from display_draw import Display
import player
import enemy
from enemy import Enemy

pygame.init()

board_width = 600
board_height = 600

clock = pygame.time.Clock()
enemy_list = []
enemy_counter = 0
time_zero = pygame.time.get_ticks()
last_enemy_time = 0
last_bullet_time = 0

if __name__ == '__main__':
    direction_of_movement = 0
    game_over = False

    pygame.display.set_caption('Avoider')
    board = Display(board_width, board_height)
    surface = board.draw_board()

    player_square = player.Player()
    if len(enemy_list) == 0:
        enemy_list.append(enemy.Enemy())
    else:
        while len(enemy_list) != enemy_counter:
                enemy_list.append(enemy.Enemy.add_new_enemy())

    while not game_over:

        surface.fill(pygame.color.THECOLORS['azure2'])
        delta_time = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    direction_of_movement = event.key

        player_square.draw_player(surface)
        current_time = round((pygame.time.get_ticks() - time_zero)  / 1000)
        for enemy in enemy_list:
            enemy.draw_enemy(surface)
            enemy.draw_bullet(surface, delta_time, board_width)
        player_square.player_move(delta_time, direction_of_movement, board_height)
        pygame.display.update()

        if current_time - last_bullet_time >= 2:
            for enemy in enemy_list:
                enemy.add_bullet()
            last_bullet_time = current_time
            if current_time - last_enemy_time >= 2:
                enemy_list.append(Enemy.add_new_enemy())
                for enemy in enemy_list:
                    enemy.add_bullet()
                last_enemy_time = current_time
        for enemy in enemy_list:
            for bullet in enemy.bullet_positions:
                if player_square.collison_with_bullet(int(bullet[0]), int(bullet[1]), 10):
                    game_over = True
                    print(f'Przeżyłeś milisekund: {round(time_zero)}')
        if len(enemy_list) % 3 == 0:
            for enemy in enemy_list[:-1]:
                enemy.position_y = random.randrange(0,board_height-10, 10)
    pygame.quit()
    quit()